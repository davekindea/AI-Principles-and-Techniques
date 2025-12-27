"""Test that A* finds optimal path"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question3.astar_search import AStarSearch, create_heuristic_function
from question2.graph_with_costs import create_figure2_graph
from question2.uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
heuristic = create_heuristic_function()
astar = AStarSearch(graph, heuristic)
ucs = UniformCostSearch(graph)

# Test to Awash
print("Testing path from Addis Ababa to Awash:")
print("=" * 60)
path_a, cost_a, _ = astar.search('Addis Ababa', 'Awash')
path_u, cost_u, _ = ucs.search('Addis Ababa', 'Awash')

print(f"A* path: {' -> '.join(path_a)}")
print(f"A* cost: {cost_a}")
print(f"\nUCS path: {' -> '.join(path_u)}")
print(f"UCS cost: {cost_u}")
print(f"\nA* finds optimal: {cost_a == cost_u}")

# Check the path through Batu -> Shashemene
print("\n" + "=" * 60)
print("Checking path: Addis Ababa -> Adama -> Batu -> Shashemene -> Awash")
graph_dict = graph.get_graph()
path_check = ['Addis Ababa', 'Adama', 'Batu', 'Shashemene', 'Awash']
cost_check = 0
for i in range(len(path_check) - 1):
    neighbors = graph_dict.get(path_check[i], [])
    for n, c in neighbors:
        if n == path_check[i + 1]:
            cost_check += c
            print(f"  {path_check[i]} -> {path_check[i+1]}: {c}")
            break
print(f"Total cost: {cost_check}")
print(f"Is this minimum? {cost_check <= cost_a}")

