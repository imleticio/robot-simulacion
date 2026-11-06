"""Check command preservation and real x86 reset dispatch, not a full RXE run."""
import importlib.util
from pathlib import Path
import shutil
import struct
import subprocess
import unittest

from tools.patch_robosim_yield import patched_bytes


ROOT = Path(__file__).resolve().parents[1]
EXE = Path.home() / "Downloads/BricxCC Simulator/legosimulator/legosimulator.exe"
NBC = EXE.parent.parent / "nbc.exe"
AUDIT_AVAILABLE = all(importlib.util.find_spec(name) for name in ("unicorn", "pefile"))


def command_model(refresh, command_lost=False, frozen_physics=False, reset_count=False):
    """Counterexample model: refreshing can repair power, not frozen physics."""
    counter = 0
    power = 0 if command_lost else 15
    flat = 0
    for sample in range(1, 376):
        if refresh:
            power = 15
            if reset_count:
                counter = 0
        before = counter
        if not frozen_physics:
            counter += power // 5
        flat = flat + 1 if counter == before else 0
        if flat >= 40:
            return 21, sample, counter
        if counter >= 743:
            return 5, sample, counter
    return 4, 375, counter


class CommandRefreshTests(unittest.TestCase):
    def test_wrapper_only_adds_command_refresh_to110(self):
        def defines(name):
            return dict(line.split()[1:3] for line in (ROOT / name).read_text().splitlines()
                        if line.startswith("#define"))
        expected = defines("robot_prueba_codo_tiempo.nxc")
        expected.update(CORNER_REVISION="111", TURN_REFRESH_COMMAND="1")
        self.assertEqual(defines("robot_prueba_codo_mando.nxc"), expected)

    @unittest.skipUnless(NBC.exists(), "requires bundled compiler header strings")
    def test_bundled_macro_supports_reset_none_and_update_flags(self):
        source = NBC.read_bytes()
        self.assertIn(b"#define RESET_NONE           0x00", source)
        self.assertIn(b"#define Power           2", source)
        self.assertIn(b"#define OnFwdEx(_ports, _pwr, _reset)", source)
        self.assertIn(b"UF_UPDATE_TACHO_LIMIT+UF_UPDATE_MODE+UF_UPDATE_SPEED+_reset", source)

    def test_refresh_recovers_only_a_lost_command_in_the_model(self):
        self.assertEqual(command_model(False, command_lost=True), (21, 40, 0))
        self.assertEqual(command_model(True, command_lost=True), (5, 248, 744))

    def test_refresh_does_not_claim_to_fix_frozen_physics(self):
        self.assertEqual(command_model(True, frozen_physics=True), (21, 40, 0))

    def test_resetting_each_time_cannot_complete_the_pivot(self):
        self.assertEqual(command_model(True, reset_count=True), (4, 375, 3))

    def test_normal_model_progress_is_not_extended_to_watchdog(self):
        self.assertEqual(command_model(True), command_model(False))
        self.assertEqual(command_model(True), (5, 248, 744))

    def test_preprocessing_preserves_baseline_and_adds_no_wait_or_angle(self):
        compiler = shutil.which("clang")
        if not compiler:
            self.skipTest("clang unavailable; NBC compilation is separate")
        def preprocess(name):
            return subprocess.check_output(
                [compiler, "-E", "-P", "-x", "c", str(ROOT / name)], text=True)
        old = preprocess("robot_prueba_codo_tiempo.nxc")
        new = preprocess("robot_prueba_codo_mando.nxc")
        self.assertEqual(old.count("SetInput("), 72)
        self.assertEqual(new.count("SetInput("), 76)
        self.assertIn("SetInput(IN_1, ScaledValue, 111);", new)
        turn = new.split("    if (phase == 1)", 1)[1].split("    if (phase == 2)", 1)[0]
        loop = turn.split("for (turnStep", 1)[1]
        self.assertIn("OnFwdEx(OUT_C, 15, RESET_NONE);", loop)
        self.assertNotIn("startC =", loop)
        self.assertNotIn("startA =", loop)
        self.assertLess(loop.index("turnPowerBefore = MotorPower"), loop.index("OnFwdEx("))
        self.assertLess(loop.index("OnFwdEx("), loop.index("turnPowerAfter = MotorPower"))
        self.assertLess(loop.index("turnPowerAfter = MotorPower"), loop.index("Wait(20)"))
        self.assertIn("stopReason = 22;", loop)
        self.assertIn("deltaC >= 743", loop)
        self.assertIn("turnFlatRun >= 40", loop)
        for command in ("OnFwd(", "Off(", "Wait(", "MotorRotationCount("):
            self.assertEqual(old.count(command), new.count(command))
        self.assertNotIn("MotorPower(", old)
        for forbidden in ("OnRev(", "&&", "||", "PlayTone("):
            self.assertNotIn(forbidden, new)


