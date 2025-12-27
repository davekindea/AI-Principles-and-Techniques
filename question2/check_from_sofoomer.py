"""Check reachability from Sof Oumer"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

goals = ['Axum', 'Gondar', 'Lalibela', 'Babile', 'Jimma', 'Arba Minch']
print("Checking reachability from Sof Oumer:")
for goal in goals:
    path, cost, _ = ucs.search("Sof Oumer", goal)
    print(f"{goal}: {'Reachable' if path else 'Not reachable'}")

print("\nChecking reachability from Bale:")
for goal in goals:
    path, cost, _ = ucs.search("Bale", goal)
    print(f"{goal}: {'Reachable' if path else 'Not reachable'}")

