"""Bounded sampled progress/contact specification; not route validation."""
from pathlib import Path
import shutil
import subprocess
import unittest


ROOT = Path(__file__).resolve().parents[1]


def controlled_exit(samples, final=(0, 0), limit=200, target=180):
    totals = [0, 0]
    stable = 0
    commands = 0
    reason = 15
    for left, right, da, dc in samples[:limit]:
        if max(left, right) > 75:
            return 1, commands
        if min(left, right) >= 25:
            return 11, commands
        if left < 25 and right < 25 and min(totals) >= target:
            stable += 1
        else:
            stable = 0
        if stable >= 5:
            reason = 16
            break
        commands += 1
        if da == 30000 or dc == 30000:
            return 8, commands
        if min(da, dc) < 0:
            return 7, commands
        totals = [totals[0] + da, totals[1] + dc]
    else:
        if len(samples) < limit:
            raise ValueError("Incomplete model trace")
    if max(final) > 75:
        return 1, commands
    if min(final) >= 25:
        return 11, commands
    if reason == 16 and max(final) >= 25:
        return 15, commands
    return reason, commands


class ControlledExitTests(unittest.TestCase):
    def test_progress_then_five_fresh_both_black_samples_can_complete(self):
        self.assertEqual(controlled_exit([(0, 0, 3, 3)] * 200), (16, 64))

    def test_zero_progress_never_passes_even_on_black(self):
        self.assertEqual(controlled_exit([(0, 0, 0, 0)] * 200), (15, 200))

    def test_one_stalled_track_never_passes(self):
        self.assertEqual(controlled_exit([(0, 0, 0, 3)] * 200), (15, 200))

    def test_runtime_all_right_only_counterexample_is_not_success(self):
        self.assertEqual(controlled_exit([(49, 0, 0, 2)] * 200, final=(49, 0)),
                         (15, 200))

    def test_both_totals_reached_without_fresh_both_black_is_not_success(self):
        samples = [(0, 0, 3, 3)] * 60 + [(0, 49, 2, 0)] * 140
        self.assertEqual(controlled_exit(samples, final=(0, 49)), (15, 200))

    def test_one_sided_contact_resets_confirmation(self):
        samples = ([(0, 0, 3, 3)] * 60 + [(0, 0, 2, 2)] * 4
                   + [(0, 49, 2, 0)] + [(0, 0, 2, 2)] * 5)
        self.assertEqual(controlled_exit(samples), (16, 69))

    def test_loss_and_white_abort_without_recovery_motion(self):
        for sample, reason in [((49, 49, 0, 0), 11), ((0, 100, 0, 0), 1)]:
            self.assertEqual(controlled_exit([sample]), (reason, 0))

    def test_encoder_faults_abort_without_success(self):
        for da, reason in [(30000, 8), (-1, 7)]:
            self.assertEqual(controlled_exit([(0, 0, da, 1)]), (reason, 1))

    def test_final_contact_loss_downgrades_completion(self):
        samples = [(0, 0, 3, 3)] * 200
        for final, reason in [((0, 49), 15), ((49, 49), 11), ((100, 0), 1)]:
            self.assertEqual(controlled_exit(samples, final=final)[0], reason)

    def test_watchdog_final_resample_preserves_white_loss_protection(self):
        samples = [(0, 0, 0, 0)] * 200
        self.assertEqual(controlled_exit(samples, final=(49, 49)), (11, 200))
        self.assertEqual(controlled_exit(samples, final=(100, 0)), (1, 200))

    def test_preprocessor_retains_legacy_layout_and_selects_controlled_gate(self):
        compiler = shutil.which("clang")
        if not compiler:
            self.skipTest("clang preprocessor unavailable; NBC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_salida_medida.nxc")
        new = preprocess("robot_prueba_salida_controlada.nxc")
        self.assertEqual(old.count("SetInput("), 47)
        self.assertEqual(new.count("SetInput("), 50)
        self.assertNotIn("exitCenteredSamples", old)
        self.assertIn("SetInput(IN_1, ScaledValue, 105);", new)
        self.assertIn("exitStep < 200", new)
        self.assertIn("exitTotalA >= 180", new)
        self.assertIn("exitTotalC >= 180", new)
        self.assertIn("exitCenteredSamples >= 5", new)
        self.assertIn("if (stopReason == 15)", new)
        for command in ("OnFwd(", "Off(", "OnRev(", "Wait("):
            self.assertEqual(old.count(command), new.count(command))
        gate = new.split("if (exitCenteredSamples >= 5)", 1)[1]
        self.assertLess(gate.index("stopReason = 16;"), gate.index("OnFwd("))
