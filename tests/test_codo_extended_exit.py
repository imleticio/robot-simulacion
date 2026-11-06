"""Structural checks for the extended observation, not NXC runtime tests."""
from pathlib import Path
import unittest
from unittest.mock import patch

from test_codo_control_model import exit_model


ROOT = Path(__file__).resolve().parents[1]


class ExtendedExitTests(unittest.TestCase):
    def test_wrapper_changes_only_revision_and_bound_from_slow_exit(self):
        source = (ROOT / "robot_prueba_salida_extendida.nxc").read_text()
        defines = [line for line in source.splitlines() if line.startswith("#define")]
        self.assertEqual(defines, [
            "#define CORNER_REVISION 103",
            "#define EXIT_STEPS 100",
            "#define EXIT_FORWARD_POWER 12",
            "#define EXIT_CORRECTION_POWER 9",
        ])
        self.assertIn('#include "robot_prueba_codo.nxc"', source)

    def test_shared_source_retains_default_bound_and_logs_selected_bound(self):
        source = (ROOT / "robot_prueba_codo.nxc").read_text()
        self.assertIn("#ifndef EXIT_STEPS\n#define EXIT_STEPS 50\n#endif", source)
        self.assertIn("SetInput(IN_1, ScaledValue, EXIT_STEPS);", source)

    def test_loss_after_old_cap_still_stops_without_second_turn(self):
        with patch("test_codo_control_model.EXIT_LIMIT", 100):
            reason, commands = exit_model(5, [(0, 0)] * 55 + [(49, 49)])
        self.assertEqual(reason, 11)
        self.assertEqual(len(commands), 55)

    def test_new_cap_requires_final_contact_check(self):
        with patch("test_codo_control_model.EXIT_LIMIT", 100):
            reason, commands = exit_model(5, [(0, 0)] * 100, final_reading=(49, 49))
        self.assertEqual(reason, 11)
        self.assertEqual(len(commands), 100)
