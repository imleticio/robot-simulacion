"""Execute the actual NXC continuation with simulated C APIs, not RoboSim."""
import ctypes
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]

HARNESS = r"""
#define OUT_A 1
#define OUT_C 4
#define OUT_AC 5
#define IN_3 3
#define IN_4 4
#define BLACK_THRESHOLD 25
#define WHITE_THRESHOLD 75
#define EXIT_FORWARD_POWER 12
#define EXIT_CORRECTION_POWER 9
#define CONTROL_INTERVAL_MS 20
int testMode, ticks, powerA, powerC, commands;
long rawA, rawC;
void Off(int ports) {
    if (ports & OUT_A) { powerA = 0; rawA = 0; }
    if (ports & OUT_C) { powerC = 0; rawC = 0; }
}
void OnFwd(int ports, int power) {
    commands++;
    if (ports & OUT_A) { powerA = power; rawA = 0; }
    if (ports & OUT_C) { powerC = power; rawC = 0; }
}
void Wait(int interval) {
    (void)interval;
    ticks++;
    if (testMode == 8) { return; }
    rawA += powerA / 4;
    rawC += powerC / 4;
    if (testMode == 11) { rawA = -3; }
    if (testMode == 12) { rawA = 0; }
}
long MotorRotationCount(int port) {
    if (testMode == 9) { return 30000; }
    if (testMode == 10 && ticks > 0) { return 30000; }
    return port == OUT_A ? rawA : rawC;
}
int Sensor(int port) {
    if (testMode == 15) { return port == IN_3 ? 49 : 0; }
    if (testMode == 16) { return 49; }
    if (testMode == 17) { return 100; }
    if (ticks >= 5) {
        if (testMode == 1) { return 49; }
        if (testMode == 2) { return 100; }
        if (testMode == 3) { return port == IN_3 ? 0 : 49; }
        if (testMode == 4) { return port == IN_3 ? 49 : 0; }
    }
    if (ticks >= 60) {
        if (testMode == 5) { return 49; }
        if (testMode == 6) { return 100; }
        if (testMode == 7) { return port == IN_3 ? 0 : 49; }
    }
    if (ticks >= 5 && ticks < 10) {
        if (testMode == 13) { return port == IN_3 ? 0 : 49; }
        if (testMode == 14) { return port == IN_3 ? 49 : 0; }
    }
    return 0;
}
"""


class ContinuationStageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.compiler = shutil.which("clang")
        if cls.compiler is None:
            raise unittest.SkipTest("clang unavailable; NBC compilation is separate")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-continuation-")
        cls.addClassCleanup(cls.temp.cleanup)
        source = Path(cls.temp.name) / "continuation.c"
        source.write_text(HARNESS + '\n#include "' +
                          str(ROOT / "robot_continuation_stage.nxc") + '"\n')
        library = Path(cls.temp.name) / "continuation.so"
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        subprocess.run([cls.compiler, *flags, "-Wall", "-Wextra", "-Werror",
                        "-std=c99", str(source), "-o", str(library)],
                       check=True, capture_output=True, text=True)
        cls.lib = ctypes.CDLL(str(library))
        cls.lib.RunContinuationStage.argtypes = []
        cls.lib.RunContinuationStage.restype = ctypes.c_int

    def field(self, name, kind=ctypes.c_int):
        return kind.in_dll(self.lib, name)

    def setUp(self):
        for name in ("testMode", "ticks", "powerA", "powerC", "commands",
                     "continueSamples", "continueBothSamples", "continueLeftSamples",
                     "continueRightSamples", "continueEncoderStatus"):
            self.field(name).value = 0
        for name in ("rawA", "rawC", "continueTotalA", "continueTotalC"):
            self.field(name, ctypes.c_long).value = 0
        for name in ("continueStartA", "continueStartC", "continueCurrentA", "continueCurrentC"):
            self.field(name, ctypes.c_long).value = 30000
        for name in ("continueEntryLeft", "continueEntryRight", "continueFinalLeft", "continueFinalRight"):
            self.field(name).value = 30000

    def run_case(self, mode):
        self.field("testMode").value = mode
        reason = self.lib.RunContinuationStage()
        self.assertEqual(self.field("powerA").value, 0)
        self.assertEqual(self.field("powerC").value, 0)
        return reason

    def test_black_straight_stops_at_first_sampled_track_reference(self):
        self.assertEqual(self.run_case(0), 17)
        self.assertEqual(self.field("continueSamples").value, 60)
        self.assertEqual(self.field("continueTotalA", ctypes.c_long).value, 180)
        self.assertEqual(self.field("continueTotalC", ctypes.c_long).value, 180)

    def test_lost_black_stops_before_another_command(self):
        self.assertEqual(self.run_case(1), 11)
        self.assertEqual(self.field("continueSamples").value, 5)
        self.assertEqual(self.field("commands").value, 5)

    def test_white_stops_before_another_command(self):
        self.assertEqual(self.run_case(2), 1)
        self.assertEqual(self.field("commands").value, 5)

    def test_persistent_left_correction_hits_difference_guard(self):
        self.assertEqual(self.run_case(3), 19)
        self.assertEqual(self.field("continueSamples").value, 35)
        self.assertEqual(self.field("continueTotalA", ctypes.c_long).value, 75)
        self.assertEqual(self.field("continueTotalC", ctypes.c_long).value, 15)

    def test_persistent_right_correction_hits_symmetric_guard(self):
        self.assertEqual(self.run_case(4), 19)
        self.assertEqual(self.field("continueTotalA", ctypes.c_long).value, 15)
        self.assertEqual(self.field("continueTotalC", ctypes.c_long).value, 75)

    def test_final_sample_can_override_segment_endpoint_on_loss(self):
        self.assertEqual(self.run_case(5), 11)

    def test_final_sample_can_override_segment_endpoint_on_white(self):
        self.assertEqual(self.run_case(6), 1)

    def test_final_one_sided_contact_is_inconclusive(self):
        self.assertEqual(self.run_case(7), 20)

    def test_zero_motion_hits_watchdog_not_success(self):
        self.assertEqual(self.run_case(8), 18)
        self.assertEqual(self.field("continueSamples").value, 120)

    def test_sentinel_baseline_stops_without_waiting(self):
        self.assertEqual(self.run_case(9), 8)
        self.assertEqual(self.field("ticks").value, 0)
        self.assertEqual(self.field("continueEncoderStatus").value, 2)

    def test_sentinel_after_wait_stops_without_accumulating(self):
        self.assertEqual(self.run_case(10), 8)
        self.assertEqual(self.field("continueTotalA", ctypes.c_long).value, 0)

    def test_negative_delta_is_a_fault_not_progress(self):
        self.assertEqual(self.run_case(11), 7)
        self.assertEqual(self.field("continueEncoderStatus").value, 3)

    def test_single_stalled_track_cannot_pass(self):
        self.assertEqual(self.run_case(12), 19)

    def test_brief_left_correction_can_return_to_forward_motion(self):
        self.assertEqual(self.run_case(13), 17)
        self.assertEqual(self.field("continueLeftSamples").value, 5)
        self.assertGreater(self.field("continueTotalC", ctypes.c_long).value, 120)

    def test_brief_right_correction_can_return_to_forward_motion(self):
        self.assertEqual(self.run_case(14), 17)
        self.assertEqual(self.field("continueRightSamples").value, 5)

    def test_nonblack_entry_cannot_restart_motion(self):
        for mode, reason in [(15, 20), (16, 11), (17, 1)]:
            self.setUp()
            self.assertEqual(self.run_case(mode), reason)
            self.assertEqual(self.field("commands").value, 0)

    def test_106_preprocessing_preserves_105_and_gates_phase5(self):
        def preprocess(name):
            return subprocess.check_output(
                [self.compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_salida_controlada.nxc")
        new = preprocess("robot_prueba_continuacion.nxc")
        self.assertEqual(old.count("SetInput("), 50)
        self.assertEqual(new.count("SetInput("), 68)
        self.assertNotIn("RunContinuationStage", old)
        self.assertIn("SetInput(IN_1, ScaledValue, 106);", new)
        gate = new.split("    if (stopReason == 16)\n    {\n        phase = 5;", 1)
        self.assertEqual(len(gate), 2)
        self.assertIn("stopReason = RunContinuationStage();", gate[1])
        self.assertNotIn("PlayTone(", new)
        self.assertNotIn("OnRev(", new)
        self.assertNotIn("&&", new)
        self.assertNotIn("||", new)
        self.assertNotIn("robot_marker_tracker", new)
