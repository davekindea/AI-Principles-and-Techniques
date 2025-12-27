"""Test path finding with new graph structure"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()

print("Addis Ababa connections:")
for neighbor, cost in graph.get_neighbors("Addis Ababa"):
    print(f"  -> {neighbor} (cost: {cost})")

print("\nTesting path from Addis Ababa to Lalibela:")
ucs = UniformCostSearch(graph)
path, cost, explored = ucs.search("Addis Ababa", "Lalibela")

if path:
    print(f"Path found: {' -> '.join(path)}")
    print(f"Total cost: {cost}")
else:
    print("No path found")
    print(f"Nodes explored: {len(explored)}")

