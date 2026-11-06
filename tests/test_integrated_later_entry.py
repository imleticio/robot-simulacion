"""115is one position hypothesis, not a physics-based alignment fix."""
import ctypes
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest

import test_integrated_route as route_test

ROOT = route_test.ROOT


class IntegratedLaterEntryTests(unittest.TestCase):
    field = route_test.IntegratedRouteTests.field
    val = route_test.IntegratedRouteTests.val
    setUp = route_test.IntegratedRouteTests.setUp
    run_stage = route_test.IntegratedRouteTests.run_stage

    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("clang")
        if not compiler:
            raise unittest.SkipTest("clang unavailable")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-later-entry-")
        cls.addClassCleanup(cls.temp.cleanup)
        header = (ROOT / "robot_vuelta_integrada_cruce_tardio.nxc").read_text().split("#include", 1)[0]
        source = Path(cls.temp.name) / "later.c"
        source.write_text(header + route_test.HARNESS + '\n#include "' +
                          str(ROOT / "robot_route_stages.nxc") + '"\n')
        library = Path(cls.temp.name) / "later.so"
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        subprocess.run([compiler, *flags, "-std=c99", "-Wall", "-Wextra", "-Werror",
                        str(source), "-o", str(library)], check=True,
                       capture_output=True, text=True)
        cls.lib = ctypes.CDLL(str(library))

    def test_actual_entry_header_uses450_without_changing_return_reference(self):
        self.field("lapTurn").value = 1
        self.lib.ConfigureRouteTurn(1)
        self.assertEqual(self.run_stage("RouteFollow"), 1)
        self.assertEqual(self.val("routeReference", ctypes.c_long), 450)
        self.assertEqual(self.val("lapSamples"), 90)
        self.lib.ConfigureRouteTurn(7)
        self.assertEqual(self.val("routeReference", ctypes.c_long), 450)

    def test_first_and_second_pivot_target_not_increased(self):
        for turn, a, c in ((0, 744, 0), (1, 0, 744)):
            with self.subTest(turn=turn):
                self.setUp()
                self.lib.ConfigureRouteTurn(turn)
                self.assertEqual(self.run_stage("RoutePivot"), 1)
                self.assertEqual(self.val("lapPivotA", ctypes.c_long), a)
                self.assertEqual(self.val("lapPivotC", ctypes.c_long), c)
                self.assertEqual(self.val("lapSamples"), 248)

    def test_one_sided_exit_still_fails_instead_of_extending_watchdog(self):
        self.assertEqual(self.run_stage("RouteExit", 10), 0)
        self.assertEqual(self.val("lapReason"), 15)
        self.assertEqual(self.val("lapSamples"), 200)

    def test_full_mock_control_flow_still_requires_all_turns_before_finish(self):
        self.lib.RunRouteAttempt()
        self.assertEqual(self.val("lapReason"), 100)
        self.assertEqual(self.val("lapCompletedTurns"), 18)
        self.assertEqual(self.val("tones"), 2)
        self.assertEqual(self.val("loggingPowered"), 0)

    def test_only_revision_and_first_reference_changed_relative_to114(self):
        def body(filename):
            return [line.strip() for line in (ROOT / filename).read_text().splitlines()
                    if line.strip() and not line.lstrip().startswith("//")
                    and not line.startswith("#define ROUTE_REVISION")
                    and not line.startswith("#define ROUTE_FIRST_B_REFERENCE")]
        self.assertEqual(body("robot_vuelta_integrada_cruce.nxc"),
                         body("robot_vuelta_integrada_cruce_tardio.nxc"))


if __name__ == "__main__":
    unittest.main()
