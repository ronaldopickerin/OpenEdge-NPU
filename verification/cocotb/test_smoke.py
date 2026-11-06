import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_addition(dut):
    test_cases = [
        (0, 0),
        (1, 1),
        (10, 20),
        (127, 128),
        (255, 255),
    ]

    for a, b in test_cases:
        dut.a.value = a
        dut.b.value = b

        await Timer(1, unit="ns")

        actual = int(dut.sum.value)
        expected = a + b

        assert actual == expected, (
            f"FAIL: {a} + {b} = {actual}, "
            f"expected {expected}"
        )

        dut._log.info(
            f"PASS: {a} + {b} = {actual}"
        )