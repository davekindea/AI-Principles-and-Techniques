"""Check different paths to Awash"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question2.graph_with_costs import create_figure2_graph
from question2.uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
graph_dict = graph.get_graph()
ucs = UniformCostSearch(graph)

# Path 1: Current optimal
path1 = ['Addis Ababa', 'Adama', 'Matahara', 'Awash']
cost1 = 0
print("Path 1: Addis Ababa -> Adama -> Matahara -> Awash")
for i in range(len(path1) - 1):
    neighbors = graph_dict.get(path1[i], [])
    found = False
    for n, c in neighbors:
        if n == path1[i + 1]:
            cost1 += c
            print(f"  {path1[i]} -> {path1[i+1]}: {c}")
            found = True
            break
    if not found:
        print(f"  ERROR: No connection from {path1[i]} to {path1[i+1]}")
print(f"Total cost: {cost1}\n")

# Path 2: Through Batu -> Shashemene
path2 = ['Addis Ababa', 'Adama', 'Batu', 'Shashemene', 'Awash']
cost2 = 0
print("Path 2: Addis Ababa -> Adama -> Batu -> Shashemene -> Awash")
valid = True
for i in range(len(path2) - 1):
    neighbors = graph_dict.get(path2[i], [])
    found = False
    for n, c in neighbors:
        if n == path2[i + 1]:
            cost2 += c
            print(f"  {path2[i]} -> {path2[i+1]}: {c}")
            found = True
            break
    if not found:
        print(f"  ERROR: No connection from {path2[i]} to {path2[i+1]}")
        valid = False

if valid:
    print(f"Total cost: {cost2}")
    print(f"\nPath 2 is {'better' if cost2 < cost1 else 'worse or equal'} than Path 1")
else:
    print("\nPath 2 is not valid - missing connections")

# Check UCS optimal
print("\nUCS optimal path:")
path_ucs, cost_ucs, _ = ucs.search('Addis Ababa', 'Awash')
print(" -> ".join(path_ucs))
print(f"Cost: {cost_ucs}")

