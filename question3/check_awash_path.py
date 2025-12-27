"""Check different paths to Awash"""

from question2.graph_with_costs import create_figure2_graph
from question2.uniform_cost_search import UniformCostSearch

graph = create_figure2_graph()
ucs = UniformCostSearch(graph)

# Check UCS optimal path
path1, cost1, _ = ucs.search('Addis Ababa', 'Awash')
print("UCS optimal path:")
print(" -> ".join(path1))
print(f"Cost: {cost1}\n")

# Check path through Adama -> Batu -> Shashemene -> Awash
graph_dict = graph.get_graph()
path2 = ['Addis Ababa', 'Adama', 'Batu', 'Shashemene', 'Awash']
cost2 = 0
valid = True

print("Checking path: Addis Ababa -> Adama -> Batu -> Shashemene -> Awash")
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
        break

if valid:
    print(f"Total cost: {cost2}")
    print(f"Is this minimum? {cost2 <= cost1}")

