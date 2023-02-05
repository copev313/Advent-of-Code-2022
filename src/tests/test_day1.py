"""
    Day 1 - Solution Tests
"""
import pytest

from src.day1 import part1, part2, parse_input

# ============================================================================

@pytest.fixture
def example_input():
    return parse_input("day1_example.txt")


@pytest.fixture
def input():
    return parse_input("day1.txt")

# ============================================================================

def test_part1_example(example_input):
    expected_value = 24000
    actual_value = part1(example_input)[0]
    assert actual_value == expected_value


def test_part1_actual(input):
    expected_value = 74198
    actual_value = part1(input)[0]
    assert actual_value == expected_value


def test_part2_example(example_input):
    expected_value = 45000
    actual_value = part2(example_input)
    assert actual_value == expected_value


def test_part2_actual(input):
    expected_value = 209914
    actual_value = part2(input)
    assert actual_value == expected_value
