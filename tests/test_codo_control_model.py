"""Host-side specification checks; these do NOT compile or execute NXC."""

from pathlib import Path
import json
import math
import re
import unittest


SOURCE = Path(__file__).resolve().parents[1] / "robot_prueba_codo.nxc"
EXIT_LIMIT = 50


def position_model(readings, start=(0, 0)):
    """Zero means permission to pivot, not a terminal NXC stop reason."""
    if 30000 in start:
        return 8, 0
    for samples, (a, c, left, right) in enumerate(readings[:30], 1):
        if left > 75 or right > 75:
            return 1, samples
        if a == 30000 or c == 30000:
            return 8, samples
        da, dc = a - start[0], c - start[1]
        if da < 0 or dc < 0:
            return 7, samples
        if da >= 60 or dc >= 60:
            return (0 if da >= 60 and dc >= 60 else 13), samples
    if len(readings) < 30:
        raise ValueError("Model input ended before positioning cap or a stop event")
    return 12, 30


def turn_model(readings, confirmation, start=(0, 0)):
    """Model only the post-approach turn and stopped confirmation phases."""
    if 30000 in start:
        return 8, 0, 0
    for samples, (a, c, left, right) in enumerate(readings[:240], 1):
        if left > 75 or right > 75:
            return 1, samples, 0
        if a == 30000 or c == 30000:
            return 8, samples, 0
        da, dc = a - start[0], c - start[1]
        if da != 0 or dc < 0:
            return 7, samples, 0
        if dc >= 743:
            stable = 0
            previous_state = 0
            for left, right in confirmation[:3]:
                if left > 75 or right > 75:
                    return 1, samples, stable
                if left < 25:
                    state = 3 if right < 25 else 1
                else:
                    state = 2 if right < 25 else 0
                if state == 0:
                    return 6, samples, stable
                stable = stable + 1 if state == previous_state else 1
                previous_state = state
            return (5 if stable == 3 else 6), samples, stable
    return 4, min(len(readings), 240), 0


def exit_model(turn_reason, readings, final_reading=(0, 0)):
    """Model the gated exit; each command is (C power, A power)."""
    commands = []
    if turn_reason != 5:
        return turn_reason, commands
    for left, right in readings[:EXIT_LIMIT]:
        if left > 75 or right > 75:
            return 1, commands
        if left < 25:
            commands.append((20, 20) if right < 25 else (0, 15))
        elif right < 25:
            commands.append((15, 0))
        else:
            return 11, commands
    if len(commands) < EXIT_LIMIT:
        raise ValueError("Model input ended before the exit bound or a stop event")
    left, right = final_reading
    if left > 75 or right > 75:
        return 1, commands
    if left >= 25 and right >= 25:
        return 11, commands
    return 10, commands


