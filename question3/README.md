# Question 3: A* Search Algorithm

## Overview
This implementation uses A* search to find the optimal path from "Addis Ababa" to "Moyale" using heuristic values.

## Files
- `astar_search.py`: Main A* search implementation
- `heuristics.py`: Heuristic values for all cities (estimated cost to Moyale)
- `test_question3.py`: Test script

## Optimal Path
**From Addis Ababa to Moyale:**
- Path: Addis Ababa → Adama → Batu → Shashemene → Hawassa → Dilla → Bule Hora → Yabello → Moyale
- **Total Cost: 27**
- Cost breakdown:
  - Addis Ababa → Adama: 3
  - Adama → Batu: 4
  - Batu → Shashemene: 3
  - Shashemene → Hawassa: 1
  - Hawassa → Dilla: 3
  - Dilla → Bule Hora: 4
  - Bule Hora → Yabello: 3
  - Yabello → Moyale: 6

## Heuristic Values
The heuristic values are based on the provided path data and represent the estimated remaining cost from each node to the goal (Moyale). The heuristic is **admissible** (never overestimates) and **consistent**, ensuring A* finds the optimal path.

## Performance
- **Nodes explored**: ~14 (much better than UCS which explored 43-46 nodes)
- **Optimality**: Guaranteed (heuristic is admissible)
- **Completeness**: Guaranteed (if a path exists, A* will find it)

## Usage
```python
from question3.astar_search import AStarSearch, create_heuristic_function
from question2.graph_with_costs import create_figure2_graph

graph = create_figure2_graph()
heuristic_func = create_heuristic_function()
astar = AStarSearch(graph, heuristic_func)

path, cost, explored = astar.search("Addis Ababa", "Moyale")
```

