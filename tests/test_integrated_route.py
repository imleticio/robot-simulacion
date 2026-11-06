"""Execute the actual integrated NXC stages as C with mocked IO, NOT RoboSim."""
import ctypes
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HARNESS = r'''
#define OUT_A 1
#define OUT_C 4
#define OUT_AC 5
#define IN_1 1
#define IN_3 3
#define IN_4 4
#define ScaledValue 4
#define RESET_NONE 0
extern int lapPhase, lapSamples, lapTurn;
int mode, ticks, powerA, powerC, tones, frameFields, loggingPowered, stoppedAfterMotion;
long rawA, rawC;
void Off(int ports) {
    if (powerA != 0 || powerC != 0) { stoppedAfterMotion = 1; }
    if (ports & OUT_A) { powerA = 0; rawA = 0; }
    if (ports & OUT_C) { powerC = 0; rawC = 0; }
}
void OnFwd(int ports, int power) {
    stoppedAfterMotion = 0;
    if (ports & OUT_A) { powerA = power; rawA = 0; }
    if (ports & OUT_C) { powerC = power; rawC = 0; }
}
void OnFwdEx(int ports, int power, int reset) {
    if (reset != RESET_NONE) { OnFwd(ports, power); return; }
    if (ports & OUT_A) { powerA = power; }
    if (ports & OUT_C) { powerC = power; }
}
void Wait(int ms) {
    (void)ms;
    ticks++;
    if (mode == 1) { return; }
    if (mode == 22) {
        if (powerA != 0) { rawA++; }
        if (powerC != 0) { rawC++; }
        return;
    }
    rawA += powerA / 4;
    rawC += powerC / 4;
    if (mode == 8 && ticks > 2) { rawC = -1; }
    if (mode == 9) { rawA++; rawC++; }
}
long MotorRotationCount(int port) {
    if (mode == 2) { return 30000; }
    if (mode == 3 && ticks > 0) { return 30000; }
    return port == OUT_A ? rawA : rawC;
}
int MotorPower(int port) {
    if (mode == 4) { return 0; }
    if (mode == 5) { return 30000; }
    return port == OUT_A ? powerA : powerC;
}
int Sensor(int port) {
    if (mode == 6) { return 101; }
    if (mode == 7) { return 100; }
    if (mode == 10) { return port == IN_3 ? 0 : 49; }
    if (mode == 11) { return 49; }
    if (mode == 12 && ticks >= 60) { return 100; }
    if (mode == 13 && lapPhase == 2 && lapTurn == 1) { return 100; }
    if (mode == 14 && lapPhase == 3 && lapTurn == 5) { return 100; }
    if (mode == 15 && lapPhase == 1) { return 100; }
    if (mode == 16 && lapPhase == 5 && ticks >= 65) { return 49; }
    if (mode == 17 && lapSamples >= 400) { return port == IN_3 ? 0 : 49; }
    if (mode == 18 && stoppedAfterMotion) { return 100; }
    if (mode == 19 && stoppedAfterMotion) { return port == IN_3 ? 0 : 49; }
    if (mode >= 20) { return 0; } // Constant black for individual-stage tests.
    if (mode == 0 || mode == 13 || mode == 14 || mode == 15) {
        if (lapPhase == 0) { return ticks >= 6 ? 100 : 0; }
        if (lapPhase == 1) { return lapSamples >= 5 ? 0 : 100; }
        if (lapPhase == 6) { return lapSamples >= 5 ? 100 : 0; }
        if (lapPhase == 2) {
            if (lapTurn == 1 || lapTurn == 7) { return 0; }
            return lapSamples >= 10 ? 49 : 0;
        }
    }
    return 0;
}
void SetInput(int port, int field, long value) {
    (void)port; (void)field; (void)value;
    frameFields++;
    if (powerA != 0 || powerC != 0) { loggingPowered++; }
}
void SetSensorLight(int port) { (void)port; }
void PlayTone(int frequency, int duration) {
    (void)frequency; (void)duration; tones++;
}
'''


class IntegratedRouteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("clang")
        if not compiler:
            raise unittest.SkipTest("clang unavailable")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-route-")
        cls.addClassCleanup(cls.temp.cleanup)
        source = Path(cls.temp.name) / "route.c"
        source.write_text(HARNESS + '\n#include "' +
                          str(ROOT / "robot_route_stages.nxc") + '"\n')
        library = Path(cls.temp.name) / "route.so"
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        subprocess.run([compiler, *flags, "-std=c99", "-Wall", "-Wextra", "-Werror",
                        str(source), "-o", str(library)], check=True,
                       capture_output=True, text=True)
        cls.lib = ctypes.CDLL(str(library))

    def field(self, name, kind=ctypes.c_int):
        return kind.in_dll(self.lib, name)

    def val(self, name, kind=ctypes.c_int):
        return self.field(name, kind).value

    def setUp(self):
        for name in ("mode", "ticks", "powerA", "powerC", "tones", "frameFields",
                     "loggingPowered", "lapReason", "lapPhase", "lapTurn",
                     "stoppedAfterMotion",
                     "lapCompletedTurns", "lapStarted", "lapCandidate",
                     "lapRefreshes", "lapPowerMismatches"):
            self.field(name).value = 0
        for name in ("rawA", "rawC", "lapPivotA", "lapPivotC"):
            self.field(name, ctypes.c_long).value = 0
        self.lib.RouteResetStage()
        self.lib.ConfigureRouteTurn(0)

    def run_stage(self, name, mode=20, *args):
        self.field("mode").value = mode
        result = getattr(self.lib, name)(*args)
        self.assertEqual(self.val("powerA"), 0)
        self.assertEqual(self.val("powerC"), 0)
        return result

    def test_complete_mock_route_has_two_tones_and_candidate_not_two_laps(self):
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 100)
        self.assertEqual(self.val("lapCompletedTurns"), 18)
        self.assertEqual(self.val("lapCandidate"), 1)
        self.assertEqual(self.val("tones"), 2)
        self.assertEqual(self.val("frameFields") % 24, 0)
        self.assertEqual(self.val("loggingPowered"), 0)
        self.assertEqual(self.val("powerA"), 0)
        self.assertEqual(self.val("powerC"), 0)

    def test_route_directions_and_only_two_reference_decisions(self):
        directions = []
        references = []
        for turn in range(18):
            self.assertEqual(self.lib.ConfigureRouteTurn(turn), 1)
            directions.append(self.val("routeDirection"))
            if self.val("routeTrigger") == 1:
                references.append((turn, self.val("routeReference", ctypes.c_long)))
        self.assertEqual(directions, [-1, 1, 1, 1, 1, -1, -1, 1, 1,
                                      1, 1, -1, -1, 1, -1, -1, -1, -1])
        self.assertEqual(references, [(1, 1200), (7, 450)])
        for turn in (-1, 18, 99):
            self.assertEqual(self.lib.ConfigureRouteTurn(turn), 0)
            self.assertEqual(self.val("routeDirection"), 0)

    def test_right_pivot_retains_original_baseline_across_refreshes(self):
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RoutePivot"), 1)
        self.assertEqual(self.val("lapPivotC", ctypes.c_long), 744)
        self.assertEqual(self.val("lapPivotA", ctypes.c_long), 0)
        self.assertEqual(self.val("lapSamples"), 248)
        self.assertEqual(self.val("lapRefreshes"), 248)

    def test_left_pivot_is_explicit_mirrored_new_motion(self):
        self.assertEqual(self.run_stage("RoutePivot"), 1)
        self.assertEqual(self.val("lapPivotA", ctypes.c_long), 744)
        self.assertEqual(self.val("lapPivotC", ctypes.c_long), 0)

    def test_pivot_stall_stops_at_40_without_exit(self):
        self.assertEqual(self.run_stage("RoutePivot", 1), 0)
        self.assertEqual(self.val("lapReason"), 21)
        self.assertEqual(self.val("lapSamples"), 40)

    def test_slow_pivot_retains_separate_375_sample_hard_watchdog(self):
        self.assertEqual(self.run_stage("RoutePivot", 22), 0)
        self.assertEqual(self.val("lapReason"), 4)
        self.assertEqual(self.val("lapSamples"), 375)

    def test_each_forward_stage_stops_stalled_motion(self):
        for name, args in (("RouteFollow", ()), ("RouteExit", ()), ("RouteMarker", (0,))):
            with self.subTest(stage=name):
                self.setUp()
                self.assertEqual(self.run_stage(name, 1, *args), 0)
                self.assertEqual(self.val("lapReason"), 21)
                self.assertEqual(self.val("lapSamples"), 40)

    def test_invalid_marker_mode_stops_before_motion(self):
        self.assertEqual(self.run_stage("RouteMarker", 20, 3), 0)
        self.assertEqual(self.val("lapReason"), 25)
        self.assertEqual(self.val("ticks"), 0)

    def test_pivot_faults_stop_without_success(self):
        for mode, reason in ((2, 8), (3, 8), (4, 22), (5, 8), (6, 26),
                             (7, 1), (8, 7), (9, 7), (11, 6)):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_stage("RoutePivot", mode), 0)
                self.assertEqual(self.val("lapReason"), reason)

    def test_exit_requires_both_motors_and_five_fresh_black_samples(self):
        self.assertEqual(self.run_stage("RouteExit"), 1)
        self.assertEqual(self.val("lapStable"), 5)
        self.assertGreaterEqual(self.val("lapTotalA", ctypes.c_long), 180)
        self.assertGreaterEqual(self.val("lapTotalC", ctypes.c_long), 180)

    def test_one_sided_exit_is_not_a_pass(self):
        self.assertEqual(self.run_stage("RouteExit", 10), 0)
        self.assertEqual(self.val("lapReason"), 15)

    def test_follow_cannot_pivot_when_starting_already_on_gray(self):
        self.assertEqual(self.run_stage("RouteFollow", 11), 0)
        self.assertEqual(self.val("lapReason"), 11)
        self.assertEqual(self.val("lapSamples"), 0)

    def test_reference_needs_contact_and_does_not_accept_early_line_loss(self):
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RouteFollow", 11), 0)
        self.assertEqual(self.val("lapReason"), 11)

    def test_reference_stops_on_one_sided_contact_at_the_requested_reference(self):
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RouteFollow", 17), 0)
        self.assertEqual(self.val("lapReason"), 23)
        self.assertEqual(self.val("lapSamples"), 400)

    def test_reference_pass_is_only_a_sampled_endpoint_not_junction_recognition(self):
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RouteFollow"), 1)
        self.assertEqual(self.val("lapSamples"), 400)

    def test_stopped_exit_resample_cannot_hide_white_or_one_sided_contact(self):
        for mode, reason in ((18, 1), (19, 15)):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_stage("RouteExit", mode), 0)
                self.assertEqual(self.val("lapReason"), reason)

    def test_follow_stopped_resample_cannot_hide_white(self):
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RouteFollow", 18), 0)
        self.assertEqual(self.val("lapReason"), 1)

    def test_straight_follow_is_bounded_not_a_false_junction_detector(self):
        self.assertEqual(self.run_stage("RouteFollow"), 0)
        self.assertEqual(self.val("lapReason"), 3)
        self.assertEqual(self.val("lapSamples"), 2000)

    def test_persistent_correction_keeps_60_count_difference_guard(self):
        self.assertEqual(self.run_stage("RouteFollow", 10), 0)
        self.assertEqual(self.val("lapReason"), 19)

    def test_early_white_stops_route_instead_of_counting_lap(self):
        self.field("mode").value = 13
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 1)
        self.assertEqual(self.val("lapCompletedTurns"), 1)
        self.assertEqual(self.val("lapCandidate"), 0)
        self.assertEqual(self.val("tones"), 1)

    def test_mid_route_fault_cannot_skip_a_turn(self):
        self.field("mode").value = 14
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 1)
        self.assertEqual(self.val("lapCompletedTurns"), 5)
        self.assertEqual(self.val("lapCandidate"), 0)

    def test_white_release_watchdog_is_not_a_route_start(self):
        self.field("mode").value = 15
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 24)
        self.assertEqual(self.val("lapCompletedTurns"), 0)
        self.assertEqual(self.val("tones"), 1)

    def test_finish_requires_full_ordered_sequence(self):
        self.field("lapStarted").value = 1
        self.assertEqual(self.run_stage("RouteMarker", 7, 2), 0)
        self.assertEqual(self.val("lapReason"), 25)
        self.assertEqual(self.val("tones"), 0)
        self.assertEqual(self.val("lapCandidate"), 0)

    def test_finish_also_requires_observed_start_marker(self):
        self.field("lapCompletedTurns").value = 18
        self.assertEqual(self.run_stage("RouteMarker", 7, 2), 0)
        self.assertEqual(self.val("lapReason"), 25)
        self.assertEqual(self.val("tones"), 0)

    def test_invalid_start_never_moves_or_sounds(self):
        self.field("mode").value = 11
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 2)
        self.assertEqual(self.val("lapStarted"), 0)
        self.assertEqual(self.val("tones"), 0)


if __name__ == "__main__":
    unittest.main()
