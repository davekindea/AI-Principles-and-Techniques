"""Find all possible paths to verify optimality"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

# Test multiple paths
print("Testing different paths from Addis Ababa to Lalibela:")
print("=" * 60)

# Get UCS result
path_ucs, cost_ucs, _ = ucs.search("Addis Ababa", "Lalibela")
print(f"UCS path: {' -> '.join(path_ucs)}")
print(f"UCS cost: {cost_ucs}")

# Manually check some alternative paths
graph_dict = graph.get_graph()
alternative_paths = [
    ["Addis Ababa", "Adama", "Matahara", "Awash", "Gabi Rasu", "Samara", "Woldia", "Lalibela"],
    ["Addis Ababa", "Ambo", "Wolkite", "Hossana", "Wolaita Sodo", "Arba Minch", "Konso", "Yabello", "Moyale"],
]

print("\nChecking alternative paths:")
for alt_path in alternative_paths:
    if alt_path[-1] == "Lalibela":
        cost = 0
        valid = True
        for i in range(len(alt_path) - 1):
            neighbors = graph_dict.get(alt_path[i], [])
            found = False
            for n, c in neighbors:
                if n == alt_path[i + 1]:
                    cost += c
                    found = True
                    break
            if not found:
                valid = False
                break
        if valid:
            print(f"  Path: {' -> '.join(alt_path)}")
            print(f"  Cost: {cost}")
            print(f"  {'Better' if cost < cost_ucs else 'Worse or equal'} than UCS")

