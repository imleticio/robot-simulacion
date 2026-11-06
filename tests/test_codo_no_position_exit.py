"""Regression checks for108geometry with unchanged105exit, not runtime proof."""
from pathlib import Path
import shutil
import subprocess
import unittest

from test_codo_control_model import turn_model
from test_codo_controlled_exit import controlled_exit


ROOT = Path(__file__).resolve().parents[1]


class NoPositionExitTests(unittest.TestCase):
    def test_wrapper_only_changes_revision_and_position_from105(self):
        def defines(name):
            source = (ROOT / name).read_text()
            return dict(line.split()[1:3] for line in source.splitlines()
                        if line.startswith("#define"))
        old = defines("robot_prueba_salida_controlada.nxc")
        new = defines("robot_prueba_codo_salida_sin_avance.nxc")
        old.update(CORNER_REVISION="108", POSITION_COUNT_TARGET="0")
        self.assertEqual(new, old)

    def test_preprocessed_pivot_and_exit_match105_except_telemetry(self):
        compiler = shutil.which("clang")
        if not compiler:
            self.skipTest("clang unavailable; NBC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_salida_controlada.nxc")
        new = preprocess("robot_prueba_codo_salida_sin_avance.nxc")
        self.assertEqual(new.count("SetInput("), 50)
        self.assertIn("SetInput(IN_1, ScaledValue, 108);", new)
        position, pivot = new.split("    if (phase == 4)", 1)[1].split(
            "    if (phase == 1)", 1)
        self.assertNotIn("OnFwd(", position)
        self.assertIn("phase = 1;", position)
        self.assertNotIn("RunContinuationStage", new)
        normalized = pivot.replace("ScaledValue, 108", "ScaledValue, 105").replace(
            "ScaledValue, 0);\n    SetInput(IN_1, ScaledValue, 30)",
            "ScaledValue, 60);\n    SetInput(IN_1, ScaledValue, 30)")
        self.assertEqual(normalized, old.split("    if (phase == 1)", 1)[1])
        self.assertIn("if (0 == 1)", pivot)  # observation-only flag is disabled

    def test_observed_incomplete107pivot_cannot_enable_exit(self):
        reason, _, _ = turn_model([(0, 193, 0, 49)] * 240, [])
        self.assertEqual(reason, 4)
        self.assertNotEqual(reason, 5)

    def test_same_exit_criterion_still_rejects_one_sided_rotation(self):
        self.assertEqual(controlled_exit([(49, 0, 0, 2)] * 200, final=(49, 0)),
                         (15, 200))
