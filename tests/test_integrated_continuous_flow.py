"""116handoff/progress tests on actual NXC helpers with mocked IO, NOT physics."""
import ctypes
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest

import test_integrated_route as route_test

ROOT = route_test.ROOT


class IntegratedContinuousFlowTests(unittest.TestCase):
    field = route_test.IntegratedRouteTests.field
    val = route_test.IntegratedRouteTests.val
    run_stage = route_test.IntegratedRouteTests.run_stage

    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("clang")
        if not compiler:
            raise unittest.SkipTest("clang unavailable")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-continuous-")
        cls.addClassCleanup(cls.temp.cleanup)
        header = (ROOT / "robot_vuelta_integrada_continua.nxc").read_text().split("#include", 1)[0]
        stats = r'''
extern int lapPendingTurn, lapCompletedTurns;
int bFollowSamples, bPivotCompleted, bPivotPending, laterExitLogs, firstExitLogs;
'''
        sensor = r'''
    if (lapPhase == 2 && lapTurn == 2) {
        if (mode == 30) {
            if (lapSamples < 45) { return port == IN_3 ? 0 : 49; }
            return lapSamples < 230 ? 0 : 49;
        }
        if (mode == 31) { return 49; }
        if (mode == 32) { return lapSamples >= 20 ? 100 : 0; }
        if (mode == 34 || mode == 35 || mode == 36) { return 0; }
    }
    if (mode == 33 && lapPhase == 6) { return 49; }
    if (mode == 37 && lapPhase == 5 && lapTurn == 0) { return 49; }
'''
        harness = route_test.HARNESS.replace(
            "    if (mode >= 20)", sensor + "    if (mode >= 20 && mode < 30)")
        harness = harness.replace("if (mode == 0 ||", "if (mode >= 30 || mode == 0 ||")
        harness = harness.replace("    ticks++;", r'''
    ticks++;
    if (lapPhase == 2 && lapTurn == 2) {
        if (lapSamples + 1 > bFollowSamples) { bFollowSamples = lapSamples + 1; }
        if (mode == 34) { return; }
    }
''')
        harness = harness.replace("long MotorRotationCount(int port) {", r'''
long MotorRotationCount(int port) {
    if (mode == 35 && lapPhase == 2 && lapTurn == 2) { return 30000; }
''')
        harness = harness.replace("    frameFields++;", r'''
    frameFields++;
    if (lapPhase == 4 && lapTurn == 1) {
        bPivotCompleted = lapCompletedTurns;
        bPivotPending = lapPendingTurn;
    }
    if (lapPhase == 5) {
        if (lapTurn == 0) { firstExitLogs++; }
        else { laterExitLogs++; }
    }
''')
        source = Path(cls.temp.name) / "continuous.c"
        source.write_text(header + stats + harness + '\n#include "' +
                          str(ROOT / "robot_route_stages.nxc") + '"\n')
        library = Path(cls.temp.name) / "continuous.so"
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        subprocess.run([compiler, *flags, "-std=c99", "-Wall", "-Wextra", "-Werror",
                        str(source), "-o", str(library)], check=True,
                       capture_output=True, text=True)
        cls.lib = ctypes.CDLL(str(library))

    def setUp(self):
        route_test.IntegratedRouteTests.setUp(self)
        self.field("lapPendingTurn").value = -1
        for name in ("bFollowSamples", "laterExitLogs", "firstExitLogs"):
            self.field(name).value = 0
        for name in ("bPivotCompleted", "bPivotPending"):
            self.field(name).value = -99

    def run_route(self, mode):
        self.field("mode").value = mode
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("powerA"), 0)
        self.assertEqual(self.val("powerC"), 0)

    def test_outgoing_following_continues_past_old200_gate_until_next_trigger(self):
        # Hypothetical contact history; NOT a replay of114/115or proof of alignment.
        self.run_route(30)
        self.assertEqual(self.val("bFollowSamples"), 230)
        self.assertEqual(self.val("bPivotCompleted"), 1)
        self.assertEqual(self.val("bPivotPending"), 1)
        self.assertEqual(self.val("laterExitLogs"), 0)
        self.assertGreater(self.val("firstExitLogs"), 0)
        self.assertEqual(self.val("lapReason"), 100)
        self.assertEqual(self.val("lapCompletedTurns"), 18)
        self.assertEqual(self.val("lapPendingTurn"), -1)
        self.assertEqual(self.val("tones"), 2)
        self.assertEqual(self.val("frameFields") % 27, 0)
        self.assertEqual(self.val("loggingPowered"), 0)

    def test_immediate_outgoing_loss_does_not_count_B_or_try_next_pivot(self):
        self.run_route(31)
        self.assertEqual(self.val("lapReason"), 11)
        self.assertEqual(self.val("lapCompletedTurns"), 1)
        self.assertEqual(self.val("lapPendingTurn"), 1)
        self.assertEqual(self.val("lapTurn"), 2)
        self.assertEqual(self.val("lapSamples"), 0)
        self.assertEqual(self.val("tones"), 1)

    def test_unexpected_white_still_stops_pending_leg(self):
        self.run_route(32)
        self.assertEqual(self.val("lapReason"), 1)
        self.assertEqual(self.val("lapCompletedTurns"), 1)
        self.assertEqual(self.val("lapPendingTurn"), 1)

    def test_frozen_outgoing_motion_still_stops_after40_samples(self):
        self.run_route(34)
        self.assertEqual(self.val("lapReason"), 21)
        self.assertEqual(self.val("lapSamples"), 40)
        self.assertEqual(self.val("lapCompletedTurns"), 1)

    def test_outgoing_encoder_sentinel_stops_before_waiting(self):
        self.run_route(35)
        self.assertEqual(self.val("lapReason"), 8)
        self.assertEqual(self.val("lapSamples"), 0)
        self.assertEqual(self.val("lapPendingTurn"), 1)

    def test_outgoing_leg_retains2000_sample_hard_watchdog(self):
        self.run_route(36)
        self.assertEqual(self.val("lapReason"), 3)
        self.assertEqual(self.val("lapSamples"), 2000)
        self.assertEqual(self.val("lapCompletedTurns"), 1)

    def test_failed_final_marker_does_not_credit_last_pending_leg(self):
        self.run_route(33)
        self.assertEqual(self.val("lapReason"), 11)
        self.assertEqual(self.val("lapCompletedTurns"), 17)
        self.assertEqual(self.val("lapPendingTurn"), 17)
        self.assertEqual(self.val("lapCandidate"), 0)
        self.assertEqual(self.val("tones"), 1)

    def test_pending_state_cannot_skip_an_ordered_leg(self):
        self.field("lapCompletedTurns").value = 1
        self.field("lapPendingTurn").value = 3
        self.assertEqual(self.lib.RouteConfirmPending(), 0)
        self.assertEqual(self.val("lapReason"), 25)
        self.assertEqual(self.val("lapCompletedTurns"), 1)

    def test_incomplete_route_cannot_seek_final_marker(self):
        self.field("lapStarted").value = 1
        self.field("lapCompletedTurns").value = 1
        self.field("lapPendingTurn").value = 1
        self.assertEqual(self.run_stage("RouteMarker", 7, 2), 0)
        self.assertEqual(self.val("lapReason"), 25)
        self.assertEqual(self.val("lapCandidate"), 0)
        self.assertEqual(self.val("tones"), 0)

    def test_first_exit_is_not_bypassed_so_B_reference_origin_is_preserved(self):
        self.run_route(37)
        self.assertEqual(self.val("lapReason"), 11)
        self.assertEqual(self.val("lapCompletedTurns"), 0)
        self.assertEqual(self.val("lapPendingTurn"), -1)
        self.assertEqual(self.val("lapTurn"), 0)

    def test_perfect_mock_sequence_remains_a_candidate_not_physical_coverage(self):
        self.run_route(0)
        self.assertEqual(self.val("lapReason"), 100)
        self.assertEqual(self.val("lapCompletedTurns"), 18)
        self.assertEqual(self.val("lapPendingTurn"), -1)
        self.assertEqual(self.val("tones"), 2)


if __name__ == "__main__":
    unittest.main()
