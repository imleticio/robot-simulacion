"""Structural guards for the observation-only build, not NXC runtime tests."""
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class CornerPoseTests(unittest.TestCase):
    def test_observation_wrapper_has_no_motion_commands(self):
        source = (ROOT / "robot_prueba_pose_codo.nxc").read_text()
        self.assertIn("#define CORNER_STOP_AFTER_CONFIRMATION 1", source)
        self.assertIn('#include "robot_prueba_codo.nxc"', source)
        self.assertNotIn("OnFwd(", source)

    def test_observation_gate_precedes_exit_and_preserves_failures(self):
        source = (ROOT / "robot_prueba_codo.nxc").read_text()
        gate = source.index("    if (CORNER_STOP_AFTER_CONFIRMATION == 1)")
        exit_gate = source.index("    if (stopReason == 5)", gate + 100)
        section = source[gate:exit_gate]
        self.assertIn("if (stopReason == 5)", section)
        self.assertIn("stopReason = 14;", section)
        self.assertNotIn("OnFwd(", section)
        self.assertNotIn("phase =", section)
        self.assertIn("#define CORNER_STOP_AFTER_CONFIRMATION 0", source)
