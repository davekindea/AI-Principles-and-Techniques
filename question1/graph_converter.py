"""
Question 1.1: Convert Figure 1 (State space graph for traveling Ethiopia)
into a manageable data structure (dictionary/adjacency list)
"""

class GraphConverter:
    """Converts a state space graph into a dictionary-based adjacency list"""
    
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, from_node, to_node):
        """
        Add an edge to the graph (undirected)
        
        Args:
            from_node: Starting node
            to_node: Destination node
        """
        if from_node not in self.graph:
            self.graph[from_node] = []
        if to_node not in self.graph:
            self.graph[to_node] = []
        
        if to_node not in self.graph[from_node]:
            self.graph[from_node].append(to_node)
        if from_node not in self.graph[to_node]:
            self.graph[to_node].append(from_node)
    
    def build_from_edges(self, edges):
        """
        Build graph from a list of edges
        
        Args:
            edges: List of tuples (from_node, to_node)
        """
        for from_node, to_node in edges:
            self.add_edge(from_node, to_node)
    
    def build_from_adjacency_list(self, adjacency_data):
        """
        Build graph from adjacency list format
        {node: [list of connected nodes]}
        
        Args:
            adjacency_data: Dictionary with node as key and list of neighbors as value
        """
        for node, neighbors in adjacency_data.items():
            for neighbor in neighbors:
                self.add_edge(node, neighbor)
    
    def get_graph(self):
        """Return the graph as a dictionary"""
        return self.graph
    
    def get_neighbors(self, node):
        """Get all neighbors of a node"""
        return self.graph.get(node, [])