@unittest.skipUnless(AUDIT_AVAILABLE and EXE.exists(), "requires audit dependencies and original EXE")
class OutputFlagsMachineCodeTests(unittest.TestCase):
    """Run the actual setOutputConfiguration dispatcher with a stub backend."""
    def dispatch(self, flags):
        import pefile
        from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_CODE
        from unicorn.x86_const import (UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDI,
                                       UC_X86_REG_ESI, UC_X86_REG_ESP, UC_X86_REG_EIP)
        image = EXE.read_bytes()
        patched_bytes(image)  # Verify the audited original hash before using addresses.
        pe = pefile.PE(data=image)
        uc = Uc(UC_ARCH_X86, UC_MODE_32)
        uc.mem_map(0x400000, (pe.OPTIONAL_HEADER.SizeOfImage + 4095) & ~4095)
        uc.mem_write(0x400000, pe.get_memory_mapped_image())
        uc.mem_map(0x100000, 0x20000)
        system, backend, vtable, stubs, end = 0x110000, 0x111000, 0x111100, 0x112000, 0x113000
        def write32(address, value):
            uc.mem_write(address, struct.pack("<I", value))
        def read32(address):
            return struct.unpack("<I", uc.mem_read(address, 4))[0]
        write32(system, backend)
        write32(backend, vtable)
        for slot in range(7, 12):
            write32(vtable + slot * 4, stubs + slot * 16)
        stack = 0x108000
        write32(stack, end)
        uc.reg_write(UC_X86_REG_ESP, stack)
        uc.reg_write(UC_X86_REG_EAX, 0)  # UpdateFlags field
        uc.reg_write(UC_X86_REG_ECX, flags)
        uc.reg_write(UC_X86_REG_EDI, system)
        uc.reg_write(UC_X86_REG_ESI, 2)  # C
        called = []
        def hook(machine, address, size, _):
            if stubs + 7 * 16 <= address <= stubs + 11 * 16:
                self.assertEqual((address - stubs) % 16, 0)
                called.append((address - stubs) // 16)
                sp = machine.reg_read(UC_X86_REG_ESP)
                self.assertEqual(read32(sp + 4), 2)
                machine.reg_write(UC_X86_REG_EIP, read32(sp))
                machine.reg_write(UC_X86_REG_ESP, sp + 8)  # thiscall ret4
        uc.hook_add(UC_HOOK_CODE, hook)
        uc.emu_start(0x41C700, end, count=1000)
        self.assertEqual(uc.reg_read(UC_X86_REG_EIP), end)
        return called

    def test_reset_none_only_dispatches_mode_and_target_commits(self):
        self.assertEqual(self.dispatch(0x07), [7, 8])

    def test_legacy_onfwd_flags_also_dispatch_counter_resets(self):
        self.assertEqual(self.dispatch(0x07 + 0x28), [7, 8, 9, 10])

    def test_rotation_reset_is_a_separate_explicit_bit(self):
        self.assertEqual(self.dispatch(0x07 + 0x40), [7, 8, 11])
