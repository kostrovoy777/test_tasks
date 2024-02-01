import random
import pytest


def convert_int_to_hex(int_mass: list[int]) -> str:
    assert len(int_mass) == 256, "Incorrect length"
    assert all([isinstance(number, int) for number in int_mass]), "Not int number"
    assert all([0 <= number <= 255 for number in int_mass]), "Incorrect int range"
    hex_result = ""
    for number in int_mass[1:int_mass[0] + 1]:
        hex_result += "{:02x} ".format(number)
    return "0x" + hex_result.upper().strip()


def test_correct():
    random.seed(version=2)
    int_mass = [23, 89, 2, 137, 172, 177, 19, 9, 172, 39, 20, 9, 172, 37, 20, 9, 175, 161, 85, 9, 172, 178, 100, 9, 0]
    while len(int_mass) < 256:
        int_mass.append(random.randint(0, 255))
    assert convert_int_to_hex(int_mass) == "0x59 02 89 AC B1 13 09 AC 27 14 09 AC 25 14 09 AF A1 55 09 AC B2 64 09"


def test_incorrect_length():
    int_mass = [23, 89, 2, 137, 172, 177, 19, 9, 172, 39, 20, 9, 172, 37, 20, 9, 175, 161, 85, 9, 172, 178, 100, 9, 0]
    with pytest.raises(AssertionError, match="Incorrect length"):
        convert_int_to_hex(int_mass)


def test_not_int():
    int_mass = [23, 89, 2, 137, 172, 177, 19, 9, "172", 39, 20, 9, 172, 37, 20, 9, 175, 161, 85, 9, 172, 178, 100, 9, 0]
    while len(int_mass) < 256:
        int_mass.append(random.randint(0, 255))
    with pytest.raises(AssertionError, match="Not int number"):
        convert_int_to_hex(int_mass)