# Building the graph from Figure 1
def create_figure1_graph():
    """
    Create the graph structure based on Figure 1
    Data extracted directly from the image
    """
    converter = GraphConverter()
    
    # Graph structure from image extraction
    # Format: {City: [list of connected cities]}
    adjacency_data = {
        "Adama": ["Addis Ababa", "Assella", "Matahara", "Batu"],
        "Addis Ababa": ["Debre Birhan", "Ambo", "Adama"],
        "Adigrat": ["Adwa", "Mekelle"],
        "Adwa": ["Axum", "Adigrat", "Mekelle"],
        "Alamata": ["Mekelle", "Sekota", "Samara", "Woldia"],
        "Ambo": ["Addis Ababa", "Nekemte", "Wolkite"],
        "Arba Minch": ["Wolaita Sodo", "Konso", "Basketo"],
        "Asmera": ["Axum"],
        "Assella": ["Adama", "Dodolla"],
        "Assosa": ["Dembi Dollo"],
        "Awash": ["Gabi Rasu", "Matahara", "Chiro"],
        "Axum": ["Asmera", "Shire", "Adwa"],
        "Azezo": ["Metema", "Gondar", "Bahir Dar"],
        "Babile": ["Harar", "Jijiga", "Goba"],
        "Bahir Dar": ["Azezo", "Debre Tabor", "Metekel", "Injibara", "Finote Selam"],
        "Bale": ["Dodolla", "Liben", "Goba", "Sof Oumer"],
        "Basketo": ["Arba Minch", "Bench Maji"],
        "Batu": ["Butajira", "Shashemene", "Adama"],
        "Bedelle": ["Nekemte", "Gore", "Jimma"],
        "Bench Maji": ["Basketo", "Juba"],
        "Bongo": ["Tepi", "Mizan Teferi", "Jimma", "Dawro"],
        "Bule Hora": ["Yabello", "Dilla"],
        "Butajira": ["Wolkite", "Worabe", "Batu"],
        "Chiro": ["Awash", "Dire Dawa"],
        "Dawro": ["Bongo", "Wolaita Sodo"],
        "Debarke": ["Shire", "Gondar"],
        "Debre Birhan": ["Debre Sina", "Addis Ababa"],
        "Debre Markos": ["Finote Selam", "Debre Sina"],
        "Debre Sina": ["Debre Markos", "Kemise", "Debre Birhan"],
        "Debre Tabor": ["Lalibela", "Bahir Dar"],
        "Dega Habur": ["Jijiga", "Kebri Dehar"],
        "Dembi Dollo": ["Gimbi", "Assosa", "Gambella"],
        "Dessie": ["Woldia", "Kemise"],
        "Dilla": ["Bule Hora", "Hawassa"],
        "Dire Dawa": ["Chiro", "Harar"],
        "Dodolla": ["Shashemene", "Assella", "Bale"],
        "Dollo": ["Gode"],
        "Fanti Rasu": ["Samara", "Kilbet Rasu"],
        "Finote Selam": ["Bahir Dar", "Injibara", "Debre Markos"],
        "Gabi Rasu": ["Samara", "Awash"],
        "Gambella": ["Dembi Dollo", "Gore"],
        "Gimbi": ["Nekemte", "Dembi Dollo"],
        "Goba": ["Bale", "Sof Oumer", "Babile"],
        "Gode": ["Sof Oumer", "Kebri Dehar", "Dollo", "Mokadisho"],
        "Gondar": ["Humera", "Debarke", "Metema", "Azezo"],
        "Gore": ["Gambella", "Bedelle", "Tepi"],
        "Harar": ["Dire Dawa", "Babile"],
        "Hawassa": ["Dilla", "Shashemene"],
        "Hossana": ["Wolkite", "Worabe", "Wolaita Sodo"],
        "Humera": ["Kartum", "Shire", "Gondar"],
        "Injibara": ["Bahir Dar", "Metekel", "Finote Selam"],
        "Jijiga": ["Babile", "Dega Habur"],
        "Jimma": ["Bongo", "Bedelle", "Wolkite"],
        "Juba": ["Bench Maji"],
        "Kartum": ["Humera", "Metema"],
        "Kebri Dehar": ["Dega Habur", "Werder", "Gode"],
        "Kemise": ["Dessie", "Debre Sina"],
        "Kilbet Rasu": ["Fanti Rasu"],
        "Konso": ["Arba Minch", "Yabello"],
        "Lalibela": ["Sekota", "Woldia", "Debre Tabor"],
        "Liben": ["Bale"],
        "Matahara": ["Adama", "Awash"],
        "Mekelle": ["Adwa", "Adigrat", "Sekota", "Alamata"],
        "Metema": ["Kartum", "Gondar", "Azezo"],
        "Metekel": ["Bahir Dar", "Injibara"],
        "Mizan Teferi": ["Tepi", "Bongo"],
        "Mokadisho": ["Gode"],
        "Moyale": ["Yabello", "Nairobi"],
        "Nairobi": ["Moyale"],
        "Nekemte": ["Ambo", "Gimbi", "Bedelle"],
        "Samara": ["Alamata", "Woldia", "Fanti Rasu", "Gabi Rasu"],
        "Sekota": ["Mekelle", "Lalibela", "Alamata"],
        "Shashemene": ["Wolaita Sodo", "Hawassa", "Batu", "Dodolla"],
        "Shire": ["Humera", "Axum", "Debarke"],
        "Sof Oumer": ["Bale", "Goba", "Gode"],
        "Tepi": ["Gore", "Mizan Teferi", "Bongo"],
        "Werder": ["Kebri Dehar"],
        "Wolaita Sodo": ["Worabe", "Hossana", "Dawro", "Arba Minch", "Shashemene"],
        "Woldia": ["Alamata", "Lalibela", "Samara", "Dessie"],
        "Wolkite": ["Ambo", "Jimma", "Hossana", "Butajira"],
        "Worabe": ["Butajira", "Hossana", "Wolaita Sodo"],
        "Yabello": ["Konso", "Bule Hora", "Moyale"],
    }
    
    converter.build_from_adjacency_list(adjacency_data)
    return converter


if __name__ == "__main__":
    # Test the graph converter
    converter = create_figure1_graph()
    graph = converter.get_graph()
    
    print("Graph Structure (Adjacency List):")
    for node, neighbors in sorted(graph.items()):
        print(f"{node}: {neighbors}")
    
    print(f"\nTotal nodes: {len(graph)}")
    
    # Count all unique nodes
    all_nodes = set()
    for node, neighbors in graph.items():
        all_nodes.add(node)
        all_nodes.update(neighbors)
    print(f"Total unique nodes (including all connections): {len(all_nodes)}")
