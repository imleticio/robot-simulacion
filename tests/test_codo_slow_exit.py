"""Verify exit-only power configuration; not simulator validation."""
from pathlib import Path
import unittest

from test_codo_control_model import exit_model


ROOT = Path(__file__).resolve().parents[1]


class SlowExitTests(unittest.TestCase):
    def test_wrapper_scales_both_powers_equally(self):
        source = (ROOT / "robot_prueba_salida_lenta.nxc").read_text()
        self.assertIn("#define CORNER_REVISION 102", source)
        self.assertIn("#define EXIT_FORWARD_POWER 12", source)
        self.assertIn("#define EXIT_CORRECTION_POWER 9", source)
        self.assertEqual(12 / 20, 9 / 15)
        self.assertNotIn("#define MOTOR_COUNT_TARGET", source)
        self.assertNotIn("#define POSITION_COUNT_TARGET", source)
        self.assertNotIn("#define EXIT_STEPS", source)

    def test_exit_configuration_does_not_affect_approach(self):
        source = (ROOT / "robot_prueba_codo.nxc").read_text()
        approach = source.split("    if (phase == 4)", 1)[0]
        self.assertIn("OnFwd(OUT_AC, 20);", approach)
        self.assertNotIn("OnFwd(OUT_AC, EXIT_FORWARD_POWER);", approach)

    def test_scaled_model_commands_still_stop_on_loss(self):
        reason, commands = exit_model(5, [(0, 0), (49, 0), (49, 49)])
        scaled = [tuple(power * 3 // 5 for power in pair) for pair in commands]
        self.assertEqual(reason, 11)
        self.assertEqual(scaled, [(12, 12), (9, 0)])

    def test_scaled_model_does_not_enable_failed_confirmation(self):
        self.assertEqual(exit_model(6, [(0, 0)]), (6, []))
