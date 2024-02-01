import pytest


def convert_ascii_to_hex(ascii_num: str, order: bytes) -> list[bytes]:
    assert ascii_num.isdigit(), "Incorrect ASCII number"
    assert order in [b'\x01', b'\x00'], "Incorrect order parameter"

    hex_str = "{:02x}".format(int(ascii_num))
    if len(hex_str) % 2 != 0:
        hex_str = "0" + hex_str

    hex_mass = []
    for i in range(0, len(hex_str), 2):
        hex_mass.append(bytes.fromhex(hex_str[i: i+2]))

    if order == b'\x01':
        hex_mass.reverse()

    return hex_mass


def test_correct():
    assert convert_ascii_to_hex("65281", b'\x01') == [b'\x01', b'\xff']


def test_incorrect_ascii():
    with pytest.raises(AssertionError, match="Incorrect ASCII number"):
        convert_ascii_to_hex("65ssss", b'\x01')


def test_incorrect_order():
    with pytest.raises(AssertionError, match="Incorrect order parameter"):
        convert_ascii_to_hex("65281", b'\x03')
