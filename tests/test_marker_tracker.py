"""Execute the actual API-free NXC state machine as native C, not RoboSim."""
import ctypes
from pathlib import Path
import platform
import shutil
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]


class MarkerTrackerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        compiler = shutil.which("clang")
        if compiler is None:
            raise unittest.SkipTest("clang unavailable; NBC compilation is separate")
        cls.temp = tempfile.TemporaryDirectory(prefix="robot-marker-")
        cls.addClassCleanup(cls.temp.cleanup)
        library = Path(cls.temp.name) / "marker.so"
        shared_flags = ["-dynamiclib"] if platform.system() == "Darwin" else ["-shared", "-fPIC"]
        subprocess.run([compiler, *shared_flags, "-Wall", "-Wextra", "-Werror",
                        "-std=c99", "-x", "c", str(ROOT / "robot_marker_tracker.nxc"),
                        "-o", str(library)], check=True, capture_output=True, text=True)
        cls.lib = ctypes.CDLL(str(library))
        cls.lib.ResetMarkerTracker.argtypes = []
        cls.lib.ResetMarkerTracker.restype = None
        cls.lib.UpdateMarkerTracker.argtypes = [ctypes.c_int] * 3
        cls.lib.UpdateMarkerTracker.restype = None

    def setUp(self):
        self.lib.ResetMarkerTracker()

    def value(self, name):
        return ctypes.c_int.in_dll(self.lib, name).value

    def feed(self, left, right, count=1, route=0):
        events = []
        for _ in range(count):
            self.lib.UpdateMarkerTracker(left, right, route)
            event = self.value("markerEvent")
            if event:
                events.append(event)
        return events

    def start(self):
        self.feed(0, 0, 3)
        self.assertEqual(self.feed(100, 100, 3), [1])

    def cross(self, route):
        self.feed(0, 0, 3)
        return self.feed(100, 100, 3, route)

    def test_start_is_not_a_completed_lap(self):
        self.start()
        self.assertEqual(self.value("markerCrossings"), 1)
        self.assertEqual(self.value("markerLapCount"), 0)
        self.assertEqual(self.value("markerFinished"), 0)

    def test_three_accepted_crossings_complete_exactly_two_laps(self):
        self.start()
        self.assertEqual(self.cross(1), [2])
        self.assertEqual(self.value("markerLapCount"), 1)
        self.assertEqual(self.value("markerFinished"), 0)
        self.assertEqual(self.cross(1), [3])
        self.assertEqual(self.value("markerLapCount"), 2)
        self.assertEqual(self.value("markerCrossings"), 3)
        self.assertEqual(self.value("markerFinished"), 1)

    def test_starting_on_white_does_not_invent_start(self):
        self.assertEqual(self.feed(100, 100, 30), [])
        self.assertEqual(self.value("markerCrossings"), 0)

    def test_remaining_on_white_emits_only_one_event(self):
        self.start()
        self.assertEqual(self.feed(100, 100, 100, route=1), [])
        self.assertEqual(self.value("markerCrossings"), 1)

    def test_one_gray_dip_does_not_rearm(self):
        self.start()
        self.feed(69, 69)
        self.assertEqual(self.feed(100, 100, 3, route=1), [])

    def test_long_gray_does_not_rearm(self):
        self.start()
        self.feed(49, 49, 100)
        self.assertEqual(self.feed(100, 100, 3, route=1), [])

    def test_short_black_dip_does_not_rearm(self):
        self.start()
        self.feed(0, 0, 2)
        self.assertEqual(self.feed(100, 100, 3, route=1), [])

    def test_black_release_must_be_consecutive(self):
        self.start()
        self.feed(0, 0, 2)
        self.feed(49, 49)
        self.feed(0, 0)
        self.assertEqual(self.feed(100, 100, 3, route=1), [])

    def test_white_confirmation_must_be_consecutive(self):
        self.feed(0, 0, 3)
        self.assertEqual(self.feed(100, 100, 2), [])
        self.feed(49, 49)
        self.assertEqual(self.feed(100, 100, 2), [])
        self.assertEqual(self.feed(100, 100), [1])

    def test_one_white_sensor_is_not_a_marker(self):
        self.feed(0, 0, 3)
        for pair in [(100, 0), (0, 100), (100, 49), (49, 100)]:
            self.assertEqual(self.feed(*pair, count=5), [])
        self.assertEqual(self.value("markerCrossings"), 0)

    def test_early_crossing_is_rejected_not_counted_as_lap(self):
        self.start()
        self.assertEqual(self.cross(0), [4])
        self.assertEqual(self.value("markerRejectedCrossings"), 1)
        self.assertEqual(self.value("markerLapCount"), 0)

    def test_route_flag_cannot_late_accept_same_rejected_crossing(self):
        self.start()
        self.cross(0)
        self.assertEqual(self.feed(100, 100, 10, route=1), [])
        self.assertEqual(self.value("markerLapCount"), 0)

    def test_each_lap_requires_its_own_route_permission(self):
        self.start()
        self.cross(1)
        self.assertEqual(self.cross(0), [4])
        self.assertEqual(self.value("markerLapCount"), 1)
        self.assertEqual(self.value("markerFinished"), 0)

    def test_nonboolean_route_values_are_not_permission(self):
        self.start()
        for route in (-1, 2, 30000):
            self.assertEqual(self.cross(route), [4])
        self.assertEqual(self.value("markerLapCount"), 0)

    def test_finish_latches_and_event_does_not_repeat(self):
        self.start()
        self.cross(1)
        self.cross(1)
        self.assertEqual(self.cross(1), [])
        self.assertEqual(self.value("markerLapCount"), 2)
        self.assertEqual(self.value("markerCrossings"), 3)

    def test_reset_requires_new_black_release_and_new_start(self):
        self.start()
        self.cross(1)
        self.lib.ResetMarkerTracker()
        self.assertEqual(self.value("markerLapCount"), 0)
        self.assertEqual(self.feed(100, 100, 3), [])
        self.start()

    def test_threshold_boundaries_do_not_count_as_black_or_white(self):
        self.feed(25, 25, 3)
        self.assertEqual(self.feed(100, 100, 3), [])
        self.feed(24, 24, 3)
        self.assertEqual(self.feed(75, 75, 3), [])
        self.assertEqual(self.feed(76, 76, 3), [1])

    def test_counters_saturate_during_long_uniform_readings(self):
        self.feed(0, 0, 1000)
        self.assertEqual(self.value("markerBlackSamples"), 3)
        self.feed(100, 100, 1000)
        self.assertEqual(self.value("markerWhiteSamples"), 3)

    def test_invalid_sensor_values_are_faults_not_white_markers(self):
        for pair in [(-1, 100), (100, -1), (30000, 100), (100, 101)]:
            self.lib.ResetMarkerTracker()
            self.feed(0, 0, 3)
            self.assertEqual(self.feed(*pair), [5])
            self.assertEqual(self.feed(100, 100, 3), [])
            self.assertEqual(self.value("markerCrossings"), 0)

    def test_invalid_reading_breaks_white_confirmation(self):
        self.feed(0, 0, 3)
        self.feed(100, 100, 2)
        self.feed(30000, 30000)
        self.assertEqual(self.feed(100, 100, 3), [])

    def test_module_is_silent_api_free_and_not_integrated_into_corner(self):
        source = (ROOT / "robot_marker_tracker.nxc").read_text()
        for forbidden in ("&&", "||", "OnFwd(", "OnRev(", "PlayTone(", "Sensor(", "Wait("):
            self.assertNotIn(forbidden, source)
        corner = (ROOT / "robot_prueba_codo.nxc").read_text()
        self.assertNotIn("robot_marker_tracker.nxc", corner)
