"""Nominal pivot budget and progress guards, not wall-time or pose proof."""
import json
import math
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


def pivot_progress(readings, cap=375):
    previous = progress = flat = consecutive = longest = 0
    for samples, current in enumerate(readings[:cap], 1):
        if current == 30000:
            return 8, samples, progress, flat, longest
        if current < previous:
            return 7, samples, progress, flat, longest
        if current > previous:
            progress += 1
            consecutive = 0
        else:
            flat += 1
            consecutive += 1
            longest = max(longest, consecutive)
        previous = current
        if consecutive >= 40:
            return 21, samples, progress, flat, longest
        if current >= 743:
            return 5, samples, progress, flat, longest
    if len(readings) < cap:
        raise ValueError("Incomplete pivot trace")
    return 4, cap, progress, flat, longest


class TurnBudgetTests(unittest.TestCase):
    def test_budget_matches_inspected_ordinary_motor_model(self):
        evidence = json.loads((ROOT / "evidence/robosim-scheduler-audit-2026-11-06.json").read_text())
        self.assertIn("150 counts/s", evidence["static_evidence"]["motor_speed"])
        minimum = math.ceil(743 / (150 * 0.020))
        self.assertEqual(minimum, 248)
        self.assertLess(240 * 0.020, 743 / 150)
        self.assertGreaterEqual(375, math.ceil(1.5 * minimum))

    def test_old_cap_rejects_ideal_20ms_progress_before_target(self):
        result = pivot_progress([3 * i for i in range(1, 376)], cap=240)
        self.assertEqual(result, (4, 240, 240, 0, 0))

    def test_new_cap_allows_same_progress_to_target(self):
        self.assertEqual(pivot_progress([3 * i for i in range(1, 376)]),
                         (5, 248, 248, 0, 0))

    def test_sustained_zero_progress_stops_before_overall_cap(self):
        self.assertEqual(pivot_progress([0] * 375), (21, 40, 0, 40, 40))

    def test_progress_then_frozen_encoder_is_distinguished(self):
        self.assertEqual(pivot_progress([3 * i for i in range(1, 21)] + [60] * 40),
                         (21, 60, 20, 40, 40))

    def test_flat_run_resets_on_real_progress(self):
        samples = [0] * 39 + [3] + [3] * 39 + [746]
        self.assertEqual(pivot_progress(samples), (5, 80, 2, 78, 39))

    def test_slow_but_continuous_motion_still_has_absolute_watchdog(self):
        self.assertEqual(pivot_progress(list(range(1, 376))), (4, 375, 375, 0, 0))

    def test_backwards_jump_is_not_a_normal_flat_sample(self):
        self.assertEqual(pivot_progress([10, 9]), (7, 2, 1, 0, 0))

    def test_sentinel_stops_without_fabricating_progress(self):
        self.assertEqual(pivot_progress([3, 30000]), (8, 2, 1, 0, 0))

    def test_wrapper_changes_only_watchdog_progress_guard_and_revision(self):
        def defines(name):
            return dict(line.split()[1:3] for line in (ROOT / name).read_text().splitlines()
                        if line.startswith("#define"))
        expected = defines("robot_prueba_codo_continuo_sin_avance.nxc")
        expected.update(CORNER_REVISION="110", TURN_SAMPLE_LIMIT="375", TURN_PROGRESS_GUARD="1")
        self.assertEqual(defines("robot_prueba_codo_tiempo.nxc"), expected)

    def test_preprocessing_preserves_motion_commands_and_old_layout(self):
        compiler = shutil.which("clang")
        if not compiler:
            self.skipTest("clang unavailable; NBC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_codo_continuo_sin_avance.nxc")
        new = preprocess("robot_prueba_codo_tiempo.nxc")
        self.assertEqual(old.count("SetInput("), 68)
        self.assertEqual(new.count("SetInput("), 72)
        self.assertIn("SetInput(IN_1, ScaledValue, 110);", new)
        self.assertIn("turnStep < 375", new)
        self.assertIn("deltaC >= 743", new)
        self.assertIn("turnFlatRun >= 40", new)
        self.assertIn("stopReason = 21;", new)
        self.assertNotIn("turnFlatRun", old)
        for command in ("OnFwd(", "Off(", "OnRev(", "Wait(", "MotorRotationCount("):
            self.assertEqual(old.count(command), new.count(command))
        for forbidden in ("&&", "||", "PlayTone("):
            self.assertNotIn(forbidden, new)
