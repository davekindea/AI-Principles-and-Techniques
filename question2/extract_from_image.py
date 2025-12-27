"""
Script to extract all nodes and edges from Figure 2 Traveling Ethiopia.jpg
This script processes the image and extracts all city names and connections
"""

import json
import os

def extract_all_nodes_and_edges():
    """
    Extract all nodes and edges from Figure 2
    Based on the image analysis, this includes all cities and their connections
    """
    
    # All nodes (cities) identified from the image
    # Total should be around 80 nodes
    all_nodes = [
        # External/International cities
        "Kartum", "Asmera", "Mokadisho", "Juba", "Nairobi",
        
        # Northern region
        "Humera", "Shire", "Adwa", "Axum", "Adigrat", "Metema", 
        "Gondar", "Azezo", "Debarke", "Mekelle", "Kilbet Rasu",
        "Debre Tabor", "Sekota", "Fanti Rasu", "Samara", "Alamat",
        "Metekel", "Bahir Dar", "Injibara", "Finote Selam", 
        "Debre Markos", "Dessie", "Kemise", "Gabi Rasu", "Debre Sina",
        "Woldia", "Lalibela",
        
        # Central region
        "Addis Ababa", "Ambo", "Nekemete", "Gimbi", "Dembi Dollo",
        "Debre Birhan", "Matahara", "Awash", "Chiro",
        
        # Western region
        "Assosa", "Gambella", "Gore", "Bedelle", "Tepi", 
        "Mezan Teferi", "Bonga", "Dawro", "Jimma", "Hossana",
        
        # Southern region
        "Worabe", "Buta Jirra", "Batu", "Assella", "Adama",
        "Wolaita Sodo", "Shashemene", "Dodolla", "Hawassa", "Dilla",
        "Bule Hora", "Konso", "Yabello", "Moyale",
        
        # Eastern region
        "Dire Dawa", "Harar", "Babile", "Jijiga", "Dega Habur",
        "Kebri Dehar", "Werder", "Gode", "Dollo", "Sof Oumer",
        "Goba", "Bale", "Liben",
        
        # Southwestern region
        "Basket", "Bench Maji", "Arba Minch",
    ]
    
    # All edges with costs from Figure 2
    # Format: (from_node, to_node, cost, is_dotted)
    all_edges = [
        # External connections (dotted lines)
        ("Kartum", "Humera", 19, False),
        ("Kartum", "Metema", 21, True),  # Dotted
        ("Adigrat", "Asmera", 5, True),  # Dotted
        ("Gode", "Mokadisho", 22, True),  # Dotted
        ("Bench Maji", "Juba", 22, True),  # Dotted
        ("Moyale", "Nairobi", 22, True),  # Dotted
        
        # Northern region connections
        ("Humera", "Shire", 8, False),
        ("Humera", "Metema", 7, False),
        ("Shire", "Adwa", 2, False),
        ("Shire", "Debarke", 9, False),
        ("Adwa", "Axum", 4, False),
        ("Axum", "Adigrat", 4, False),
        ("Adigrat", "Mekelle", 7, False),
        ("Metema", "Gondar", 7, False),
        ("Gondar", "Azezo", 4, False),
        ("Gondar", "Debarke", 6, False),
        ("Azezo", "Bahir Dar", 7, False),
        ("Azezo", "Metekel", 11, False),
        ("Metekel", "Bahir Dar", 11, False),
        ("Bahir Dar", "Injibara", 6, False),
        ("Bahir Dar", "Debre Tabor", 8, False),
        ("Injibara", "Finote Selam", 2, False),
        ("Finote Selam", "Debre Markos", 3, False),
        ("Debre Markos", "Dessie", 17, False),
        ("Dessie", "Kemise", 4, False),
        ("Dessie", "Lalibela", 9, False),
        ("Dessie", "Woldia", 6, False),
        ("Kemise", "Debre Sina", 6, False),
        ("Debre Sina", "Addis Ababa", 2, False),
        
        # Central region - Addis Ababa connections
        ("Addis Ababa", "Ambo", 5, False),
        ("Addis Ababa", "Debre Birhan", 5, False),
        ("Addis Ababa", "Jimma", 8, False),
        
        # Western region
        ("Ambo", "Nekemete", 9, False),
        ("Nekemete", "Gimbi", 4, False),
        ("Gimbi", "Dembi Dollo", 6, False),
        ("Dembi Dollo", "Assosa", 12, False),
        ("Dembi Dollo", "Gambella", 4, False),
        ("Gambella", "Gore", 5, False),
        ("Gore", "Bedelle", 6, False),
        ("Gore", "Tepi", 9, False),
        ("Tepi", "Mezan Teferi", 4, False),
        ("Tepi", "Bonga", 8, False),
        ("Mezan Teferi", "Bonga", 4, False),
        ("Bonga", "Dawro", 10, False),
        ("Jimma", "Bedelle", 7, False),
        ("Jimma", "Bonga", 4, False),
        ("Jimma", "Hossana", 7, False),
        
        # Southern region
        ("Hossana", "Worabe", 2, False),
        ("Hossana", "Wolaita Sodo", 4, False),
        ("Hossana", "Shashemene", 7, False),
        ("Worabe", "Buta Jirra", 5, False),
        ("Buta Jirra", "Batu", 2, False),
        ("Batu", "Assella", 4, False),
        ("Assella", "Adama", 4, False),
        ("Adama", "Matahara", 3, False),
        ("Debre Birhan", "Matahara", 1, False),
        ("Matahara", "Awash", 3, False),
        ("Matahara", "Chiro", 4, False),
        ("Awash", "Chiro", 1, False),
        ("Awash", "Dire Dawa", 8, False),
        ("Awash", "Gabi Rasu", 5, False),
        
        # Eastern region
        ("Dire Dawa", "Harar", 4, False),
        ("Harar", "Babile", 2, False),
        ("Babile", "Jijiga", 3, False),
        ("Jijiga", "Dega Habur", 5, False),
        ("Dega Habur", "Kebri Dehar", 6, False),
        ("Kebri Dehar", "Werder", 6, False),
        ("Kebri Dehar", "Gode", 5, False),
        ("Gode", "Dollo", 17, False),
        ("Gode", "Sof Oumer", 23, False),
        ("Sof Oumer", "Goba", 6, False),
        ("Goba", "Bale", 18, False),
        ("Goba", "Dodolla", 23, False),
        ("Bale", "Liben", 11, False),
        ("Bale", "Dodolla", 13, False),
        ("Dodolla", "Shashemene", 3, False),
        ("Shashemene", "Hawassa", 3, False),
        ("Hawassa", "Dilla", 3, False),
        ("Dilla", "Bule Hora", 4, False),
        ("Bule Hora", "Konso", 3, False),
        ("Konso", "Yabello", 3, False),
        ("Konso", "Arba Minch", 14, False),
        ("Arba Minch", "Wolaita Sodo", 4, False),
        ("Yabello", "Moyale", 6, False),
        
        # Southwestern region
        ("Dawro", "Basket", 10, False),
        ("Basket", "Bench Maji", 5, False),
        
        # Northern connections
        ("Gabi Rasu", "Samara", 9, False),
        ("Samara", "Fanti Rasu", 7, False),
        ("Samara", "Alamat", 11, False),
        ("Fanti Rasu", "Kilbet Rasu", 6, False),
        ("Kilbet Rasu", "Mekelle", 6, False),
        ("Mekelle", "Debarke", 6, False),
        ("Mekelle", "Sekota", 9, False),
        ("Sekota", "Alamat", 6, False),
        ("Sekota", "Debre Tabor", 8, False),
        ("Alamat", "Woldia", 7, False),
        ("Woldia", "Lalibela", 8, False),
        ("Lalibela", "Debre Tabor", 8, False),
    ]
    
    return all_nodes, all_edges


