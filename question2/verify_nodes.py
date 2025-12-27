"""Verify all nodes are included in the graph"""

from graph_with_costs import create_figure2_graph
import json

# Load extracted data
with open('extracted_graph_data.json', 'r', encoding='utf-8') as f:
    extracted_data = json.load(f)

# Get graph
graph = create_figure2_graph()
graph_dict = graph.get_graph()

# Get all nodes from graph (including destinations)
all_graph_nodes = set()
for node, neighbors in graph_dict.items():
    all_graph_nodes.add(node)
    for neighbor, _ in neighbors:
        all_graph_nodes.add(neighbor)

# Get extracted nodes
extracted_nodes = set(extracted_data['nodes'])

print("=" * 70)
print("Node Verification")
print("=" * 70)
print(f"Nodes in extracted data: {len(extracted_nodes)}")
print(f"Nodes in graph (all, including destinations): {len(all_graph_nodes)}")
print(f"Nodes with outgoing edges: {len(graph_dict)}")

missing = sorted(extracted_nodes - all_graph_nodes)
extra = sorted(all_graph_nodes - extracted_nodes)

if missing:
    print(f"\nMissing nodes ({len(missing)}): {missing}")
else:
    print("\n[OK] All extracted nodes are in the graph!")

if extra:
    print(f"\nExtra nodes in graph ({len(extra)}): {extra}")

print("\n" + "=" * 70)

