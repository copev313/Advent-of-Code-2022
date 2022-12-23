"""
    Day 1: Calorie Counting
"""
from helpers.input import get_input_data


def parse_input(filename: str) -> list[int | None]:
    """Retrieves, parses, and formats the input data. """
    # Load input data as list of strings:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # Convert to integers (except empty strings):
    lines = list(map(lambda x: int(x) if x != "" else None, lines))
    # Ensure last line is None:
    lines = lines if lines[-1] is None else [*lines, None]
    return lines


def part1(data: list[int | str], num_totals: int = 1) -> int:
    """Returns the solution to part 1 of the day 1 puzzle.

    Parameters
    ----------
    data : list[int | str]
        The input data to process.

    num_totals : int, optional (default: 1)
        The number of max calorie sums to return.

    Returns
    -------
    int:
        The max calorie sum(s).
    """
    sums_list = []
    sum_cals = 0
    for line in data:
        # End of group -> add sum to list:
        if line is None:
            sums_list.append(sum_cals)
            sum_cals = 0
        else:
            sum_cals += line
    # Return first few max sums of the sorted list:
    sums_list.sort(reverse=True)
    return sums_list[:num_totals]


def part2(data: list[int | str]) -> int:
    """Returns the solution to part 2 of the day 1 puzzle. 

    Parameters
    ----------
    data : list[int | str]
        The input data to process.

    Returns
    -------
    int:
        The sum of the top three calorie sums.
    """
    top3_max_sums = part1(data, num_totals=3)
    return sum(top3_max_sums)

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day1.txt")

    print(f" Part 1 Solution: {part1(input_data)[0]} ")
    assert part1(input_data)[0] == 74198

    print(f" Part 2 Solution: {part2(input_data)} ")
    assert part2(input_data) == 209914
