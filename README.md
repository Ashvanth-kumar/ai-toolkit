
# AI Toolkit

A Python library implementing classic Artificial Intelligence search
algorithms using Breadth-First Search (BFS).

## Algorithms

### 1. Missionaries and Cannibals
Finds a sequence of valid boat crossings to transport three missionaries
and three cannibals safely across a river.

### 2. Water Jug Problem
Finds a sequence of operations to measure a target amount of water
using two jugs of specified capacities.

## Installation

```bash
pip install ai-toolkit-Anonymous
```

## Usage

```python
from ai_toolkit import (
    solve_missionaries_and_cannibals,
    solve_water_jug,
)

# Missionaries and Cannibals
solution = solve_missionaries_and_cannibals()
print(solution)

# Water Jug: jug capacities are 4 and 3, target is 2
solution = solve_water_jug(4, 3, 2)
print(solution)
```

## Run the Algorithms Locally

```bash
python -m src.ai_toolkit.misson
python -m src.ai_toolkit.waterjugpy
```

## License

This project is licensed under the MIT License.