class CornerControlModelTests(unittest.TestCase):
    def test_positioning_allows_gray_only_within_encoder_bound(self):
        readings = [(3 * i, 3 * i, 49, 49) for i in range(1, 31)]
        self.assertEqual(position_model(readings), (0, 20))

    def test_positioning_stops_on_first_motor_if_other_is_short(self):
        self.assertEqual(position_model([(60, 59, 49, 49)]), (13, 1))
        self.assertEqual(position_model([(59, 60, 49, 49)]), (13, 1))

    def test_positioning_stall_does_not_enable_pivot(self):
        self.assertEqual(position_model([(0, 0, 49, 49)] * 30), (12, 30))

    def test_positioning_wrong_direction_does_not_enable_pivot(self):
        self.assertEqual(position_model([(-1, 1, 49, 49)]), (7, 1))
        self.assertEqual(position_model([(1, -1, 49, 49)]), (7, 1))

    def test_positioning_white_on_either_sensor_aborts(self):
        self.assertEqual(position_model([(30, 30, 100, 49)]), (1, 1))
        self.assertEqual(position_model([(30, 30, 49, 100)]), (1, 1))

    def test_positioning_white_has_priority_over_reaching_target(self):
        self.assertEqual(position_model([(60, 60, 100, 0)]), (1, 1))

    def test_positioning_sentinel_aborts(self):
        self.assertEqual(position_model([], start=(30000, 0)), (8, 0))
        self.assertEqual(position_model([(30000, 30, 49, 49)]), (8, 1))

    def test_positioning_uses_independent_relative_baselines(self):
        self.assertEqual(position_model([(160, 260, 49, 49)], start=(100, 200)), (0, 1))

    def test_black_reacquisition_cannot_shorten_position_target(self):
        readings = [(2 * i, 2 * i, 0, 0) for i in range(1, 31)]
        self.assertEqual(position_model(readings), (0, 30))

    def test_positioning_overshoot_is_logged_but_does_not_extend_motion(self):
        self.assertEqual(position_model([(63, 63, 49, 49)]), (0, 1))

    def test_early_black_cannot_complete_turn(self):
        readings = [(0, i * 4, 0, 0) for i in range(1, 187)]
        self.assertEqual(turn_model(readings, [(0, 0)] * 3), (5, 186, 3))

    def test_black_without_motor_progress_times_out(self):
        self.assertEqual(turn_model([(0, 0, 0, 0)] * 240, []), (4, 240, 0))

    def test_old_center_motor_target_cannot_complete_forward_pivot(self):
        self.assertEqual(turn_model([(0, 360, 0, 0)] * 240, [(0, 0)] * 3), (4, 240, 0))

    def test_target_without_black_fails_stopped(self):
        self.assertEqual(turn_model([(0, 746, 49, 49)], [(49, 49)]), (6, 1, 0))

    def test_target_requires_three_confirmation_samples(self):
        self.assertEqual(turn_model([(0, 743, 0, 0)], [(0, 0)] * 2), (6, 1, 2))

    def test_interrupted_confirmation_fails(self):
        self.assertEqual(turn_model([(0, 743, 0, 0)], [(0, 0), (0, 49)]), (6, 1, 1))

    def test_stable_left_only_black_can_enable_exit(self):
        self.assertEqual(turn_model([(0, 746, 0, 49)], [(0, 49)] * 3), (5, 1, 3))

    def test_stable_right_only_black_can_enable_exit(self):
        self.assertEqual(turn_model([(0, 746, 49, 0)], [(49, 0)] * 3), (5, 1, 3))

    def test_alternating_sides_cannot_confirm(self):
        self.assertEqual(
            turn_model([(0, 743, 0, 49)], [(0, 49), (49, 0), (0, 49)]),
            (6, 1, 1),
        )

    def test_change_from_edge_to_both_resets_confirmation(self):
        self.assertEqual(
            turn_model([(0, 743, 0, 49)], [(0, 49), (0, 0), (0, 0)]),
            (6, 1, 2),
        )

    def test_one_sided_gate_enters_correct_bounded_correction(self):
        reason, _, _ = turn_model([(0, 746, 0, 49)], [(0, 49)] * 3)
        exit_reason, commands = exit_model(reason, [(0, 49)] * 2 + [(0, 0)] * (EXIT_LIMIT - 2))
        self.assertEqual(exit_reason, 10)
        self.assertEqual(commands[:2], [(0, 15)] * 2)
        self.assertEqual(commands[2:], [(20, 20)] * (EXIT_LIMIT - 2))

    def test_stopped_motor_movement_invalidates_pivot(self):
        self.assertEqual(turn_model([(1, 743, 0, 0)], []), (7, 1, 0))
        self.assertEqual(turn_model([(-1, 743, 0, 0)], []), (7, 1, 0))

    def test_white_stops_before_encoder_target(self):
        self.assertEqual(turn_model([(0, 90, 100, 0)], []), (1, 1, 0))

    def test_white_during_confirmation_stops(self):
        self.assertEqual(turn_model([(0, 743, 0, 0)], [(0, 100)]), (1, 1, 0))

    def test_wrong_direction_stops(self):
        self.assertEqual(turn_model([(1, 2, 0, 0)], []), (7, 1, 0))
        self.assertEqual(turn_model([(-1, -2, 0, 0)], []), (7, 1, 0))

    def test_unassigned_encoder_stops(self):
        self.assertEqual(turn_model([], [], start=(30000, 0)), (8, 0, 0))
        self.assertEqual(turn_model([(30000, 30, 0, 0)], []), (8, 1, 0))

    def test_nonzero_baseline_uses_relative_progress(self):
        self.assertEqual(
            turn_model([(10, 763, 0, 0)], [(0, 0)] * 3, start=(10, 20)),
            (5, 1, 3),
        )

    def test_exit_is_disabled_for_every_turn_failure(self):
        for reason in (1, 2, 3, 4, 6, 7, 8, 9):
            with self.subTest(reason=reason):
                self.assertEqual(exit_model(reason, [(0, 0)] * EXIT_LIMIT), (reason, []))

    def test_exit_stops_after_50_commands(self):
        reason, commands = exit_model(5, [(0, 0)] * 100)
        self.assertEqual(reason, 10)
        self.assertEqual(commands, [(20, 20)] * EXIT_LIMIT)

    def test_exit_does_not_stop_at_old_25_step_cap(self):
        reason, commands = exit_model(5, [(0, 0)] * 25 + [(49, 49)])
        self.assertEqual((reason, len(commands)), (11, 25))

    def test_prior_23_step_line_loss_still_stops_immediately(self):
        reason, commands = exit_model(5, [(0, 0)] * 23 + [(49, 49)] + [(0, 0)] * 30)
        self.assertEqual((reason, len(commands)), (11, 23))

    def test_exit_loss_never_triggers_another_turn(self):
        self.assertEqual(exit_model(5, [(0, 0)] * 3 + [(49, 49)]), (11, [(20, 20)] * 3))

    def test_exit_initial_loss_commands_no_motion(self):
        self.assertEqual(exit_model(5, [(49, 49)]), (11, []))

    def test_exit_white_on_either_sensor_stops(self):
        self.assertEqual(exit_model(5, [(100, 0)]), (1, []))
        self.assertEqual(exit_model(5, [(0, 100)]), (1, []))

    def test_exit_one_sided_corrections_brake_inner_track(self):
        reason, commands = exit_model(5, [(0, 49), (49, 0)] + [(0, 0)] * (EXIT_LIMIT - 2))
        self.assertEqual(reason, 10)
        self.assertEqual(commands[:3], [(0, 15), (15, 0), (20, 20)])

    def test_exit_stops_after_one_sided_contact_is_lost(self):
        self.assertEqual(exit_model(5, [(49, 0), (49, 49)]), (11, [(15, 0)]))

    def test_exit_correction_has_lower_advance_and_tighter_ideal_curvature(self):
        # Command-space comparison under proportional drive response, NOT
        # a simulator stability test or a claim of actual line recovery.
        old = (10, 25)
        new = (0, 15)
        self.assertLess(sum(new), sum(old))
        self.assertEqual(abs(new[1] - new[0]), abs(old[1] - old[0]))
        self.assertGreater(
            abs(new[1] - new[0]) / sum(new),
            abs(old[1] - old[0]) / sum(old),
        )

    def test_exit_checks_loss_after_final_command(self):
        reason, commands = exit_model(5, [(0, 0)] * EXIT_LIMIT, final_reading=(49, 49))
        self.assertEqual((reason, len(commands)), (11, EXIT_LIMIT))

    def test_exit_final_white_has_priority(self):
        reason, commands = exit_model(5, [(0, 0)] * EXIT_LIMIT, final_reading=(100, 0))
        self.assertEqual((reason, len(commands)), (1, EXIT_LIMIT))

    def test_exit_threshold_boundary_is_not_black(self):
        self.assertEqual(exit_model(5, [(25, 25)]), (11, []))

    def test_nxc_source_safety_structure(self):
        source = SOURCE.read_text()
        self.assertEqual(source.count("{"), source.count("}"))
        for forbidden in ("&&", "||", "PlayTone(", "TextOut("):
            self.assertNotIn(forbidden, source)
        default_source = re.sub(
            r"^#if (?:EXIT_(?:MEASURE_ENCODERS|REQUIRE_PROGRESS)|ENABLE_CONTINUATION|TURN_PROGRESS_GUARD|TURN_REFRESH_COMMAND) == 1\n.*?^#endif\n", "", source,
            flags=re.M | re.S,
        )
        self.assertEqual(default_source.count("SetInput("), 39)
        self.assertEqual(source.count("SetInput("), 76)
        self.assertEqual(source.count("OnRev("), 0)
        approach, positioning = source.split("    if (phase == 4)", 1)
        positioning, turn = positioning.split("    if (phase == 1)", 1)
        self.assertIn("phase = 4;", approach)
        self.assertNotIn("phase = 1;", approach)
        self.assertEqual(positioning.count("OnFwd("), 1)
        self.assertIn("OnFwd(OUT_AC, POSITION_POWER);", positioning)
        self.assertLess(positioning.index("OnFwd("), positioning.index("for (positionStep"))
        self.assertIn("if (positionDeltaA >= POSITION_COUNT_TARGET)", positioning)
        self.assertIn("if (positionDeltaC >= POSITION_COUNT_TARGET)", positioning)
        self.assertIn("phase = 1;", positioning)
        self.assertIn("stopReason = 12;", positioning)
        self.assertIn("stopReason = 13;", positioning)
        self.assertTrue(positioning.rstrip().endswith("Off(OUT_AC);"))
        turn, confirm = turn.split("    if (phase == 2)", 1)
        confirm, exit_section = confirm.split("    if (stopReason == 5)", 1)
        self.assertEqual(turn.count("OnFwd("), 1)
        self.assertLess(turn.index("Off(OUT_A);"), turn.index("for (turnStep"))
        self.assertLess(turn.index("OnFwd(OUT_C, TURN_POWER);"), turn.index("for (turnStep"))
        self.assertIn("if (deltaA > 0)", turn)
        self.assertIn("if (deltaA < 0)", turn)
        self.assertNotIn("OnFwd(", confirm)
        self.assertNotIn("OnRev(", confirm)
        self.assertIn("sampleState == confirmationState", confirm)
        self.assertIn("confirmationState = sampleState;", confirm)
        self.assertIn("stable = 1;", confirm)
        self.assertNotIn("OnRev(", exit_section)
        self.assertIn("phase = 3;", exit_section)
        self.assertIn("exitStep < EXIT_STEPS", exit_section)
        self.assertIn("stopReason = 11;", exit_section)
        left_correction = exit_section.split("exitLeftSamples++;", 1)[1].split("}", 1)[0]
        right_correction = exit_section.split("exitRightSamples++;", 1)[1].split("}", 1)[0]
        self.assertLess(left_correction.index("Off(OUT_C);"), left_correction.index("OnFwd(OUT_A,"))
        self.assertLess(right_correction.index("Off(OUT_A);"), right_correction.index("OnFwd(OUT_C,"))
        self.assertIn("OnFwd(OUT_AC, EXIT_FORWARD_POWER);", exit_section)
        self.assertLess(
            exit_section.index("Off(OUT_AC);\n        // Check again"),
            exit_section.index("leftReading = Sensor(IN_3);", exit_section.index("// Check again")),
        )
        defines = dict(re.findall(r"^#define (\w+) (-?\d+)$", source, re.M))
        self.assertEqual(int(defines["MOTOR_COUNT_TARGET"]), 743)
        self.assertEqual(int(defines["TURN_SAMPLE_LIMIT"]), 240)
        self.assertEqual(int(defines["CONFIRM_SAMPLES"]), 3)
        self.assertEqual(int(defines["EXIT_STEPS"]), EXIT_LIMIT)
        self.assertEqual(int(defines["POSITION_COUNT_TARGET"]), 60)
        self.assertEqual(int(defines["POSITION_SAMPLE_LIMIT"]), 30)
        self.assertEqual(int(defines["POSITION_POWER"]), 15)
        self.assertEqual(int(defines["EXIT_CORRECTION_POWER"]), 15)
        self.assertIn("SetInput(IN_1, ScaledValue, CORNER_REVISION);", source)
        self.assertIn("SetInput(IN_1, ScaledValue, confirmationState);", source)

    def test_target_matches_static_physics_evidence(self):
        evidence = json.loads(
            (SOURCE.parent / "evidence/robosim-physics-2026-11-06.json").read_text()
        )
        constants = evidence["constants"]
        distance = constants["motor_distance_factor"]["value"] * constants["count_angle_factor"]["value"]
        width = constants["drive_spacing"]["value"]
        reference = (math.pi / 2) * width / distance
        self.assertAlmostEqual(reference, 742.5, places=3)
        self.assertEqual(math.ceil(reference), evidence["derivation"]["chosen_integer_motor_target"])
        self.assertEqual(math.ceil(reference), 743)

    def test_static_physics_model_old_target_underturns(self):
        # Host-side example of the recovered per-step atan integration,
        # NOT a measurement of live heading, collision, or track containment.
        scale = 0.4000000059604645 * 0.008726646192371845
        width = 1.649999976158142

        def yaw(count):
            full_steps, remainder = divmod(count, 4)
            return math.degrees(
                full_steps * math.atan(4 * scale / width)
                + math.atan(remainder * scale / width)
            )

        self.assertLess(yaw(720), 88)
        self.assertLess(abs(yaw(743) - 90), 0.2)


if __name__ == "__main__":
    unittest.main()
