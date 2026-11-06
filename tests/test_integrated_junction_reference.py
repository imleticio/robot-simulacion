"""114changes one provisional B reference; this is NOT map/physics validation."""
import ctypes
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest

import test_integrated_route as route_test

ROOT = route_test.ROOT


class IntegratedJunctionReferenceTests(unittest.TestCase):
    field = route_test.IntegratedRouteTests.field
    val = route_test.IntegratedRouteTests.val
    setUp = route_test.IntegratedRouteTests.setUp
    run_stage = route_test.IntegratedRouteTests.run_stage

    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("clang")
        if not compiler:
            raise unittest.SkipTest("clang unavailable")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-junction-")
        cls.addClassCleanup(cls.temp.cleanup)
        harness = route_test.HARNESS.replace(
            "    if (mode >= 20)",
            "    if (mode == 27 && lapSamples >= 152) { return 49; }\n"
            "    if (mode == 28 && lapSamples >= 30) { return 49; }\n"
            "    if (mode >= 20)")
        cls.libraries = {}
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        for revision, reference in ((113, 1200), (114, 370)):
            source = Path(cls.temp.name) / f"junction{revision}.c"
            source.write_text(f"#define ROUTE_REVISION {revision}\n"
                              "#define ROUTE_BASELINE_APPROACH 1\n"
                              f"#define ROUTE_FIRST_B_REFERENCE {reference}\n" +
                              harness + '\n#include "' +
                              str(ROOT / "robot_route_stages.nxc") + '"\n')
            library = Path(cls.temp.name) / f"junction{revision}.so"
            subprocess.run([compiler, *flags, "-std=c99", "-Wall", "-Wextra",
                            "-Werror", str(source), "-o", str(library)], check=True,
                           capture_output=True, text=True)
            cls.libraries[revision] = ctypes.CDLL(str(library))
        cls.lib = cls.libraries[114]

    def tearDown(self):
        self.lib = self.libraries[114]

    def prepare_B(self):
        self.field("lapTurn").value = 1
        self.field("lapCompletedTurns").value = 1
        self.lib.ConfigureRouteTurn(1)

    def test_old_reference_misses_mock_leg_but_new_candidate_is_reached(self):
        # Hypothetical constant-black approach followed by loss at760counts;
        # NOT a replay of the real contact history and NOT proof B is at370.
        self.lib = self.libraries[113]
        self.setUp()
        self.prepare_B()
        self.assertEqual(self.run_stage("RouteFollow", 27), 0)
        self.assertEqual(self.val("lapReason"), 11)
        self.lib = self.libraries[114]
        self.setUp()
        self.prepare_B()
        self.assertEqual(self.run_stage("RouteFollow", 27), 1)
        self.assertEqual(self.val("routeReference", ctypes.c_long), 370)
        self.assertEqual(self.val("lapSamples"), 74)

    def test_early_line_loss_still_stops_without_wrong_corner_fallback(self):
        self.prepare_B()
        self.assertEqual(self.run_stage("RouteFollow", 28), 0)
        self.assertEqual(self.val("lapReason"), 11)
        self.assertEqual(self.val("lapCompletedTurns"), 1)
        self.assertEqual(self.val("lapPivotA", ctypes.c_long), 0)
        self.assertEqual(self.val("lapPivotC", ctypes.c_long), 0)

    def test_return_reference_and_turn_sequence_unchanged(self):
        for turn in range(18):
            values = []
            for revision in (113, 114):
                lib = self.libraries[revision]
                lib.ConfigureRouteTurn(turn)
                values.append((ctypes.c_int.in_dll(lib, "routeDirection").value,
                               ctypes.c_int.in_dll(lib, "routeTrigger").value,
                               ctypes.c_long.in_dll(lib, "routeReference").value))
            if turn == 1:
                self.assertEqual(values, [(1, 1, 1200), (1, 1, 370)])
            else:
                self.assertEqual(values[0], values[1])

    def test_full_mock_sequence_and_two_marker_sounds_remain(self):
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 100)
        self.assertEqual(self.val("lapCompletedTurns"), 18)
        self.assertEqual(self.val("tones"), 2)
        self.assertEqual(self.val("frameFields") % 26, 0)
        self.assertEqual(self.val("loggingPowered"), 0)

    def test_entry_differs_only_in_revision_reference_and_explanatory_comments(self):
        def body(filename):
            text = (ROOT / filename).read_text()
            return [line.strip() for line in text.splitlines()
                    if line.strip() and not line.lstrip().startswith("//")
                    and not line.startswith("#define ROUTE_REVISION")
                    and not line.startswith("#define ROUTE_FIRST_B_REFERENCE")]
        self.assertEqual(body("robot_vuelta_integrada_aproximacion.nxc"),
                         body("robot_vuelta_integrada_cruce.nxc"))


if __name__ == "__main__":
    unittest.main()
