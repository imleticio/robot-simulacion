"""Check the isolated positioning experiment; not simulator geometry proof."""
import math
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


class NoPositionCornerTests(unittest.TestCase):
    def test_wrapper_omits_positioning_and_stops_before_exit(self):
        source = (ROOT / "robot_prueba_codo_sin_avance.nxc").read_text()
        defines = [line for line in source.splitlines() if line.startswith("#define")]
        self.assertEqual(defines, [
            "#define CORNER_REVISION 107",
            "#define POSITION_COUNT_TARGET 0",
            "#define CORNER_STOP_AFTER_CONFIRMATION 1",
        ])

    def test_default_positioning_remains_60(self):
        source = (ROOT / "robot_prueba_codo.nxc").read_text()
        self.assertIn("#ifndef POSITION_COUNT_TARGET\n#define POSITION_COUNT_TARGET 60\n#endif", source)

    def test_approach_offset_is_lateral_relative_to_ideal_quarter_turn_exit(self):
        # An approach-axis translation persists after changing heading; after
        # an ideal right angle it is perpendicular to the exit direction.
        # This is geometry, NOT a reconstruction of the current sensor pose.
        offset = 60 * 0.4 * math.pi / 360
        exit_axis = (math.cos(math.pi / 2), math.sin(math.pi / 2))
        parallel = offset * exit_axis[0]
        lateral_magnitude = offset * exit_axis[1]
        self.assertAlmostEqual(parallel, 0)
        self.assertAlmostEqual(lateral_magnitude, 0.2094395102)

    def test_preprocessed_program_has_no_position_command_or_exit_restart(self):
        compiler = shutil.which("clang")
        if not compiler:
            self.skipTest("clang unavailable; NBC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        new = preprocess("robot_prueba_codo_sin_avance.nxc")
        old = preprocess("robot_prueba_pose_codo.nxc")
        self.assertEqual(new.count("SetInput("), 39)
        self.assertIn("SetInput(IN_1, ScaledValue, 107);", new)
        self.assertIn("SetInput(IN_1, ScaledValue, 0);", new)
        position, pivot = new.split("    if (phase == 4)", 1)[1].split("    if (phase == 1)", 1)
        self.assertIn("phase = 1;", position)
        self.assertNotIn("OnFwd(", position)
        self.assertNotIn("MotorRotationCount(", position)
        self.assertIn("OnFwd(OUT_C, 15);", pivot)
        self.assertIn("deltaC >= 743", pivot)
        self.assertIn("turnStep < 240", pivot)
        self.assertIn("if (1 == 1)", pivot)
        self.assertIn("stopReason = 14;", pivot)
        self.assertNotIn("RunContinuationStage", new)
        # After the positioning block, all pivot/contact/exit code must be
        # identical to101, apart from the diagnostic revision value.
        old_pivot = old.split("    if (phase == 1)", 1)[1]
        self.assertEqual(pivot.replace("ScaledValue, 107", "ScaledValue, (100 + 1)")
                         .replace("ScaledValue, 0);\n    SetInput(IN_1, ScaledValue, 30)",
                                  "ScaledValue, 60);\n    SetInput(IN_1, ScaledValue, 30)"),
                         old_pivot)
