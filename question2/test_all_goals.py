"""Test if we can reach all goals from different positions"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

goals = ['Axum', 'Gondar', 'Lalibela', 'Jimma', 'Arba Minch']
positions = ['Babile', 'Addis Ababa', 'Bale']

for pos in positions:
    print(f"\nFrom {pos}:")
    for goal in goals:
        path, cost, _ = ucs.search(pos, goal)
        print(f"  {goal}: {'Reachable' if path else 'Not reachable'}")

