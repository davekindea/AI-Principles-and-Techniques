"""
Question 2.1: Convert Figure 2 (State space graph with backward cost)
into a manageable data structure
"""

class GraphWithCosts:
    """Represents a graph with edge costs (backward costs)"""
    
    def __init__(self):
        self.graph = {}  # {node: [(neighbor, cost), ...]}
    
    def add_edge(self, from_node, to_node, cost):
        """
        Add a directed edge with cost (avoids duplicates)
        
        Args:
            from_node: Starting node
            to_node: Destination node
            cost: Cost of the edge
        """
        if from_node not in self.graph:
            self.graph[from_node] = []
        
        # Check if edge already exists to avoid duplicates
        if not any(neighbor == to_node for neighbor, _ in self.graph[from_node]):
            self.graph[from_node].append((to_node, cost))
    
    def add_bidirectional_edge(self, from_node, to_node, cost):
        """Add bidirectional edge with same cost both ways"""
        self.add_edge(from_node, to_node, cost)
        self.add_edge(to_node, from_node, cost)
    
    def build_from_edges(self, edges, bidirectional=True):
        """
        Build graph from a list of edges with costs
        
        Args:
            edges: List of tuples (from_node, to_node, cost)
            bidirectional: If True, make all edges bidirectional (default: True)
        """
        for from_node, to_node, cost in edges:
            if bidirectional:
                self.add_bidirectional_edge(from_node, to_node, cost)
            else:
                self.add_edge(from_node, to_node, cost)
    
    def get_graph(self):
        """Return the graph as a dictionary"""
        return self.graph
    
    def get_neighbors(self, node):
        """Get all neighbors of a node with their costs"""
        return self.graph.get(node, [])


