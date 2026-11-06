"""37,113 regression: long approach is not the short continuation diagnostic.

The sensor pattern below is hypothetical, not a reconstruction of the observed
243samples. Actual112telemetry proves a62-count stop before any pivot, but does
not record the per-sample contact history.
"""
import ctypes
from pathlib import Path
import platform
import re
import shutil
import subprocess
import tempfile
import unittest

import test_integrated_route as route_test

HARNESS = route_test.HARNESS
ROOT = route_test.ROOT


class IntegratedApproachTests(unittest.TestCase):
    field = route_test.IntegratedRouteTests.field
    val = route_test.IntegratedRouteTests.val
    setUp = route_test.IntegratedRouteTests.setUp
    run_stage = route_test.IntegratedRouteTests.run_stage

    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("clang")
        if not cls.compiler:
            raise unittest.SkipTest("clang unavailable")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-approach-")
        cls.addClassCleanup(cls.temp.cleanup)
        pattern = r'''
    if (mode == 23 || mode == 24 || mode == 25 || mode == 26) {
        if (lapSamples >= 243) {
            if (mode == 25) { return 100; }
            if (mode == 26) {
                if (lapSamples < 246) { return port == IN_3 ? 100 : 50; }
                return port == IN_3 ? 0 : 50;
            }
            return 49;
        }
        if (lapSamples >= 212) {
            if (mode == 24) { return port == IN_3 ? 50 : 0; }
            return port == IN_3 ? 0 : 50;
        }
        return 0;
    }
'''
        harness = HARNESS.replace("    if (mode >= 20)", pattern + "    if (mode >= 20)")
        cls.libraries = {}
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        for feature, revision in ((0, 112), (1, 113)):
            source = Path(cls.temp.name) / f"approach{revision}.c"
            source.write_text(f"#define ROUTE_REVISION {revision}\n"
                              f"#define ROUTE_BASELINE_APPROACH {feature}\n" +
                              harness + '\n#include "' +
                              str(ROOT / "robot_route_stages.nxc") + '"\n')
            library = Path(cls.temp.name) / f"approach{revision}.so"
            subprocess.run([cls.compiler, *flags, "-std=c99", "-Wall", "-Wextra",
                            "-Werror", str(source), "-o", str(library)], check=True,
                           capture_output=True, text=True)
            cls.libraries[revision] = ctypes.CDLL(str(library))
        cls.lib = cls.libraries[113]

    def tearDown(self):
        self.lib = self.libraries[113]

    def test_legacy_short_limit_blocks_hypothetical_approach_but_113_reaches_edge(self):
        for mode in (23, 24):
            with self.subTest(direction=mode):
                self.lib = self.libraries[112]
                self.setUp()
                self.assertEqual(self.run_stage("RouteFollow", mode), 0)
                self.assertEqual(self.val("lapReason"), 19)
                self.assertGreaterEqual(abs(self.val("lapTotalA", ctypes.c_long) -
                                            self.val("lapTotalC", ctypes.c_long)), 60)
                self.lib = self.libraries[113]
                self.setUp()
                self.assertEqual(self.run_stage("RouteFollow", mode), 1)
                self.assertEqual(self.val("lapReason"), 0)
                self.assertEqual(self.val("lapSamples"), 243)
                self.assertEqual(self.val("lapPivotA", ctypes.c_long), 0)
                self.assertEqual(self.val("lapPivotC", ctypes.c_long), 0)

    def test_approach_commands_match_111_not_exit_braking(self):
        self.field("mode").value = 20
        for state, a, c in ((3, 20, 20), (1, 25, 10), (2, 10, 25)):
            with self.subTest(state=state):
                self.assertEqual(self.lib.RouteIntervalMode(state, 1), 1)
                self.assertEqual(self.val("powerA"), a)
                self.assertEqual(self.val("powerC"), c)
                self.lib.Off(5)

    def test_first_approach_watchdog_is_reduced_to_111_400_samples(self):
        self.assertEqual(self.run_stage("RouteFollow"), 0)
        self.assertEqual(self.val("lapReason"), 3)
        self.assertEqual(self.val("lapSamples"), 400)

    def test_later_leg_watchdog_is_not_extended(self):
        self.field("lapTurn").value = 16
        self.assertEqual(self.run_stage("RouteFollow"), 0)
        self.assertEqual(self.val("lapReason"), 3)
        self.assertEqual(self.val("lapSamples"), 2000)

    def test_marker_still_has_original_short_difference_guard(self):
        self.assertEqual(self.run_stage("RouteMarker", 10, 1), 0)
        self.assertEqual(self.val("lapReason"), 19)
        self.assertEqual(self.val("lapSamples"), 30)

    def test_pre_white_approach_steering_is_not_charged_to_crossing_budget(self):
        self.assertEqual(self.run_stage("RouteMarker", 25, 0), 1)
        self.assertEqual(self.val("lapMarkerEntered"), 1)
        self.assertEqual(self.val("lapMarkerDifferenceBase", ctypes.c_long), 124)
        self.assertEqual(self.val("lapStarted"), 1)
        self.assertEqual(self.val("tones"), 1)

    def test_white_contact_latches_a_new_bounded_difference_budget(self):
        self.assertEqual(self.run_stage("RouteMarker", 26, 0), 0)
        self.assertEqual(self.val("lapReason"), 19)
        self.assertEqual(self.val("lapMarkerEntered"), 1)
        self.assertEqual(self.val("lapTotalA", ctypes.c_long) -
                         self.val("lapTotalC", ctypes.c_long) -
                         self.val("lapMarkerDifferenceBase", ctypes.c_long), 60)
        self.assertEqual(self.val("lapStarted"), 0)
        self.assertEqual(self.val("tones"), 0)

    def test_pre_white_line_loss_still_aborts_without_start_or_sound(self):
        self.assertEqual(self.run_stage("RouteMarker", 23, 0), 0)
        self.assertEqual(self.val("lapReason"), 11)
        self.assertEqual(self.val("lapMarkerEntered"), 0)
        self.assertEqual(self.val("lapStarted"), 0)
        self.assertEqual(self.val("tones"), 0)

    def test_approach_faults_still_stop(self):
        for mode, reason in ((1, 21), (2, 8), (3, 8), (6, 26), (7, 1),
                             (8, 7), (11, 11)):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_stage("RouteFollow", mode), 0)
                self.assertEqual(self.val("lapReason"), reason)
                self.assertEqual(self.val("lapPivotA", ctypes.c_long), 0)

    def test_reference_counts_unchanged_while_elapsed_samples_can_change(self):
        self.field("lapTurn").value = 1
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RouteFollow"), 1)
        self.assertEqual(self.val("routeReference", ctypes.c_long), 1200)
        self.assertEqual(self.val("lapSamples"), 240)

    def test_full_mock_integrated_control_flow_still_reaches_candidate_endpoint(self):
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 100)
        self.assertEqual(self.val("lapCompletedTurns"), 18)
        self.assertEqual(self.val("tones"), 2)
        self.assertEqual(self.val("loggingPowered"), 0)
        self.assertEqual(self.val("frameFields") % 26, 0)

    def test_pivot_exit_and_route_plan_not_changed_by_113_flag(self):
        outputs = {}
        source = ROOT / "robot_route_stages.nxc"
        for feature in (0, 1):
            outputs[feature] = subprocess.run(
                [self.compiler, "-E", "-P", "-x", "c",
                 f"-DROUTE_BASELINE_APPROACH={feature}", str(source)],
                check=True, capture_output=True, text=True).stdout

        def function(text, name):
            match = re.search(r"(?:int|void)\s+" + name + r"\([^)]*\)\s*\{", text)
            self.assertIsNotNone(match, name)
            start = match.start()
            depth = 1
            cursor = match.end()
            while depth:
                depth += (text[cursor] == "{") - (text[cursor] == "}")
                cursor += 1
            return text[start:cursor]

        for name in ("RoutePivot", "RouteExit", "ConfigureRouteTurn"):
            with self.subTest(function=name):
                self.assertEqual(function(outputs[0], name), function(outputs[1], name))


if __name__ == "__main__":
    unittest.main()
