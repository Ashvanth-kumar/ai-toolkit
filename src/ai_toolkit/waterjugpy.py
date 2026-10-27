
from collections import deque
from math import gcd


class State:
    """Represents the amount of water in two jugs."""

    def __init__(self, x, y, parent=None, move=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.move = move

    def key(self):
        """Return a unique representation of this state."""
        return self.x, self.y

    def is_goal(self, target):
        """Check whether either jug contains the target amount."""
        return self.x == target or self.y == target

    def generate_next_states(self, capacity_x, capacity_y):
        """Generate all possible water-jug operations."""
        next_states = []

        # Fill jug X.
        next_states.append(
            State(capacity_x, self.y, self, "Fill jug X")
        )

        # Fill jug Y.
        next_states.append(
            State(self.x, capacity_y, self, "Fill jug Y")
        )

        # Empty jug X.
        next_states.append(State(0, self.y, self, "Empty jug X"))

        # Empty jug Y.
        next_states.append(State(self.x, 0, self, "Empty jug Y"))

        # Pour water from X into Y.
        amount = min(self.x, capacity_y - self.y)
        next_states.append(
            State(
                self.x - amount,
                self.y + amount,
                self,
                f"Pour {amount} unit(s) from X to Y",
            )
        )

        # Pour water from Y into X.
        amount = min(self.y, capacity_x - self.x)
        next_states.append(
            State(
                self.x + amount,
                self.y - amount,
                self,
                f"Pour {amount} unit(s) from Y to X",
            )
        )

        # Remove transitions that do not change the state.
        unique_states = []
        seen = set()

        for state in next_states:
            if state.key() != self.key() and state.key() not in seen:
                unique_states.append(state)
                seen.add(state.key())

        return unique_states

    def get_path(self):
        """Reconstruct the solution path."""
        path = []
        current = self

        while current.parent is not None:
            path.append(current)
            current = current.parent

        path.reverse()
        return path


def solve_water_jug(capacity_x, capacity_y, target_z):
    """
    Solve the Water Jug problem using BFS.

    Returns:
        A list of states representing the solution, or None if unsolvable.
    """
    values = (capacity_x, capacity_y, target_z)

    if any(
        not isinstance(value, int) or isinstance(value, bool)
        for value in values
    ):
        raise TypeError("Jug capacities and target must be integers.")

    if capacity_x <= 0 or capacity_y <= 0:
        raise ValueError("Jug capacities must be positive.")

    if target_z < 0:
        raise ValueError("The target cannot be negative.")

    if target_z == 0:
        return []

    if target_z > max(capacity_x, capacity_y):
        return None

    if target_z % gcd(capacity_x, capacity_y) != 0:
        return None

    initial_state = State(0, 0)
    queue = deque([initial_state])
    visited = {initial_state.key()}

    while queue:
        current = queue.popleft()

        if current.is_goal(target_z):
            return current.get_path()

        for next_state in current.generate_next_states(
            capacity_x, capacity_y
        ):
            key = next_state.key()

            if key not in visited:
                visited.add(key)
                queue.append(next_state)

    return None


def main():
    """Run the Water Jug demonstration interactively."""
    print("Water Jug Problem")
    print("-" * 40)

    try:
        capacity_x = int(input("Enter capacity of jug X: "))
        capacity_y = int(input("Enter capacity of jug Y: "))
        target_z = int(input("Enter target amount: "))

        solution = solve_water_jug(
            capacity_x,
            capacity_y,
            target_z,
        )

        if solution is None:
            print("No solution exists for the given capacities and target.")
            return

        print(f"\nSolution found in {len(solution)} operations.")

        x, y = 0, 0
        print(f"Initial state: X={x}, Y={y}")

        for step, state in enumerate(solution, start=1):
            x, y = state.x, state.y
            print(f"Step {step}: {state.move}")
            print(f"  Current state: X={x}, Y={y}")

    except ValueError as error:
        print(f"Invalid input: {error}")


if __name__ == "__main__":
    main()
