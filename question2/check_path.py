"""Check if there's a path from Addis Ababa to Lalibela"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

print("Checking path from Addis Ababa to Lalibela...")
print("\nAddis Ababa connections:")
for neighbor, cost in graph.get_neighbors("Addis Ababa"):
    print(f"  -> {neighbor} (cost: {cost})")

print("\nNodes that connect to Lalibela:")
graph_dict = graph.get_graph()
for node, neighbors in graph_dict.items():
    for neighbor, cost in neighbors:
        if neighbor == "Lalibela":
            print(f"  {node} -> Lalibela (cost: {cost})")

print("\n" + "="*60)
path, total_cost, explored = ucs.search("Addis Ababa", "Lalibela")

if path:
    print(f"\n✓ Path found!")
    print(f"Path: {' -> '.join(path)}")
    print(f"Total cost: {total_cost}")
    print(f"Nodes explored: {len(explored)}")
else:
    print(f"\n[X] No path found")
    print(f"Nodes explored: {len(explored)}")
    print(f"Last few explored: {explored[-10:] if len(explored) > 10 else explored}")

