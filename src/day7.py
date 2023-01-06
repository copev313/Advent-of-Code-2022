"""
    Day 7: No Space Left On Device
"""
from helpers.input import get_input_data


def parse_input(filename: str) -> list[str]:
    """Retrieves, parses, and formats the input data. """
    # Load input data as list of strings:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # Convert to list:
    return list(lines)



def part1(data: list[str]) -> int:
    """Returns the solution to part 1 of the puzzle. """
    pass



def part2(data: list[str]) -> int:
    """Returns the solution to part 2 of the puzzle. """
    pass


# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day7.txt")

    # part1_solution = part1(input_data)
    # print(f" Part 1 Solution: {part1_solution} ")
    # assert part1_solution == 0

    # part2_solution = part2(input_data)
    # print(f" Part 2 Solution: {part2_solution} ")
    # assert part2_solution == 0
