"""
    Day 6: Tuning Trouble
"""
from helpers.input import get_input_data


def parse_input(filename: str) -> str:
    """Retrieves, parses, and formats the input data. """
    # Load input data as list of strings:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # Convert to list:
    return list(lines)[0]



def part1(data: list[str]) -> int:
    """Returns the solution to part 1 of the puzzle. """
    # Convert input data to list of letters:
    for i in range(len(data)):
        # Gather a substring of the last four letters:
        marker = data[i: i + 4]
        # Convert to substring to a set of letters:
        marker_set = set(list(marker))
        # [CASE] We have a marker of four unique letters:
        if len(marker_set) == 4:
            print(f" {marker} ")
            return i + 4



def part2(data: list[str]) -> int:
    """Returns the solution to part 2 of the puzzle. """
    # Convert input data to list of letters:
    for i in range(len(data)):
        # Gather a substring of the last four letters:
        marker = data[i: i + 14]
        # Convert to substring to a set of letters:
        marker_set = set(list(marker))
        # [CASE] We have a marker of four unique letters:
        if len(marker_set) == 14:
            print(f" {marker} ")
            return i + 14


# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day6.txt")

    part1_solution = part1(input_data)
    print(f" Part 1 Solution: {part1_solution} ")
    assert part1_solution == 1343

    part2_solution = part2(input_data)
    print(f" Part 2 Solution: {part2_solution} ")
    assert part2_solution == 2193
