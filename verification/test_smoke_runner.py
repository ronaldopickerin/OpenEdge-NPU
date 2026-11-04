
import sys
from pathlib import Path

from cocotb_tools.runner import get_runner


ROOT = Path(__file__).resolve().parents[1]
TEST_DIR = ROOT / "verification" / "cocotb"


def test_smoke_runner(monkeypatch):
    # Add testbench directory to Python's import path.
    # cocotb's runner uses sys.path when launching
    # the simulator.
    monkeypatch.syspath_prepend(str(TEST_DIR))

    runner = get_runner("verilator")

    runner.build(
        sources=[ROOT / "rtl/core/smoke_test.sv"],
        hdl_toplevel="smoke_test",
        build_dir=ROOT / "build/smoke",
        always=True,
    )

    runner.test(
        hdl_toplevel="smoke_test",
        test_module="test_smoke",
        test_dir=ROOT / "build/smoke",
    )
