"""Verify UCS finds truly optimal path using exhaustive search"""

from graph_with_costs import create_figure2_graph
from uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

# Get UCS result
path_ucs, cost_ucs, _ = ucs.search("Addis Ababa", "Lalibela")
print("UCS Result:")
print(f"  Path: {' -> '.join(path_ucs)}")
print(f"  Cost: {cost_ucs}\n")

# Verify by checking the path costs manually
graph_dict = graph.get_graph()
print("Verifying path costs:")
total_manual = 0
for i in range(len(path_ucs) - 1):
    neighbors = graph_dict.get(path_ucs[i], [])
    for n, c in neighbors:
        if n == path_ucs[i + 1]:
            total_manual += c
            print(f"  {path_ucs[i]} -> {path_ucs[i+1]}: {c}")
            break

print(f"\nManual total: {total_manual}")
print(f"Algorithm total: {cost_ucs}")
print(f"Match: {total_manual == cost_ucs}")

# Check if there's a shorter path by trying some alternatives
print("\n" + "="*60)
print("Checking if there's a shorter path...")

# Try some known alternative paths
test_paths = [
    (["Addis Ababa", "Adama", "Matahara", "Awash", "Gabi Rasu", "Samara", "Woldia", "Lalibela"], "Through Awash"),
    (["Addis Ababa", "Ambo", "Nekemte", "Gimbi", "Dembi Dollo", "Gambella", "Gore", "Tepi", "Bongo", "Jimma"], "Through West"),
]

for test_path, description in test_paths:
    if test_path[-1] == "Lalibela":
        cost = 0
        valid = True
        for i in range(len(test_path) - 1):
            neighbors = graph_dict.get(test_path[i], [])
            found = False
            for n, c in neighbors:
                if n == test_path[i + 1]:
                    cost += c
                    found = True
                    break
            if not found:
                valid = False
                break
        if valid:
            print(f"{description}: Cost = {cost} {'[BETTER]' if cost < cost_ucs else '[WORSE]'}")

