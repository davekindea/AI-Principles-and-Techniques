"""
Question 1.2: Write a class that takes the converted state space graph,
initial state, goal state and a search strategy (BFS or DFS) and returns
the corresponding solution/path.
"""

from collections import deque
from graph_converter import GraphConverter


class SearchAlgorithm:
    """Implements BFS and DFS search strategies"""
    
    def __init__(self, graph):
        """
        Initialize with a graph (dictionary adjacency list)
        
        Args:
            graph: Dictionary where keys are nodes and values are lists of neighbors
        """
        self.graph = graph
    
    def breadth_first_search(self, initial_state, goal_state):
        """
        Breadth-First Search algorithm
        
        Args:
            initial_state: Starting node
            goal_state: Target node
            
        Returns:
            tuple: (path, nodes_explored) or (None, nodes_explored) if no path found
        """
        if initial_state == goal_state:
            return [initial_state], [initial_state]
        
        # Queue for BFS: (current_node, path)
        queue = deque([(initial_state, [initial_state])])
        visited = set([initial_state])
        nodes_explored = [initial_state]
        
        while queue:
            current_node, path = queue.popleft()
            
            # Get neighbors
            neighbors = self.graph.get(current_node, [])
            
            for neighbor in neighbors:
                if neighbor == goal_state:
                    # Goal found
                    final_path = path + [neighbor]
                    nodes_explored.append(neighbor)
                    return final_path, nodes_explored
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    nodes_explored.append(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        
        # No path found
        return None, nodes_explored
    
    def depth_first_search(self, initial_state, goal_state):
        """
        Depth-First Search algorithm (iterative version)
        
        Args:
            initial_state: Starting node
            goal_state: Target node
            
        Returns:
            tuple: (path, nodes_explored) or (None, nodes_explored) if no path found
        """
        if initial_state == goal_state:
            return [initial_state], [initial_state]
        
        # Stack for DFS: (current_node, path)
        stack = [(initial_state, [initial_state])]
        visited = set([initial_state])
        nodes_explored = [initial_state]
        
        while stack:
            current_node, path = stack.pop()
            
            # Get neighbors
            neighbors = self.graph.get(current_node, [])
            
            for neighbor in neighbors:
                if neighbor == goal_state:
                    # Goal found
                    final_path = path + [neighbor]
                    nodes_explored.append(neighbor)
                    return final_path, nodes_explored
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    nodes_explored.append(neighbor)
                    stack.append((neighbor, path + [neighbor]))
        
        # No path found
        return None, nodes_explored
    
    def search(self, initial_state, goal_state, strategy='bfs'):
        """
        Main search method that routes to appropriate algorithm
        
        Args:
            initial_state: Starting node
            goal_state: Target node
            strategy: 'bfs' for Breadth-First Search or 'dfs' for Depth-First Search
            
        Returns:
            tuple: (path, nodes_explored) or (None, nodes_explored) if no path found
        """
        if strategy.lower() == 'bfs':
            return self.breadth_first_search(initial_state, goal_state)
        elif strategy.lower() == 'dfs':
            return self.depth_first_search(initial_state, goal_state)
        else:
            raise ValueError(f"Unknown strategy: {strategy}. Use 'bfs' or 'dfs'")


if __name__ == "__main__":
    # Test the search algorithms
    from graph_converter import create_figure1_graph
    
    converter = create_figure1_graph()
    graph = converter.get_graph()
    
    search_alg = SearchAlgorithm(graph)
    
    # Test BFS
    print("=" * 50)
    print("Breadth-First Search")
    print("=" * 50)
    initial = "Addis Ababa"
    goal = "Moyale"
    
    path, explored = search_alg.search(initial, goal, strategy='bfs')
    if path:
        print(f"Path from {initial} to {goal}: {' -> '.join(path)}")
        print(f"Path length: {len(path) - 1} edges")
        print(f"Nodes explored: {len(explored)}")
    else:
        print(f"No path found from {initial} to {goal}")
    
    # Test DFS
    print("\n" + "=" * 50)
    print("Depth-First Search")
    print("=" * 50)
    path, explored = search_alg.search(initial, goal, strategy='dfs')
    if path:
        print(f"Path from {initial} to {goal}: {' -> '.join(path)}")
        print(f"Path length: {len(path) - 1} edges")
        print(f"Nodes explored: {len(explored)}")
    else:
        print(f"No path found from {initial} to {goal}")

