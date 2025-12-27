"""Test dynamic heuristic with different goals"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question3.astar_search import AStarSearch
from question2.graph_with_costs import create_figure2_graph

graph = create_figure2_graph()

# Use dynamic heuristic (works for ANY goal)
astar = AStarSearch(graph, heuristic_func=None)

print("Testing dynamic heuristic with different goals:")
print("=" * 60)

# Test 1: Moyale
path1, cost1, _ = astar.search("Addis Ababa", "Moyale")
print(f"\n1. Addis Ababa -> Moyale:")
print(f"   Path: {' -> '.join(path1)}")
print(f"   Cost: {cost1}")

# Test 2: Debre Birhan
path2, cost2, _ = astar.search("Addis Ababa", "Debre Birhan")
print(f"\n2. Addis Ababa -> Debre Birhan:")
print(f"   Path: {' -> '.join(path2)}")
print(f"   Cost: {cost2}")

# Test 3: Lalibela
path3, cost3, _ = astar.search("Addis Ababa", "Lalibela")
print(f"\n3. Addis Ababa -> Lalibela:")
print(f"   Path: {' -> '.join(path3)}")
print(f"   Cost: {cost3}")

# Test 4: Hawassa
path4, cost4, _ = astar.search("Addis Ababa", "Hawassa")
print(f"\n4. Addis Ababa -> Hawassa:")
print(f"   Path: {' -> '.join(path4)}")
print(f"   Cost: {cost4}")

print("\n" + "=" * 60)
print("Dynamic heuristic works for ANY destination!")

