"""
    Day 3: Rucksack Reorganization
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



def get_letter_value(x: str) -> int:
    """Returns the value of a letter in the alphabet. Lowercase letters a-z
    score 1-26. Uppercase letters A-Z score 27-52.

    Parameters
    ----------
    x: str
        The letter to score.

    Returns
    -------
    int:
        The value of the letter.
    """
    import string
    letters = list(string.ascii_letters)
    return letters.index(x) + 1


def part1(data: list[str]) -> int:
    """Returns the solution to part 1 of the puzzle.

    Parameters
    ----------
    data : list[str]
        The input data to process.

    Returns
    -------
    int:
        The sum of the priority scores from each rutsack.
    """
    # Split in half & convert each string to a tuple:
    def split_in_half(x: str) -> tuple[str, str]:
        half = len(x) // 2
        return (x[:half], x[half:])

    lines = list(map(split_in_half, data))
    priorities_sum = 0

    for comp_one, comp_two in lines:
        # Convert each component to a set:
        set_one, set_two = set(comp_one), set(comp_two)
        # Find the intersection of the two sets:
        common_type = set_one.intersection(set_two)
        # Find the values of the common letter:
        priorities_sum += get_letter_value(list(common_type)[0])

    return priorities_sum



def part2(data: list[str]) -> int:
    """Returns the solution to part 2 of the puzzle. 

    Parameters
    ----------
    data : list[str]
        The input data to process.

    Returns
    -------
    int:
        The sum of the priority scores of each item type of each 
        three-Elf group.
    """
    # Create tuples of three:
    grouped_data = []
    group = tuple()
    for line in data:
        group = group + (line,)
        # [CASE] Full group of three:
        if len(group) == 3:
            grouped_data.append(group)
            group = tuple()

    priorities_sum = 0
    for one, two, three in grouped_data:
        set_one, set_two, set_three = set(one), set(two), set(three)
        common = set_one & set_two & set_three
        priorities_sum += get_letter_value(list(common)[0])

    return priorities_sum

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day3.txt")

    print(f" Part 1 Solution: {part1(input_data)} ")
    assert part1(input_data) == 8243

    print(f" Part 2 Solution: {part2(input_data)} ")
    assert part2(input_data) == 2631
