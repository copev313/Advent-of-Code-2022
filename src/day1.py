"""
    Day 1: Calorie Counting
"""
from aoc.helpers import get_data


def parse_input():
    lines = get_data("day1.txt")
    lines = map(lambda x: x.replace("\n", ""), lines)
    lines = map(lambda x: int(x) if x != "" else x, lines)
    return list(lines)


def part1() -> int:
    lines = parse_input()
    # Max sum & current sum of calories found:
    max_cals, sum_cals = 0, 0

    for line in lines:
        # [CASE] Collect + compare total of group:
        if line == "":
            # Reached the end of the group:
            if sum_cals > max_cals:
                max_cals = sum_cals
                sum_cals = 0
        else:
            # Add calories to sum:
            sum_cals += line

    return max_cals


def part2() -> int:
    lines = parse_input()
    # List of sums of calories:
    sums_list = []
    # Current sum of calories found:
    sum_cals = 0

    for line in lines:
        # [CASE] Collect + compare total of group:
        if line == "":
            # Reached the end of the group:
            sums_list.append(sum_cals)
            sum_cals = 0
        else:
            # Add calories to sum:
            sum_cals += line

    top3_cals = []
    # Fin top 3 totals:
    for _ in range(3):
        max_sum = max(sums_list)
        top3_cals.append(max_sum)
        # Gather index of max sum:
        found_max_index = sums_list.index(max_sum)
        del sums_list[found_max_index]

    return sum(top3_cals)

# ----------------------------------------------------------------------------

if __name__ == "__main__":
    print(f" Part 1 Solution: {part1()} ")
    print(f" Part 2 Solution: {part2()} ")
