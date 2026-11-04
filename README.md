# OpenEdge-NPU
Open-source, parameterisable FPGA neural-network accelerator

## Development Environment

OpenEdge NPU is developed using SystemVerilog and
a Python-based automated verification environment.

### Verified Toolchain

- Ubuntu 26.04.1 LTS (WSL2)
- Python 3.14.4
- Verilator 5.032
- cocotb 2.1.0
- pytest 9.2.0
- AMD Vivado 2024.1 (Windows, synthesis planned)

### Setup

Install the required Linux packages:

```bash
sudo apt update
sudo apt install -y python3 python3-pip \
    python3-venv verilator build-essential git make
```

Clone the repository:

```bash
git clone https://github.com/ronaldopickerin/OpenEdge-NPU.git
cd OpenEdge-NPU
```

Create and activate the Python environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

### Run RTL Verification

```bash
python -m pytest verification/test_smoke_runner.py -v -s
```

The smoke test compiles a SystemVerilog adder using
Verilator and verifies its operation with cocotb.

Expected outcome: 1 passed (5 arithmetic vectors).

Note: Package versions in Ubuntu repositories can
change. The versions above are the tested baseline.
