"""Execute the standalone reactive NXC source as C, not simulator physics."""
import ctypes
from pathlib import Path
import platform
import re
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HARNESS = r'''
#define task void
#define main ReactiveTaskNotExecutedByTests
#define true 1
#define OUT_A 1
#define OUT_C 4
#define OUT_AC 5
#define IN_1 1
#define IN_2 2
#define IN_3 3
#define IN_4 4
#define CONTROL_1 IN_3
#define CONTROL_2 IN_4
#define ScaledValue 4
int mode, ticks, powerA, powerC, tones, fields, wrongLogPort, poweredLog, wrongHeader, sensorReadCalls;
int reverseA, reverseC, stoppedAfterMotion, configuredPorts;
long rawA, rawC;
void Off(int ports) {
    if (powerA != 0 || powerC != 0) { stoppedAfterMotion = 1; }
    if (ports & OUT_A) { powerA = 0; rawA = 0; }
    if (ports & OUT_C) { powerC = 0; rawC = 0; }
}
void OnFwd(int ports, int power) {
    stoppedAfterMotion = 0;
    if (ports & OUT_A) { powerA = power; rawA = 0; }
    if (ports & OUT_C) { powerC = power; rawC = 0; }
}
void OnRev(int ports, int power) {
    OnFwd(ports, -power);
    if (ports & OUT_A) { reverseA++; }
    if (ports & OUT_C) { reverseC++; }
}
void Wait(int ms) {
    (void)ms;
    ticks++;
    if (mode == 5) { return; }
    if (mode != 19) { rawA += powerA / 5; }
    rawC += powerC / 5;
    if (mode == 6 && powerC < 0) { rawC = 1; }
    if (mode == 7 && powerC > 0) { rawC = -1; }
}
long MotorRotationCount(int port) {
    if (mode == 2) { return 30000; }
    if (mode == 3 && ticks > 4) { return 30000; }
    return port == OUT_A ? rawA : rawC;
}
int Sensor(int port) {
    sensorReadCalls++;
    if (mode == 25) {
        if (sensorReadCalls <= 2) { return 49; }
        return port == CONTROL_1 ? 49 : 0;
    }
    if (mode == 4) { return 101; }
    if (mode == 15) { return -1; }
    if (mode == 16) { return 30000; }
    if (mode == 14) { return port == CONTROL_1 ? 0 : 49; }
    if (mode == 20) { return 49; }
    if (mode == 21) { return 100; }
    if (mode == 24) { return port == CONTROL_2 ? 0 : 49; }
    if (mode == 26) {
        if (ticks < 8) { return 0; }
        if (ticks < 132) { return port == CONTROL_1 ? 0 : 49; }
        return 0;
    }
    if (mode == 27) {
        if (ticks < 8) { return 0; }
        if (ticks < 12) { return port == CONTROL_1 ? 0 : 49; }
        return 0;
    }
    if (mode == 12 && stoppedAfterMotion && ticks >= 8) { return 49; }
    if (ticks >= 8) {
        if (mode == 1) { return 49; }
        if (mode == 6 || mode == 10) { return port == CONTROL_1 ? 0 : 49; }
        if (mode == 11) { return port == CONTROL_2 ? 0 : 49; }
        if (mode == 8) { return 100; }
        if (mode == 9) { return port == CONTROL_1 ? 100 : 0; }
    }
    if (mode == 22) {
        if (ticks < 8) { return port == CONTROL_1 ? 0 : 49; }
        if (ticks < 15) { return 100; }
        if (ticks < 21) { return port == CONTROL_1 ? 0 : 49; }
        return 100;
    }
    if (mode == 23) {
        if (ticks < 8) { return 0; }
        if (ticks < 15) { return 100; }
        if (ticks < 21) { return port == CONTROL_1 ? 0 : 100; }
        return 100;
    }
    if (mode == 0 || mode == 12 || mode == 13) {
        if (ticks < 8) { return 0; }
        if (ticks < 15) { return 100; }
        if (mode == 13) {
            if (ticks < 17) { return 0; }
        } else {
            if (ticks < 21) { return 0; }
        }
        return 100;
    }
    return 0;
}
void SetSensorLight(int port) { configuredPorts |= 1 << port; }
void SetInput(int port, int field, long value) {
    (void)field;
    if (fields % 26 == 0 && value != 38) { wrongHeader++; }
    if (fields % 26 == 1 && value != 3) { wrongHeader++; }
    fields++;
    if (port != IN_1) { wrongLogPort++; }
    if (powerA != 0 || powerC != 0) { poweredLog++; }
}
void PlayTone(int frequency, int duration) {
    (void)frequency; (void)duration; tones++;
}
'''


class ReactiveSimpleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("clang")
        if not compiler:
            raise unittest.SkipTest("clang unavailable")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-reactive-")
        cls.addClassCleanup(cls.temp.cleanup)
        source = Path(cls.temp.name) / "reactive.c"
        source.write_text(HARNESS + '\n#include "' +
                          str(ROOT / "robot_reactivo_simple.nxc") + '"\n')
        library = Path(cls.temp.name) / "reactive.so"
        flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        subprocess.run([compiler, *flags, "-std=c99", "-Wall", "-Wextra", "-Werror",
                        str(source), "-o", str(library)], check=True,
                       capture_output=True, text=True)
        cls.lib = ctypes.CDLL(str(library))

    def field(self, name, kind=ctypes.c_int):
        return kind.in_dll(self.lib, name)

    def value(self, name):
        return self.field(name).value

    def setUp(self):
        for name in ("mode", "ticks", "powerA", "powerC", "tones", "fields",
                     "wrongLogPort", "poweredLog", "reverseA", "reverseC",
                     "wrongHeader",
                     "sensorReadCalls",
                     "stoppedAfterMotion", "configuredPorts", "reactiveReason",
                     "reactiveEvent", "reactiveSamples", "reactiveStarted",
                     "reactiveCandidate", "reactiveArmed", "reactiveBlackRun",
                     "reactiveWhiteRun", "reactiveWhiteActive", "reactiveWhiteAge",
                     "reactiveStraight", "reactiveCorrection1", "reactiveCorrection2",
                     "reactiveMarkerIntervals", "reactiveFlatA", "reactiveFlatC",
                     "reactiveFlat", "reactiveCommandA", "reactiveCommandC"):
            self.field(name).value = 0
        self.field("reactiveCorrectionState").value = 0
        for name in ("rawA", "rawC", "reactiveDeltaA", "reactiveDeltaC",
                     "reactiveCorrectionDifference"):
            self.field(name, ctypes.c_long).value = 0
        self.field("reactiveS1").value = 30000
        self.field("reactiveS2").value = 30000

    def run_case(self, mode):
        self.field("mode").value = mode
        self.lib.RunReactiveFollower()
        self.assertEqual(self.value("powerA"), 0)
        self.assertEqual(self.value("powerC"), 0)
        self.assertEqual(self.value("wrongLogPort"), 0)
        self.assertEqual(self.value("poweredLog"), 0)
        self.assertEqual(self.value("wrongHeader"), 0)
        self.assertEqual(self.value("fields") % 26, 0)
        return self.value("reactiveReason")

    def test_rearmed_return_is_candidate_with_two_tones_not_coverage_claim(self):
        self.assertEqual(self.run_case(0), 100)
        self.assertEqual(self.value("reactiveStarted"), 1)
        self.assertEqual(self.value("reactiveCandidate"), 1)
        self.assertEqual(self.value("tones"), 2)
        self.assertEqual(self.value("configuredPorts"), (1 << 3) | (1 << 4))

    def test_both_gray_stops_without_forward_search(self):
        self.assertEqual(self.run_case(1), 1)
        self.assertEqual(self.value("reactiveCandidate"), 0)
        self.assertEqual(self.value("reactiveSamples"), 4)
        self.assertEqual(self.value("tones"), 0)

    def test_left3_black_commands_rightAforward_leftCreverse(self):
        self.assertEqual(self.run_case(10), 11)
        self.assertGreater(self.value("reactiveCorrection1"), 0)
        self.assertGreater(self.value("reverseC"), 0)
        self.assertEqual(self.value("reverseA"), 0)

    def test_right4_black_commands_leftCforward_rightAreverse(self):
        self.assertEqual(self.run_case(11), 11)
        self.assertGreater(self.value("reactiveCorrection2"), 0)
        self.assertGreater(self.value("reverseA"), 0)
        self.assertEqual(self.value("reverseC"), 0)

    def test_frozen_encoders_stop_after40_powered_intervals(self):
        self.assertEqual(self.run_case(5), 7)
        self.assertEqual(self.value("reactiveSamples"), 40)

    def test_one_frozen_drive_also_stops(self):
        self.assertEqual(self.run_case(19), 7)
        self.assertEqual(self.value("reactiveSamples"), 40)

    def test_wrong_encoder_sign_stops(self):
        for mode in (6, 7):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_case(mode), 6)

    def test_encoder_sentinels_stop_before_or_after_first_interval(self):
        for mode, samples in ((2, 0), (3, 1)):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_case(mode), 5)
                self.assertEqual(self.value("reactiveSamples"), samples)

    def test_invalid_sensor_inputs_never_drive(self):
        for mode in (4, 15, 16):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_case(mode), 4)
                self.assertEqual(self.value("reactiveSamples"), 0)

    def test_invalid_initial_contact_never_drives(self):
        for mode in (20, 21):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_case(mode), 2)
                self.assertEqual(self.value("reactiveSamples"), 0)

    def test_either_one_black_sensor_can_start_and_use_its_correction(self):
        for mode, field in ((14, "reactiveCorrection1"), (24, "reactiveCorrection2")):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_case(mode), 11)
                self.assertGreater(self.value(field), 0)
                self.assertEqual(self.value("reactiveCandidate"), 0)

    def test_startup_log_preserves_rejecting_sample_not_later_stopped_read(self):
        self.assertEqual(self.run_case(25), 2)
        self.assertEqual(self.value("reactiveSamples"), 0)
        self.assertEqual(self.value("reactiveS1"), 49)
        self.assertEqual(self.value("reactiveS2"), 49)
        self.assertEqual(self.value("sensorReadCalls"), 2)

    def test_one_sided_nonwhite_contact_can_rearm_without_requiring_both_black(self):
        self.assertEqual(self.run_case(22), 100)
        self.assertEqual(self.value("tones"), 2)
        self.assertEqual(self.value("reactiveCandidate"), 1)

    def test_mixed_white_and_black_cannot_rearm_consumed_marker(self):
        self.assertEqual(self.run_case(23), 8)
        self.assertEqual(self.value("tones"), 1)
        self.assertEqual(self.value("reactiveCandidate"), 0)

    def test_white_parked_after_start_cannot_finish(self):
        self.assertEqual(self.run_case(8), 8)
        self.assertEqual(self.value("tones"), 1)
        self.assertEqual(self.value("reactiveCandidate"), 0)

    def test_mixed_white_cannot_confirm_a_marker(self):
        self.assertEqual(self.run_case(9), 8)
        self.assertEqual(self.value("tones"), 0)
        self.assertEqual(self.value("reactiveStarted"), 0)

    def test_two_black_samples_do_not_rearm_consumed_marker(self):
        self.assertEqual(self.run_case(13), 8)
        self.assertEqual(self.value("tones"), 1)
        self.assertEqual(self.value("reactiveCandidate"), 0)

    def test_stopped_marker_resample_can_reject_contact(self):
        self.assertEqual(self.run_case(12), 10)
        self.assertEqual(self.value("tones"), 0)
        self.assertEqual(self.value("reactiveCandidate"), 0)
        self.assertEqual(self.value("reactiveStarted"), 0)

    def test_overall_watchdog_is_not_a_lap(self):
        self.assertEqual(self.run_case(18), 3)
        self.assertEqual(self.value("reactiveSamples"), 6000)
        self.assertEqual(self.value("reactiveCandidate"), 0)

    def test_persistent_correction_is_bounded_by_sampled_difference_not_time_extension(self):
        for mode in (10, 11):
            with self.subTest(mode=mode):
                self.setUp()
                self.assertEqual(self.run_case(mode), 11)
                difference = self.field("reactiveCorrectionDifference", ctypes.c_long).value
                self.assertGreaterEqual(abs(difference), 743)
                self.assertLess(self.value("reactiveSamples"), 6000)

    def test_reacquisition_at_budget_releases_correction_instead_of_false_stop(self):
        self.assertEqual(self.run_case(26), 3)
        self.assertEqual(self.value("reactiveCorrectionState"), 0)
        self.assertEqual(self.field("reactiveCorrectionDifference", ctypes.c_long).value, 0)

    def test_short_reactive_correction_does_not_have_to_reach743(self):
        self.assertEqual(self.run_case(27), 3)
        self.assertEqual(self.value("reactiveCorrection1"), 4)
        self.assertEqual(self.value("reverseC"), 4)
        self.assertEqual(self.field("reactiveCorrectionDifference", ctypes.c_long).value, 0)

    def test_direction_switch_restarts_the_local_not_whole_route_budget(self):
        self.field("reactiveCorrectionState").value = 1
        self.field("reactiveCorrectionDifference", ctypes.c_long).value = 800
        self.assertEqual(self.lib.ReactiveInterval(2), 1)
        self.assertEqual(self.value("reactiveCorrectionState"), 2)
        self.assertEqual(self.field("reactiveCorrectionDifference", ctypes.c_long).value, -6)
        self.lib.Off(5)

    def test_white_release_does_not_inherit_old_correction_budget(self):
        self.field("reactiveCorrectionState").value = 1
        self.field("reactiveCorrectionDifference", ctypes.c_long).value = 800
        self.field("reactiveWhiteActive").value = 1
        self.assertEqual(self.lib.ReactiveInterval(1), 1)
        self.assertEqual(self.value("reactiveCorrectionState"), 0)
        self.assertEqual(self.value("powerA"), 20)
        self.assertEqual(self.value("powerC"), 20)
        self.lib.Off(5)

    def test_source_has_one_entry_no_script_and_no_unsupported_boolean_operators(self):
        source = (ROOT / "robot_reactivo_simple.nxc").read_text()
        code = re.sub(r"//[^\n]*", "", source)
        self.assertNotIn("&&", code)
        self.assertNotIn("||", code)
        self.assertNotIn('#include', code)
        self.assertNotIn("RoutePivot", code)
        self.assertNotIn("routeComplete", code)
        self.assertEqual(code.count("task main()"), 1)
        self.assertNotIn("SetInput(IN_3", code)
        self.assertNotIn("SetInput(IN_4", code)
        self.assertNotIn("SetInput(IN_2", code)
        self.assertNotIn("SetSensorLight(IN_1", code)
        self.assertNotIn("SetSensorLight(IN_2", code)


if __name__ == "__main__":
    unittest.main()
