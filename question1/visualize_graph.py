"""
Visualize the state space graph from Figure 1
"""

import sys
import os

# Try to import visualization libraries
try:
    import matplotlib.pyplot as plt
    import networkx as nx
    HAS_VISUALIZATION = True
except ImportError:
    HAS_VISUALIZATION = False
    print("Visualization libraries not found. Installing...")
    print("Please run: pip install matplotlib networkx")

from graph_converter import create_figure1_graph


def visualize_graph():
    """Create a visual representation of the graph"""
    if not HAS_VISUALIZATION:
        print("\nCreating text-based representation instead...")
        create_text_representation()
        return
    
    # Create graph
    converter = create_figure1_graph()
    graph_dict = converter.get_graph()
    
    # Create NetworkX graph
    G = nx.Graph()
    
    # Add nodes and edges
    for node, neighbors in graph_dict.items():
        G.add_node(node)
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
    
    print(f"\nGraph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges")
    
    # Try different layout algorithms
    print("\nGenerating visualization...")
    
    # Use spring layout for better visualization
    try:
        pos = nx.spring_layout(G, k=2, iterations=50, seed=42)
    except:
        pos = nx.spring_layout(G, seed=42)
    
    # Create figure
    plt.figure(figsize=(20, 16))
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=300, alpha=0.9)
    
    # Draw edges
    nx.draw_networkx_edges(G, pos, alpha=0.5, width=0.5, edge_color='gray')
    
    # Draw labels (only for important nodes to avoid clutter)
    important_nodes = ["Addis Ababa", "Moyale", "Gondar", "Lalibela", 
                       "Axum", "Bahir Dar", "Jimma", "Hawassa", 
                       "Arba Minch", "Dire Dawa", "Harar"]
    
    labels = {node: node for node in important_nodes if node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold')
    
    # Draw all labels (smaller font)
    all_labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, all_labels, font_size=6, alpha=0.7)
    
    plt.title("Traveling Ethiopia Search Problem - State Space Graph", 
              fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    
    # Save figure
    output_file = "question1/graph_visualization.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n[OK] Graph visualization saved to: {output_file}")
    
    # Also create a simpler version with just connections
    create_simple_visualization(G, pos)
    
    # Print graph statistics
    print_graph_statistics(G)


def create_simple_visualization(G, pos):
    """Create a simpler visualization with just nodes and edges"""
    plt.figure(figsize=(20, 16))
    
    nx.draw_networkx_nodes(G, pos, node_color='lightcoral', 
                          node_size=200, alpha=0.8)
    nx.draw_networkx_edges(G, pos, alpha=0.3, width=0.3, edge_color='black')
    
    plt.title("Traveling Ethiopia - Simplified Graph View", fontsize=16)
    plt.axis('off')
    plt.tight_layout()
    
    output_file = "question1/graph_simple.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"[OK] Simple graph visualization saved to: {output_file}")


def create_text_representation():
    """Create a text-based representation of the graph"""
    converter = create_figure1_graph()
    graph_dict = converter.get_graph()
    
    print("\n" + "="*70)
    print("TEXT-BASED GRAPH REPRESENTATION")
    print("="*70)
    print(f"\nTotal Nodes: {len(graph_dict)}")
    print(f"Total Edges: {sum(len(neighbors) for neighbors in graph_dict.values()) // 2}")
    
    print("\n" + "-"*70)
    print("ADJACENCY LIST (All Nodes and Their Connections):")
    print("-"*70)
    
    for node in sorted(graph_dict.keys()):
        neighbors = sorted(graph_dict[node])
        print(f"\n{node}:")
        print(f"  -> {', '.join(neighbors)}")
        print(f"  (Degree: {len(neighbors)})")
    
    # Create DOT format for Graphviz
    print("\n" + "="*70)
    print("GRAPHVIZ DOT FORMAT (can be used with Graphviz):")
    print("="*70)
    print("\ngraph TravelingEthiopia {")
    print("  rankdir=LR;")
    print("  node [shape=circle];")
    
    edges_printed = set()
    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            edge = tuple(sorted([node, neighbor]))
            if edge not in edges_printed:
                print(f'  "{node}" -- "{neighbor}";')
                edges_printed.add(edge)
    
    print("}")


def print_graph_statistics(G):
    """Print statistics about the graph"""
    print("\n" + "="*70)
    print("GRAPH STATISTICS")
    print("="*70)
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Number of connected components: {nx.number_connected_components(G)}")
    
    if nx.is_connected(G):
        print(f"Graph is connected: Yes")
        print(f"Diameter: {nx.diameter(G)}")
        print(f"Average path length: {nx.average_shortest_path_length(G):.2f}")
    else:
        print(f"Graph is connected: No")
        print(f"Largest component size: {len(max(nx.connected_components(G), key=len))}")
    
    degrees = dict(G.degree())
    print(f"\nNode degrees:")
    print(f"  Maximum degree: {max(degrees.values())}")
    print(f"  Minimum degree: {min(degrees.values())}")
    print(f"  Average degree: {sum(degrees.values()) / len(degrees):.2f}")
    
    # Most connected nodes
    sorted_degrees = sorted(degrees.items(), key=lambda x: x[1], reverse=True)
    print(f"\nMost connected nodes (top 10):")
    for node, degree in sorted_degrees[:10]:
        print(f"  {node}: {degree} connections")


if __name__ == "__main__":
    print("="*70)
    print("Traveling Ethiopia Graph Visualization")
    print("="*70)
    
    visualize_graph()
    
    print("\n" + "="*70)
    print("Visualization complete!")
    print("="*70)


