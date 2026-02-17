"""
Question 3: A* Search algorithm
Given Figure 3 (state space graph with heuristic and backward cost),
write a class that uses A* search to generate a path from "Addis Ababa"
to goal state "Moyale". Uses shared A* algorithm with Figure 3 heuristics.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.search_algorithms import AStarSearch as SharedAStar
from question2.graph_with_costs import GraphWithCosts


class AStarSearch(SharedAStar):
    """A* Search: uses shared A* with heuristic function (Figure 3)."""
    pass


# Import heuristic function from heuristics module
try:
    from question3.heuristics import create_heuristic_function
except ImportError:
    def create_heuristic_function(graph=None):
        def heuristic(node, goal):
            return 0 if node == goal else 30
        return heuristic


def create_distance_heuristic():
    """
    Create a distance-based heuristic if city coordinates are available
    """
    # Sample coordinates (latitude, longitude) - adjust based on actual data
    city_coordinates = {
        "Addis Ababa": (9.1450, 38.7667),
        "Moyale": (3.5167, 39.0583),
        # Add more coordinates as needed
    }
    
    def distance_heuristic(node, goal):
        """Calculate Euclidean distance heuristic"""
        if node == goal:
            return 0
        
        if node not in city_coordinates or goal not in city_coordinates:
            return 1000  # Default large value
        
        from math import sqrt
        lat1, lon1 = city_coordinates[node]
        lat2, lon2 = city_coordinates[goal]
        
        # Approximate distance (simplified)
        return sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) * 100  # Scale factor
    
    return distance_heuristic


if __name__ == "__main__":
    from question2.graph_with_costs import create_figure2_graph

    graph = create_figure2_graph()
    heuristic_func = create_heuristic_function()
    astar = AStarSearch(graph, heuristic_func=heuristic_func)

    print("=" * 60)
    print("Question 3: A* Search Algorithm")
    print("=" * 60)
    initial = "Addis Ababa"
    goal = "Moyale"
    path, total_cost, explored = astar.search(initial, goal)

    if path:
        print(f"\nPath from {initial} to {goal}:")
        print(" -> ".join(path))
        print(f"\nTotal cost (g_score): {total_cost}")
        print(f"Path length: {len(path) - 1} edges")
        print(f"Nodes explored: {len(explored)}")
        graph_dict = graph.get_graph()
        total_verify = 0
        for i in range(len(path) - 1):
            for n, c in graph_dict.get(path[i], []):
                if n == path[i + 1]:
                    total_verify += c
                    print(f"  {path[i]} -> {path[i+1]}: {c}")
                    break
        print(f"Total verified: {total_verify}")
    else:
        print(f"\nNo path found from {initial} to {goal}")
        print(f"Nodes explored: {len(explored)}")

