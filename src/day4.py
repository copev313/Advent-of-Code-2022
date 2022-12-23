"""
    Day 4: Camp Cleanup
"""
from helpers.input import get_input_data


def parse_input(filename: str) -> list[tuple]:
    """Retrieves, parses, and formats the input data. """
    # Load input data as list of strings:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # Split on comma & convert to tuple:
    lines = map(lambda x: tuple(x.split(",")), lines)
    # Convert to list:
    return list(lines)



def range_to_set(range_str: str) -> set[int]:
    """Converts a range string to a set of integers. """
    start, end = range_str.split("-")
    return set(range(int(start), int(end) + 1))



def part1(data: list[tuple]) -> int:
    """Returns the solution to part 1 of the puzzle.

    Parameters
    ----------
    data : list[tuple]
        The input data to process.

    Returns
    -------
    int:
        The total number of fully contained pairs.
    """
    contained_pairs = 0
    for subset_a, subset_b in data:
        set_A, set_B = range_to_set(subset_a), range_to_set(subset_b)
        # Check if one set is fully contained within the other:
        if set_A.issubset(set_B) or set_B.issubset(set_A):
            contained_pairs += 1
    return contained_pairs



def part2(data: list[tuple]) -> int:
    """Returns the solution to part 2 of the puzzle. 

    Parameters
    ----------
    data : list[tuple]
        The input data to process.

    Returns
    -------
    int:
        The total number of overlapping pair ranges.
    """
    overlapped_pairs = 0
    for subset_a, subset_b in data:
        set_A, set_B = range_to_set(subset_a), range_to_set(subset_b)
        # Check if the sets overlap at all:
        inter = set_A.intersection(set_B)
        if len(inter) > 0:
            overlapped_pairs += 1
    return overlapped_pairs

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day4.txt")
    print(f" Input Data: {input_data} ")

    print(f" Part 1 Solution: {part1(input_data)} ")
    assert part1(input_data) == 509

    print(f" Part 2 Solution: {part2(input_data)} ")
    assert part2(input_data) == 870
