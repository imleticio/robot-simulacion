"""Offline geometry checks, not validation of active RoboSim configuration."""
import math
import unittest


def sensor_points(radius, angle_degrees):
    angle = math.radians(angle_degrees)
    forward = radius * math.cos(angle)
    lateral = radius * math.sin(angle)
    return (forward, lateral), (forward, -lateral)


class SensorGeometryTests(unittest.TestCase):
    def test_default_ideal_separation_is_about_one_fifth_cell(self):
        left, right = sensor_points(1.15, 5)
        self.assertAlmostEqual(left[1] - right[1], 0.200458208, places=7)

    def test_spreading_sensors_changes_forward_offset_too(self):
        original, _ = sensor_points(1.15, 5)
        spread, _ = sensor_points(1.15, 20)
        self.assertLess(spread[0], original[0])
        self.assertAlmostEqual(2 * spread[1], 0.786646330, places=7)

    def test_same_cell_contact_does_not_prove_heading(self):
        # A shared black cell can contain two points at different headings.
        # This is a counterexample, not a reconstruction of the live run.
        for heading in (0, 20, 45):
            angle = math.radians(heading)
            readings = []
            for lateral in (-0.1, 0.1):
                x = 0.5 - lateral * math.sin(angle)
                z = 0.5 + lateral * math.cos(angle)
                readings.append((int(x), int(z)))
            self.assertEqual(readings, [(0, 0), (0, 0)])

    def test_simultaneous_loss_without_one_sided_state_is_possible(self):
        # Crossing a cell boundary head-on can change both cells together.
        # Smaller forward steps alone do not create lateral information.
        for forward in (0.9, 1.01):
            cells = [(int(forward), int(0.5 + side)) for side in (-0.1, 0.1)]
            self.assertEqual(cells[0], cells[1])
