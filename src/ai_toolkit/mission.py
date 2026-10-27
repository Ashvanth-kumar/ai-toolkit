
from collections import deque


class State:
    """Represents a state of the Missionaries and Cannibals problem."""

    def __init__(
        self,
        missionaries_left,
        cannibals_left,
        boat_left,
        missionaries_right,
        cannibals_right,
        parent=None,
        move=None,
    ):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right
        self.parent = parent
        self.move = move

    def key(self):
        """Return a unique representation of this state."""
        return (
            self.missionaries_left,
            self.cannibals_left,
            self.boat_left,
            self.missionaries_right,
            self.cannibals_right,
        )

    def is_valid(self):
        """Check whether the state follows the problem constraints."""
        values = (
            self.missionaries_left,
            self.cannibals_left,
            self.missionaries_right,
            self.cannibals_right,
        )

        if any(value < 0 or value > 3 for value in values):
            return False

        if self.missionaries_left > 0:
            if self.missionaries_left < self.cannibals_left:
                return False

        if self.missionaries_right > 0:
            if self.missionaries_right < self.cannibals_right:
                return False

        return True

    def is_goal(self):
        """Check whether everyone has crossed to the right bank."""
        return (
            self.missionaries_left == 0
            and self.cannibals_left == 0
            and self.boat_left == 0
        )

    def generate_next_states(self):
        """Generate all valid states reachable in one boat crossing."""
        moves = [
            (1, 0),
            (2, 0),
            (0, 1),
            (0, 2),
            (1, 1),
        ]

        next_states = []

        for missionaries, cannibals in moves:
            if self.boat_left:
                # Move from left bank to right bank.
                new_state = State(
                    self.missionaries_left - missionaries,
                    self.cannibals_left - cannibals,
                    0,
                    self.missionaries_right + missionaries,
                    self.cannibals_right + cannibals,
                    self,
                    f"{missionaries} missionary(s), "
                    f"{cannibals} cannibal(s): Left -> Right",
                )
            else:
                # Move from right bank to left bank.
                new_state = State(
                    self.missionaries_left + missionaries,
                    self.cannibals_left + cannibals,
                    1,
                    self.missionaries_right - missionaries,
                    self.cannibals_right - cannibals,
                    self,
                    f"{missionaries} missionary(s), "
                    f"{cannibals} cannibal(s): Right -> Left",
                )

            if new_state.is_valid():
                next_states.append(new_state)

        return next_states

    def get_path(self):
        """Reconstruct the solution path from the initial state."""
        path = []
        current = self

        while current.parent is not None:
            path.append(current)
            current = current.parent

        path.reverse()
        return path


def solve_missionaries_and_cannibals(start_left=True):
    """
    Solve the problem using Breadth-First Search (BFS).

    Returns:
        A list of states representing the solution, or None if unsolvable.
    """
    if not isinstance(start_left, bool):
        raise TypeError("start_left must be a boolean.")

    if start_left:
        initial_state = State(3, 3, 1, 0, 0)
    else:
        initial_state = State(0, 0, 0, 3, 3)

    queue = deque([initial_state])
    visited = {initial_state.key()}

    while queue:
        current = queue.popleft()

        if current.is_goal():
            return current.get_path()

        for next_state in current.generate_next_states():
            key = next_state.key()

            if key not in visited:
                visited.add(key)
                queue.append(next_state)

    return None


def main():
    """Run the Missionaries and Cannibals demonstration."""
    print("Missionaries and Cannibals Problem")
    print("-" * 40)

    solution = solve_missionaries_and_cannibals()

    if solution is None:
        print("No solution found.")
        return

    print("Initial state: 3 missionaries and 3 cannibals on the left bank.")
    print(f"Solution found in {len(solution)} crossings.\n")

    for step, state in enumerate(solution, start=1):
        print(f"Step {step}: {state.move}")
        print(
            f"  Left bank:  M={state.missionaries_left}, "
            f"C={state.cannibals_left}"
        )
        print(
            f"  Right bank: M={state.missionaries_right}, "
            f"C={state.cannibals_right}"
        )


if __name__ == "__main__":
    main()
