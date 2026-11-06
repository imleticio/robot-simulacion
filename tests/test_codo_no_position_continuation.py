"""Verify109composes existing108geometry and106continuation without retuning."""
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class NoPositionContinuationTests(unittest.TestCase):
    def test_wrapper_adds_only_existing_continuation_to108(self):
        def defines(name):
            return dict(line.split()[1:3] for line in (ROOT / name).read_text().splitlines()
                        if line.startswith("#define"))
        expected = defines("robot_prueba_codo_salida_sin_avance.nxc")
        expected.update(CORNER_REVISION="109", ENABLE_CONTINUATION="1")
        self.assertEqual(defines("robot_prueba_codo_continuo_sin_avance.nxc"), expected)

    def test_preprocessing_retains106postposition_code_and_zero_positioning(self):
        compiler = shutil.which("clang")
        if not compiler:
            self.skipTest("clang unavailable; NBC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_continuacion.nxc")
        new = preprocess("robot_prueba_codo_continuo_sin_avance.nxc")
        self.assertEqual(new.count("SetInput("), 68)
        self.assertIn("SetInput(IN_1, ScaledValue, 109);", new)
        position, remainder = new.split("    if (phase == 4)", 1)[1].split(
            "    if (phase == 1)", 1)
        self.assertNotIn("OnFwd(", position)
        self.assertNotIn("Wait(", position)
        normalized = remainder.replace("ScaledValue, 109", "ScaledValue, 106").replace(
            "ScaledValue, 0);\n    SetInput(IN_1, ScaledValue, 30)",
            "ScaledValue, 60);\n    SetInput(IN_1, ScaledValue, 30)")
        self.assertEqual(normalized, old.split("    if (phase == 1)", 1)[1])
        self.assertIn("    if (stopReason == 16)\n    {\n        phase = 5;", new)
        for forbidden in ("OnRev(", "PlayTone(", "&&", "||", "robot_marker_tracker"):
            self.assertNotIn(forbidden, new)
