"""Execute the real x86 runner with a deterministic clock and a stub VM step.

Optional audit dependencies: unicorn, pefile. No GUI, motors or sound.
This verifies scheduler control flow, not a complete Windows/RoboSim run.
"""
import importlib.util
import struct
import unittest
from pathlib import Path

from tools.patch_robosim_yield import patched_bytes, file_offset, BRANCH_VA

EXE = Path.home() / "Downloads/BricxCC Simulator/legosimulator/legosimulator.exe"
AVAILABLE = all(importlib.util.find_spec(name) for name in ("unicorn", "pefile"))


@unittest.skipUnless(AVAILABLE and EXE.exists(), "requires audit dependencies and original EXE")
class SchedulerMachineCodeTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.original = EXE.read_bytes()
        cls.fixed = patched_bytes(cls.original)

    def run_batch(self, image, budget_ms=120, wait_ms=20, deadline=0, paused=False):
        import pefile
        from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_CODE
        from unicorn.x86_const import UC_X86_REG_EAX, UC_X86_REG_ESP, UC_X86_REG_EIP

        pe = pefile.PE(data=image)
        uc = Uc(UC_ARCH_X86, UC_MODE_32)
        uc.mem_map(0, 0x1000)  # SEH slot at fs:0
        uc.mem_map(0x400000, (pe.OPTIONAL_HEADER.SizeOfImage + 4095) & ~4095)
        uc.mem_write(0x400000, pe.get_memory_mapped_image())
        uc.mem_map(0x100000, 0x20000)  # stack, fake objects, import stub
        runner, interpreter, clock_stub, end = 0x110000, 0x111000, 0x112000, 0x113000

        def write32(address, value):
            uc.mem_write(address, struct.pack("<I", value))

        def read32(address):
            return struct.unpack("<I", uc.mem_read(address, 4))[0]

        # Verify the imported clock identity rather than assuming an IAT slot.
        imports = {item.address: item.name for group in pe.DIRECTORY_ENTRY_IMPORT
                   for item in group.imports}
        self.assertEqual(imports[0x424078], b"GetTickCount")
        write32(0x424078, clock_stub)
        write32(0x42CC9C, 0)
        write32(runner + 0x2C, interpreter)
        uc.mem_write(runner + 0x34, bytes([paused]))
        write32(interpreter + 0x24, deadline)
        stack = 0x108000
        uc.mem_write(stack, struct.pack("<IIf", end, runner, budget_ms / 1000))
        uc.reg_write(UC_X86_REG_ESP, stack)
        state = {"now": 100, "samples": 0, "step_calls": 0}

        def return_from_call():
            sp = uc.reg_read(UC_X86_REG_ESP)
            uc.reg_write(UC_X86_REG_EIP, read32(sp))
            uc.reg_write(UC_X86_REG_ESP, sp + 4)

        def hook(machine, address, size, _):
            if address == clock_stub:
                state["now"] += 1
                machine.reg_write(UC_X86_REG_EAX, state["now"])
                return_from_call()
            elif address == 0x40A520:
                # Stub the VM payload, not the runner under test. Match step's
                # deadline gate and op_wait's wall-clock deadline semantics.
                state["step_calls"] += 1
                if state["now"] >= read32(interpreter + 0x24):
                    state["samples"] += 1
                    if wait_ms is not None:
                        write32(interpreter + 0x24, state["now"] + wait_ms)
                return_from_call()

        uc.hook_add(UC_HOOK_CODE, hook)
        uc.emu_start(0x40A3F0, end, count=100000)
        self.assertEqual(uc.reg_read(UC_X86_REG_EIP), end)
        return state

    def test_original_consumes_multiple_waits_before_return_to_physics(self):
        result = self.run_batch(self.original)
        self.assertGreaterEqual(result["samples"], 5)
        self.assertGreater(result["step_calls"], result["samples"])

    def test_fix_yields_on_first_positive_wait_even_with_large_budget(self):
        for budget in (5, 120, 1000):
            with self.subTest(budget=budget):
                result = self.run_batch(self.fixed, budget_ms=budget)
                self.assertEqual(result["samples"], 1)
                self.assertEqual(result["step_calls"], 1)

    def test_unexpired_wait_does_not_execute_vm(self):
        for image in (self.original, self.fixed):
            self.assertEqual(self.run_batch(image, deadline=200)["samples"], 0)

    def test_paused_runner_stays_paused(self):
        self.assertEqual(self.run_batch(self.fixed, paused=True)["samples"], 0)

    def test_instruction_stream_without_wait_keeps_budget(self):
        old = self.run_batch(self.original, wait_ms=None)
        new = self.run_batch(self.fixed, wait_ms=None)
        self.assertEqual(new, old)
        self.assertGreater(new["samples"], 1)

    def test_only_branch_displacement_changes(self):
        changed = [i for i, (a, b) in enumerate(zip(self.original, self.fixed)) if a != b]
        self.assertEqual(changed, [file_offset(self.original, BRANCH_VA) + 1])
        self.assertEqual(len(self.original), len(self.fixed))

    def test_rejects_unknown_or_already_patched_binary(self):
        for image in (b"unknown", self.fixed):
            with self.assertRaises(ValueError):
                patched_bytes(image)


if __name__ == "__main__":
    unittest.main()
