"""Test if UCS finds optimal path"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

# Test Addis Ababa to Lalibela
print("Testing Addis Ababa to Lalibela:")
path, cost, _ = ucs.search("Addis Ababa", "Lalibela")
print(f"Path: {' -> '.join(path)}")
print(f"Cost: {cost}")

# Manually check a known optimal path
print("\nChecking if path is optimal by verifying costs:")
graph_dict = graph.get_graph()
total = 0
for i in range(len(path) - 1):
    neighbors = graph_dict.get(path[i], [])
    for n, c in neighbors:
        if n == path[i + 1]:
            total += c
            print(f"  {path[i]} -> {path[i+1]}: {c}")
            break
print(f"Manual calculation: {total}")
print(f"Algorithm returned: {cost}")
print(f"Match: {total == cost}")

