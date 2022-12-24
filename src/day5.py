"""
    Day 5: Supply Stacks
"""
from helpers.input import get_input_data


def parse_input(filename: str) -> list[tuple]:
    """Retrieves, parses, and formats the input data. """
    # Load input data as list of strings:
    lines = get_input_data(filename)
    # Remove newline characters:
    lines = map(lambda x: x.replace("\n", ""), lines)
    # Convert to list:
    return list(lines)



class Stack:
    """A traditional stack data structure. (LIFO) """
    
    def __init__(self, name: str | int):
        self.name = name
        self.stack = []

    @property
    def size(self) -> int:
        return len(self.stack)

    @property
    def is_empty(self) -> bool:
        """Returns True if the stack is empty. """
        return self.size == 0


    def push(self, item: str | int):
        """Adds an item to the top of the stack. """
        self.stack.append(item)


    def pop(self) -> str | int:
        """Removes and returns the top item from the stack. """
        if not self.is_empty:
            return self.stack.pop()


    def peek(self) -> str | int:
        """Returns the top item from the stack without removing it. """
        if self.is_empty:
            return ""
        return self.stack[-1]


def get_stack_by_name(name: str, stacks: list[Stack]) -> Stack:
    """Returns the stack with the specified name. """
    for stack in stacks:
        if stack.name == name:
            return stack
    raise ValueError(f"Stack with name {name} not found. ")


def part1(data: list[tuple]) -> int:
    """Returns the solution to part 1 of the puzzle.

    Parameters
    ----------
    data : list[tuple]
        The input data to process.

    Returns
    -------
    int:
        
    """
    cutoff_index = data.index("") + 1
    data = data[cutoff_index:]
    s1 = Stack("1")
    s2 = Stack("2")
    s3 = Stack("3")
    s4 = Stack("4")
    s5 = Stack("5")
    s6 = Stack("6")
    s7 = Stack("7")
    s8 = Stack("8")
    s9 = Stack("9")
    stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]

    def setup_stacks():
        s1.stack = ["D", "T", "W", "F", "J", "S", "H", "N"]
        s2.stack = ["H", "R", "P", "Q", "T", "N", "B", "G"]
        s3.stack = ["L", "Q", "V"]
        s4.stack = ["N", "B", "S", "W", "R", "Q"]
        s5.stack = ["N", "D", "F", "T", "V", "M", "B"]
        s6.stack = ["M", "D", "B", "V", "H", "T", "R"]
        s7.stack = ["D", "B", "Q", "J"]
        s8.stack = ["D", "N", "J", "V", "R", "Z", "H", "Q"]
        s9.stack = ["B", "N", "H", "M", "S"]

    setup_stacks()

    for line in data:
        # Split on spaces & unpack into variables:
        _, qty, _, from_stack, _, to_stack = tuple(line.split(" "))

        from_stack = get_stack_by_name(from_stack, stacks)
        to_stack = get_stack_by_name(to_stack, stacks)
        # Perform the move operation the specified number of times:
        for _ in range(int(qty)):
            element = from_stack.pop()
            to_stack.push(element)

    # Print the top element of each stack:
    top_elements = ""
    for stack in [s1, s2, s3, s4, s5, s6, s7, s8, s9]:
        top_elements += stack.peek()
    
    return top_elements



def part2(data: list[tuple]) -> int:
    """Returns the solution to part 2 of the puzzle. 

    Parameters
    ----------
    data : list[tuple]
        The input data to process.

    Returns
    -------
    int:
        
    """
    pass

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day5.txt")

    print(f" Part 1 Solution: {part1(input_data)} ")
    assert part1(input_data) == "GRTSWNJHH"

    # print(f" Part 2 Solution: {part2(input_data)} ")
    # assert part2(input_data) == 870
