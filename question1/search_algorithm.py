"""
Question 1.2: Write a class that takes the converted state space graph,
initial state, goal state and a search strategy (BFS or DFS) and returns
the corresponding solution/path. Uses shared BFS and DFS algorithms.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.search_algorithms import breadth_first_search, depth_first_search
try:
    from question1.graph_converter import GraphConverter
except ImportError:
    from graph_converter import GraphConverter


class SearchAlgorithm:
    """Uses shared BFS and DFS search strategies on the state-space graph."""

    def __init__(self, graph):
        """
        Initialize with a graph (dictionary adjacency list).

        Args:
            graph: Dictionary where keys are nodes and values are lists of neighbors
        """
        self.graph = graph

    def breadth_first_search(self, initial_state, goal_state):
        """Breadth-First Search (shared algorithm). Returns (path, nodes_explored)."""
        return breadth_first_search(self.graph, initial_state, goal_state)

    def depth_first_search(self, initial_state, goal_state):
        """Depth-First Search (shared algorithm). Returns (path, nodes_explored)."""
        return depth_first_search(self.graph, initial_state, goal_state)

    def search(self, initial_state, goal_state, strategy="bfs"):
        """
        Main search method: BFS or DFS.

        Args:
            initial_state: Starting node
            goal_state: Target node
            strategy: 'bfs' or 'dfs'

        Returns:
            tuple: (path, nodes_explored) or (None, nodes_explored)
        """
        if strategy.lower() == "bfs":
            return self.breadth_first_search(initial_state, goal_state)
        if strategy.lower() == "dfs":
            return self.depth_first_search(initial_state, goal_state)
        raise ValueError(f"Unknown strategy: {strategy}. Use 'bfs' or 'dfs'")


if __name__ == "__main__":
    try:
        from question1.graph_converter import create_figure1_graph
    except ImportError:
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

