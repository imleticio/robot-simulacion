"""Sampled interval accounting checks; not NXC runtime or total odometry."""
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


def accumulate(intervals):
    totals = [0, 0]
    valid = 0
    status = 0
    for start_a, start_c, current_a, current_c in intervals:
        if 30000 in (start_a, start_c, current_a, current_c):
            return 8, valid, tuple(totals), 2
        delta = (current_a - start_a, current_c - start_c)
        if min(delta) < 0:
            return 7, valid, tuple(totals), 3
        totals = [totals[i] + delta[i] for i in range(2)]
        valid += 1
        status = 1
    return 10, valid, tuple(totals), status


class ExitMeasurementTests(unittest.TestCase):
    def test_reset_each_command_does_not_erase_accumulated_intervals(self):
        self.assertEqual(accumulate([(0, 0, 3, 3), (0, 0, 4, 4)]),
                         (10, 2, (7, 7), 1))

    def test_nonzero_baselines_use_deltas_not_absolute_counts(self):
        self.assertEqual(accumulate([(40, 80, 43, 84)]), (10, 1, (3, 4), 1))

    def test_left_only_correction_can_report_braked_c(self):
        self.assertEqual(accumulate([(0, 0, 2, 0)]), (10, 1, (2, 0), 1))

    def test_right_only_correction_can_report_braked_a(self):
        self.assertEqual(accumulate([(0, 0, 0, 2)]), (10, 1, (0, 2), 1))

    def test_zero_is_reported_not_called_travel(self):
        self.assertEqual(accumulate([(0, 0, 0, 0)]), (10, 1, (0, 0), 1))

    def test_no_exit_has_no_measurement(self):
        self.assertEqual(accumulate([]), (10, 0, (0, 0), 0))

    def test_any_sentinel_aborts_without_adding_failed_interval(self):
        for index in range(4):
            sample = [0, 0, 3, 3]
            sample[index] = 30000
            with self.subTest(index=index):
                self.assertEqual(accumulate([(0, 0, 2, 2), sample]),
                                 (8, 1, (2, 2), 2))

    def test_negative_delta_on_either_motor_aborts(self):
        for sample in [(4, 0, 3, 1), (0, 4, 1, 3)]:
            self.assertEqual(accumulate([sample]), (7, 0, (0, 0), 3))

    def test_snapshot_order_is_inside_command_reset_boundaries(self):
        source = (ROOT / "robot_prueba_codo.nxc").read_text()
        loop = source.split("for (exitStep =", 1)[1].split(
            "        Off(OUT_AC);\n        // Check again", 1)[0]
        baseline = loop.index("exitStartA = MotorRotationCount")
        wait = loop.index("Wait(CONTROL_INTERVAL_MS);", baseline)
        current = loop.index("exitCurrentA = MotorRotationCount", wait)
        self.assertLess(loop.rindex("OnFwd("), baseline)
        self.assertLess(baseline, wait)
        self.assertLess(wait, current)
        self.assertNotIn("Off(", loop[baseline:])
        self.assertNotIn("OnFwd(", loop[baseline:])

    def test_preprocessed_frames_and_motion_commands(self):
        compiler = shutil.which("clang")
        if compiler is None:
            self.skipTest("clang preprocessor is unavailable; NXC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_salida_extendida.nxc")
        measured = preprocess("robot_prueba_salida_medida.nxc")
        self.assertEqual(old.count("SetInput("), 39)
        self.assertEqual(measured.count("SetInput("), 47)
        self.assertIn("SetInput(IN_1, ScaledValue, 104);", measured)
        self.assertIn("exitStep < 100", measured)
        for command in ("OnFwd(", "Off(", "OnRev(", "Wait("):
            self.assertEqual(old.count(command), measured.count(command))
        self.assertNotIn("exitMeasuredSamples", old)
