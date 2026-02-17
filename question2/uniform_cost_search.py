"""
Question 2.2: Uniform Cost Search algorithm
Assuming "Addis Ababa" as initial state, generate a path to "Lalibela".
Uses shared UCS algorithm with Figure 2 graph (costs).
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.search_algorithms import UniformCostSearch as SharedUCS
from question2.graph_with_costs import GraphWithCosts, create_figure2_graph


# Re-export for tests and multi_goal_ucs that import UniformCostSearch from here
class UniformCostSearch(SharedUCS):
    """Uniform Cost Search: uses shared UCS on graph with costs (Figure 2)."""
    pass


if __name__ == "__main__":
    graph = create_figure2_graph()
    ucs = UniformCostSearch(graph)
    print("=" * 60)
    print("Question 2.2: Uniform Cost Search (UCS)")
    print("=" * 60)
    initial = "Addis Ababa"
    goal = "Lalibela"
    path, total_cost, explored = ucs.search(initial, goal)
    if path:
        print(f"\nPath from {initial} to {goal}:")
        print(" -> ".join(path))
        print(f"\nTotal cost: {total_cost}")
        print(f"Path length: {len(path) - 1} edges")
        print(f"Nodes explored: {len(explored)}")
    else:
        print(f"\nNo path found from {initial} to {goal}")
        print(f"Nodes explored: {len(explored)}")
