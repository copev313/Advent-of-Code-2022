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


INITIAL_STACK_STATE = [
    ["D", "T", "W", "F", "J", "S", "H", "N"],
    ["H", "R", "P", "Q", "T", "N", "B", "G"],
    ["L", "Q", "V"],
    ["N", "B", "S", "W", "R", "Q"],
    ["N", "D", "F", "T", "V", "M", "B"],
    ["M", "D", "B", "V", "H", "T", "R"],
    ["D", "B", "Q", "J"],
    ["D", "N", "J", "V", "R", "Z", "H", "Q"],
    ["B", "N", "H", "M", "S"],
]


class Stack:
    """A traditional Last-In-First-Out stack data structure. """

    def __init__(self, name: str | int):
        self.name = name
        self.stack = []

    def __repr__(self) -> str:
        return f"{self.name}: {self.stack}"

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


    def clear(self):
        """Removes all items from the stack. """
        self.stack = []


    def move(self, qty: int, to_stk):
        """Moves the specified number of items incrementally from the top of
        the stack to the specified stack. 
        
        Parameters
        ----------
        qty : int
            The number of times to move an item.
        
        to_stk : Stack
            The stack to move the items to.
        """
        for _ in range(qty):
            element = self.pop()
            to_stk.push(element)


    def move_group(self, qty: int, to_stk):
        """Moves the specified number of items from the top of the stack to
        the specified stack, in the same grouped order. 
        
        Parameters
        ----------
        qty : int
            The number of items to move.
        
        to_stk : Stack
            The stack to move the items to.
        """
        # Gather the group of items to move:
        grouped_elements = self.stack[-qty:]
        # Remove the items from the stack:
        for _ in range(qty):
            self.pop()
        # Add the items to the specified stack:
        to_stk.stack.extend(grouped_elements)


    def peek(self) -> str | int:
        """Returns the top item from the stack without removing it. """
        if not self.is_empty:
            return self.stack[-1]



def setup_stacks(initial_state: list[list]) -> list[Stack]:
    """Returns a list of stacks with the specified initial state. 
    
    Parameters
    ----------
    initial_state : list[list]
        A list of lists containing the initial state of each stack.
    
    Returns
    -------
    list[Stack]:
        A list of stacks with the specified initial state.
    """
    # Create a tuple of stacks:
    stacks = list()
    for num in range(1, len(initial_state) + 1):
        stacks += (Stack(str(num)), )
    # Set the initial state of each stack:
    for num, stk in enumerate(stacks):
        stk.stack = initial_state[num].copy()
    return stacks



def part1(data: list[tuple]) -> str:
    """Returns the solution to part 1 of the puzzle.

    Parameters
    ----------
    data : list[tuple]
        The input data to process.

    Returns
    -------
    str:
        The top element of each stack.
    """
    cutoff_index = data.index("") + 1
    data = data[cutoff_index:]
    # Setup the stacks:
    stacks = setup_stacks(INITIAL_STACK_STATE)

    for line in data:
        # Split on spaces & unpack into variables:
        _, qty, _, from_stk, _, to_stk = tuple(line.split(" "))
        # Get the corresponding stack objects:
        from_stk, to_stk = stacks[int(from_stk) - 1], stacks[int(to_stk) - 1]
        # Perform the move operation the specified number of times:
        from_stk.move(int(qty), to_stk)

    # Return the top element of each stack:
    top_elements = ""
    for stack in stacks:
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
    str:
        The top element of each stack.
    """
    cutoff_index = data.index("") + 1
    data = data[cutoff_index:]
    # Setup the stacks:
    stacks = setup_stacks(INITIAL_STACK_STATE)

    for line in data:
        # Split on spaces & unpack into variables:
        _, qty, _, from_stk, _, to_stk = tuple(line.split(" "))
        # Get the corresponding stack objects:
        from_stk, to_stk = stacks[int(from_stk) - 1], stacks[int(to_stk) - 1]
        # Use the move group operation to the specified number of elements:
        from_stk.move_group(int(qty), to_stk)

    # Return the top element of each stack:
    top_elements = ""
    for stack in stacks:
        top_elements += stack.peek()
    return top_elements

# ----------------------------------------------------------------------------

if __name__ == "__main__":

    input_data = parse_input("day5.txt")

    part1_solution = part1(input_data)
    print(f" Part 1 Solution: {part1_solution} ")
    assert part1_solution == "GRTSWNJHH"

    part2_solution = part2(input_data)
    print(f" Part 2 Solution: {part2_solution} ")
    assert part2_solution == "QLFQDBBHM"