# Example: Building the graph from Figure 2 with costs
def create_figure2_graph():
    """
    Create the graph structure based on Figure 2 with backward costs
    Extracted from Figure 2 Traveling Ethiopia.jpg
    Data provided directly from image extraction
    """
    graph = GraphWithCosts()
    
    # All edges with costs from Figure 2
    # Format: (from, to, cost)
    # Data extracted directly from the image
    edges = [
        # Northern Region and External Connections
        ("Kartum", "Humera", 21),
        ("Kartum", "Metema", 19),
        ("Asmera", "Axum", 5),
        ("Humera", "Shire", 8),
        ("Humera", "Gondar", 9),
        ("Shire", "Axum", 2),
        ("Shire", "Debarke", 5),
        ("Axum", "Adwa", 1),
        ("Axum", "Sekota", 12),
        ("Adwa", "Adigrat", 4),
        ("Adwa", "Mekelle", 7),
        ("Adigrat", "Mekelle", 4),
        ("Mekelle", "Sekota", 9),
        ("Mekelle", "Alamata", 5),
        ("Sekota", "Lalibela", 6),
        ("Sekota", "Alamata", 6),
        ("Alamata", "Samara", 11),
        ("Alamata", "Woldia", 3),
        ("Woldia", "Lalibela", 7),
        ("Woldia", "Samara", 8),
        ("Woldia", "Dessie", 6),
        ("Lalibela", "Debre Tabor", 8),
        ("Debre Tabor", "Gondar", 8),
        ("Debre Tabor", "Bahir Dar", 4),
        ("Samara", "Fanti Rasu", 7),
        ("Samara", "Gabi Rasu", 9),
        ("Fanti Rasu", "Kilbet Rasu", 6),
        ("Gabi Rasu", "Awash", 5),

        # Central and Western Region
        ("Debarke", "Gondar", 4),
        ("Metema", "Gondar", 7),
        ("Metema", "Azezo", 7),
        ("Gondar", "Azezo", 1),
        ("Azezo", "Bahir Dar", 7),
        ("Bahir Dar", "Metekel", 11),
        ("Bahir Dar", "Injibara", 4),
        ("Bahir Dar", "Finote Selam", 6),
        ("Metekel", "Injibara", 4),
        ("Injibara", "Finote Selam", 2),
        ("Finote Selam", "Debre Markos", 3),
        ("Debre Markos", "Debre Sina", 17),
        ("Dessie", "Kemise", 4),
        ("Kemise", "Debre Sina", 6),
        ("Debre Sina", "Debre Birhan", 2),
        ("Debre Birhan", "Addis Ababa", 5),
        ("Addis Ababa", "Ambo", 5),
        ("Addis Ababa", "Adama", 3),
        ("Ambo", "Nekemte", 9),
        ("Ambo", "Wolkite", 6),
        ("Nekemte", "Gimbi", 4),
        ("Nekemte", "Bedelle", 2),
        ("Gimbi", "Dembi Dollo", 6),
        ("Dembi Dollo", "Assosa", 12),
        ("Dembi Dollo", "Gambella", 4),
        ("Gambella", "Gore", 5),
        ("Gore", "Bedelle", 6),
        ("Gore", "Tepi", 9),
        ("Tepi", "Mizan Teferi", 4),
        ("Tepi", "Bongo", 8),
        ("Mizan Teferi", "Bongo", 4),
        ("Bongo", "Jimma", 4),
        ("Bongo", "Dawro", 10),
        ("Jimma", "Bedelle", 7),
        ("Jimma", "Wolkite", 8),
        ("Wolkite", "Hossana", 5),
        ("Wolkite", "Butajira", 4),
        ("Butajira", "Worabe", 2),
        ("Butajira", "Batu", 2),
        ("Worabe", "Hossana", 2),
        ("Worabe", "Wolaita Sodo", 8),
        ("Hossana", "Wolaita Sodo", 4),
        ("Wolaita Sodo", "Dawro", 6),
        ("Wolaita Sodo", "Arba Minch", 4),
        ("Wolaita Sodo", "Shashemene", 7),

        # Southern and Eastern Region
        ("Arba Minch", "Konso", 4),
        ("Arba Minch", "Basketo", 10),
        ("Basketo", "Bench Maji", 5),
        ("Bench Maji", "Juba", 22),
        ("Konso", "Yabello", 3),
        ("Yabello", "Bule Hora", 3),
        ("Yabello", "Moyale", 6),
        ("Moyale", "Nairobi", 22),
        ("Bule Hora", "Dilla", 4),
        ("Dilla", "Hawassa", 3),
        ("Hawassa", "Shashemene", 1),
        ("Shashemene", "Batu", 3),
        ("Shashemene", "Dodolla", 3),
        ("Batu", "Adama", 4),
        ("Adama", "Assella", 4),
        ("Adama", "Matahara", 3),
        ("Matahara", "Awash", 1),
        ("Assella", "Dodolla", 1),
        ("Dodolla", "Bale", 13),
        ("Bale", "Liben", 11),
        ("Bale", "Goba", 18),
        ("Bale", "Sof Oumer", 23),
        ("Goba", "Sof Oumer", 6),
        ("Goba", "Babile", 28),
        ("Sof Oumer", "Gode", 23),
        ("Awash", "Chiro", 4),
        ("Chiro", "Dire Dawa", 8),
        ("Dire Dawa", "Harar", 4),
        ("Harar", "Babile", 2),
        ("Babile", "Jijiga", 3),
        ("Jijiga", "Dega Habur", 5),
        ("Dega Habur", "Kebri Dehar", 6),
        ("Kebri Dehar", "Werder", 6),
        ("Kebri Dehar", "Gode", 5),
        ("Gode", "Dollo", 17),
        ("Gode", "Mokadisho", 22)
    ]
    
    # Build graph with all edges bidirectional
    graph.build_from_edges(edges, bidirectional=True)
    return graph


if __name__ == "__main__":
    # Test the graph converter
    graph = create_figure2_graph()
    graph_dict = graph.get_graph()
    
    print("Graph Structure with Costs (Adjacency List):")
    for node, neighbors in sorted(graph_dict.items()):
        neighbor_str = ", ".join([f"({n}, {c})" for n, c in neighbors])
        print(f"{node}: [{neighbor_str}]")
    
    print(f"\nTotal nodes: {len(graph_dict)}")
    
    # Count all unique nodes including destinations
    all_nodes = set()
    for node, neighbors in graph_dict.items():
        all_nodes.add(node)
        for neighbor, _ in neighbors:
            all_nodes.add(neighbor)
    print(f"Total unique nodes (including destinations): {len(all_nodes)}")
