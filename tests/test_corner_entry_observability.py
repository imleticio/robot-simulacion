"""Analytical counterexamples, NOT a reconstruction of the active scene.

An ideal strip ends at forward coordinate zero. Sensor points use the static
mount model. Positive heading is a robot-right turn. The outgoing strip's
width/center and actual active sensor angles remain unknown.
"""
import math
import unittest


def entry_and_pivot(heading_degrees, spread_degrees=20, advance_counts=0):
    heading = math.radians(heading_degrees)
    forward = 1.15 * math.cos(math.radians(spread_degrees))
    lateral = 1.15 * math.sin(math.radians(spread_degrees))
    # First ideal pose with BOTH footprints past the terminal edge, plus a
    # tiny positive crossing. Such loss does not require zero entry heading.
    axle_x = -forward * math.cos(heading) + lateral * abs(math.sin(heading)) + .001
    points_x = [axle_x + forward * math.cos(heading) + side * math.sin(heading)
                for side in (-lateral, lateral)]
    advance = advance_counts * .4 * math.pi / 360
    # Ideal right-pivot radius is half the 1.65 drive spacing.
    exit_x = axle_x + advance * math.cos(heading) + .825 * (
        math.cos(heading) - math.sin(heading)
    )
    return points_x, exit_x, heading_degrees + 90


class EntryObservabilityTests(unittest.TestCase):
    def test_identical_both_lost_event_preserves_different_entry_headings(self):
        results = [entry_and_pivot(angle) for angle in (-10, 0, 10)]
        for footprints, _, _ in results:
            self.assertTrue(all(point > 0 for point in footprints))
        self.assertEqual([result[2] for result in results], [80, 90, 100])
        self.assertGreater(max(r[1] for r in results) - min(r[1] for r in results), .28)

    def test_pre_advance_changes_outgoing_lateral_pose_not_heading(self):
        _, without, yaw_without = entry_and_pivot(0)
        _, with_advance, yaw_with = entry_and_pivot(0, advance_counts=60)
        self.assertAlmostEqual(with_advance - without, .2094395102)
        self.assertEqual(yaw_without, yaw_with)