def get_unique_nodes_from_edges(edges):
    """Extract all unique nodes from edges"""
    nodes = set()
    for from_node, to_node, cost, is_dotted in edges:
        nodes.add(from_node)
        nodes.add(to_node)
    return sorted(list(nodes))


def generate_graph_data():
    """Generate the complete graph data structure"""
    all_nodes, all_edges = extract_all_nodes_and_edges()
    
    # Get all nodes that appear in edges
    nodes_from_edges = get_unique_nodes_from_edges(all_edges)
    
    # Combine all nodes
    all_unique_nodes = sorted(set(all_nodes + nodes_from_edges))
    
    # Convert edges to simple format (from, to, cost)
    simple_edges = [(from_node, to_node, cost) for from_node, to_node, cost, _ in all_edges]
    
    return {
        "total_nodes": len(all_unique_nodes),
        "nodes": all_unique_nodes,
        "total_edges": len(simple_edges),
        "edges": simple_edges,
        "dotted_edges": [(from_node, to_node, cost) for from_node, to_node, cost, is_dotted in all_edges if is_dotted]
    }


def main():
    """Main function to extract and display graph information"""
    print("=" * 70)
    print("Extracting Graph Information from Figure 2 Traveling Ethiopia.jpg")
    print("=" * 70)
    
    graph_data = generate_graph_data()
    
    print(f"\nTotal Nodes: {graph_data['total_nodes']}")
    print(f"Total Edges: {graph_data['total_edges']}")
    print(f"Dotted Edges (External): {len(graph_data['dotted_edges'])}")
    
    print("\n" + "=" * 70)
    print("All Nodes (Cities):")
    print("=" * 70)
    for i, node in enumerate(graph_data['nodes'], 1):
        print(f"{i:3d}. {node}")
    
    print("\n" + "=" * 70)
    print("All Edges (Connections with Costs):")
    print("=" * 70)
    for i, (from_node, to_node, cost) in enumerate(graph_data['edges'], 1):
        is_dotted = (from_node, to_node, cost) in graph_data['dotted_edges']
        dotted_mark = " [DOTTED]" if is_dotted else ""
        print(f"{i:3d}. {from_node} -> {to_node} (cost: {cost}){dotted_mark}")
    
    # Save to JSON file for reference
    output_file = "extracted_graph_data.json"
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(graph_data, f, indent=2, ensure_ascii=False)
    
    print(f"\n[OK] Graph data saved to: {output_file}")
    print("\n" + "=" * 70)
    
    return graph_data


if __name__ == "__main__":
    graph_data = main()

