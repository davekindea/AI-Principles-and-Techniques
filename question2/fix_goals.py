"""Check and fix connections to reach all goals"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

# Check if we can reach Bahir Dar, Debre Tabor, etc.
intermediate = ['Bahir Dar', 'Debre Tabor', 'Azezo', 'Debarke']
print("Checking intermediate nodes from Addis Ababa:")
for node in intermediate:
    path, cost, _ = ucs.search("Addis Ababa", node)
    print(f"{node}: {'Reachable' if path else 'Not reachable'}")

print("\nChecking if we can reach Gondar from Bahir Dar:")
path, cost, _ = ucs.search("Bahir Dar", "Gondar")
print(f"Gondar from Bahir Dar: {'Reachable' if path else 'Not reachable'}")

print("\nChecking if we can reach Axum from nodes we can reach:")
# Check from Lalibela (we know this is reachable)
path, cost, _ = ucs.search("Lalibela", "Axum")
print(f"Axum from Lalibela: {'Reachable' if path else 'Not reachable'}")

