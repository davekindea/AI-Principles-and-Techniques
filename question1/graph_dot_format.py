"""
Generate Graphviz DOT format for the state space graph
This can be used with Graphviz tools for better visualization
"""

from graph_converter import create_figure1_graph


def generate_dot_file():
    """Generate Graphviz DOT format file"""
    converter = create_figure1_graph()
    graph_dict = converter.get_graph()
    
    dot_content = []
    dot_content.append("graph TravelingEthiopia {")
    dot_content.append("  rankdir=TB;")
    dot_content.append("  node [shape=ellipse, style=filled, fillcolor=lightblue];")
    dot_content.append("  edge [color=gray];")
    dot_content.append("")
    
    # Highlight important nodes
    important_nodes = ["Addis Ababa", "Moyale", "Gondar", "Lalibela", 
                       "Axum", "Bahir Dar", "Jimma", "Hawassa", 
                       "Arba Minch", "Dire Dawa", "Harar"]
    
    for node in important_nodes:
        if node in graph_dict:
            dot_content.append(f'  "{node}" [fillcolor=lightcoral, style="filled,bold"];')
    
    dot_content.append("")
    
    # Add edges (avoid duplicates)
    edges_printed = set()
    for node, neighbors in graph_dict.items():
        for neighbor in neighbors:
            edge = tuple(sorted([node, neighbor]))
            if edge not in edges_printed:
                dot_content.append(f'  "{node}" -- "{neighbor}";')
                edges_printed.add(edge)
    
    dot_content.append("}")
    
    # Write to file
    output_file = "question1/graph.dot"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(dot_content))
    
    print(f"[OK] Graphviz DOT file created: {output_file}")
    print("\nTo visualize with Graphviz, run:")
    print(f"  dot -Tpng {output_file} -o graph.png")
    print(f"  dot -Tsvg {output_file} -o graph.svg")
    
    return output_file


def create_text_diagram():
    """Create a simple text-based diagram"""
    converter = create_figure1_graph()
    graph_dict = converter.get_graph()
    
    print("\n" + "="*70)
    print("TEXT-BASED GRAPH DIAGRAM")
    print("="*70)
    print("\nKey Connections from Addis Ababa:")
    print("-"*70)
    
    start = "Addis Ababa"
    if start in graph_dict:
        print(f"\n{start}")
        for neighbor in sorted(graph_dict[start]):
            print(f"  -> {neighbor}")
            if neighbor in graph_dict:
                for n2 in sorted(graph_dict[neighbor])[:3]:  # Show first 3
                    if n2 != start:
                        print(f"      -> {n2}")
    
    print("\n" + "="*70)
    print("Complete Adjacency List:")
    print("="*70)
    for node in sorted(graph_dict.keys()):
        neighbors = sorted(graph_dict[node])
        print(f"\n{node} ({len(neighbors)} connections):")
        print(f"  {', '.join(neighbors)}")


if __name__ == "__main__":
    print("="*70)
    print("Generating Graph Visualization Files")
    print("="*70)
    
    # Generate DOT file
    generate_dot_file()
    
    # Create text diagram
    create_text_diagram()
    
    print("\n" + "="*70)
    print("Visualization files created!")
    print("="*70)
    print("\nFiles created:")
    print("  1. question1/graph_visualization.png - Full graph visualization")
    print("  2. question1/graph_simple.png - Simplified view")
    print("  3. question1/graph.dot - Graphviz DOT format")
    print("\nYou can view the PNG files in any image viewer.")

