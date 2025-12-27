"""Check if all goal nodes are reachable"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

goals = ['Axum', 'Gondar', 'Lalibela', 'Babile', 'Jimma', 'Bale', 'Sof Oumer', 'Arba Minch']

print("Checking reachability from Addis Ababa:")
print("=" * 60)
for goal in goals:
    path, cost, _ = ucs.search("Addis Ababa", goal)
    if path:
        print(f"{goal:15s}: Reachable (cost: {cost:3d}, path length: {len(path)-1})")
    else:
        print(f"{goal:15s}: NOT REACHABLE")

