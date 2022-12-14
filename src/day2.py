"""
    Day 2: Rock Paper Scissors
"""
from helpers.input import get_input_data


def parse_input(filename: str):
    """Retrieves, parses, and formats the input data."""
    # Load input data as list of strings:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # Convert each pair into a tuple:
    lines = map(lambda x: tuple(x.split()), lines)
    return list(lines)


class ScoreCard:
    """An object to store the scores associated with each shape
    and outcome.
    """
    OUTCOMES = {
        "Win": 6,
        "Draw": 3,
        "Lose": 0,
    }
    SHAPES = {
        "Rock": 1,
        "Paper": 2,
        "Scissors": 3,
    }


class ChoiceLegend:
    """An object to store the mapping of choices to shapes based on the
    player / column interpretation.
    """
    OPPONENT = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }
    MYSELF = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }
    OUTCOMES = {
        "X": "Lose",
        "Y": "Draw",
        "Z": "Win",
    }


def determine_outcome(my_choice: str, opp_choice: str) -> str:
    """Determines the outcome of a game of rock-paper-scissors.

    Parameters
    ----------
    my_choice: str
        My choice of shape.

    opp_choice: str
        The opponent's choice of shape.

    Returns
    -------
    str:
        The outcome of the game (Win, Lose, or Draw).
    """
    # Mapping of shapes to points:
    shape_score = ScoreCard.SHAPES
    # Calculate the difference between the shapes:
    diff = shape_score[my_choice] - shape_score[opp_choice]
    # Determine the outcome:
    if diff == 1 or diff == -2:
        return "Win"
    elif diff == 0:
        return "Draw"
    else:
        return "Lose"


def determine_my_choice(outcome: str, opp_choice: str) -> str:
    """Determines my choice of shape based on the outcome of the game.

    Parameters
    ----------
    outcome: str
        The outcome of the game (Win, Lose, or Draw).

    opp_choice: str
        The opponent's choice of shape.

    Returns
    -------
    int:
        The shape score for the shape I must chose to fulfill the outcome.
    """
    # Mapping of shapes to points:
    shape_score = ScoreCard.SHAPES
    # Opponent's shape score:
    oscore = shape_score[opp_choice]
    match outcome:
        case "Draw":
            return oscore
        case "Win":
            return (oscore % 3) + 1
        case "Lose":
            return ((oscore-1) % 3) if oscore > 1 else 3



def part1(data: list[tuple]) -> int:
    """Calculates the sum of all the scores I would have received
    for the hypothetical rock-paper-scissors tournament, assuming
    the rules of the game are as described in part one of the puzzle.

    Parameters
    ----------
    data : list[tuple(str, str)]
        The input data to process.

    Returns
    -------
    int:
        The sum of all points scored by me during the tournament.
    """
    # Mapping of opponent's choices:
    opp_map = ChoiceLegend.OPPONENT
    my_map = ChoiceLegend.MYSELF
    shapes_scores = ScoreCard.SHAPES
    outcomes_scores = ScoreCard.OUTCOMES
    my_total_score = 0
    for opp_choice, my_choice in data:
        # Determine the outcome of the game:
        outcome = determine_outcome(my_map[my_choice], opp_map[opp_choice])
        # Determine the points scored from the outcome and shape I chose:
        scored_pts = outcomes_scores[outcome] + shapes_scores[my_map[my_choice]]
        my_total_score += scored_pts
    return my_total_score



def part2(data: list[tuple]) -> int:
    """Calculates the sum of all the scores I would have received
    for the hypothetical rock-paper-scissors tournament, assuming
    the rules of the game are as described in part two of the puzzle.

    Parameters
    ----------
    data : list[tuple(str, str)]
        The input data to process.

    Returns
    -------
    int:
        The sum of all points scored by me during the tournament.
    """
    opp_map = ChoiceLegend.OPPONENT
    outcome_map = ChoiceLegend.OUTCOMES
    outcome_scores = ScoreCard.OUTCOMES
    my_total_score = 0
    for opp_choice, outcome in data:
        # Map opponent's choice code to shape:
        opp_choice = opp_map[opp_choice]
        # Map outcome code to outcome:
        outcome = outcome_map[outcome]
        # Determine the points scored from the outcome and shape I chose:
        scored_pts = outcome_scores[outcome] + determine_my_choice(outcome, opp_choice)
        my_total_score += scored_pts
    return my_total_score

# ----------------------------------------------------------------------------

if __name__ == "__main__":
    input_data = parse_input("day2.txt")
    # print(f" Input Data: {input_data} ")

    print(f" Part 1 Solution: {part1(input_data)} ")
    assert part1(input_data) == 15632

    print(f" Part 2 Solution: {part2(input_data)} ")
    assert part2(input_data) == 14416
