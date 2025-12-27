"""
Question 2.2: Uniform Cost Search algorithm
Assuming "Addis Ababa" as initial state, generate a path to "Lalibela"
"""

import heapq
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question2.graph_with_costs import GraphWithCosts


class UniformCostSearch:
    """Implements Uniform Cost Search algorithm"""
    
    def __init__(self, graph):
        """
        Initialize with a graph that has costs
        
        Args:
            graph: GraphWithCosts object
        """
        self.graph = graph.get_graph()
    
    def search(self, initial_state, goal_state):
        """
        Uniform Cost Search algorithm
        
        Args:
            initial_state: Starting node
            goal_state: Target node
            
        Returns:
            tuple: (path, total_cost, nodes_explored) or (None, None, nodes_explored) if no path found
        """
        if initial_state == goal_state:
            return [initial_state], 0, [initial_state]
        
        # Priority queue: (total_cost, current_node, path)
        # Using total_cost as priority to ensure we explore lowest cost paths first
        priority_queue = [(0, initial_state, [initial_state])]
        visited = set()
        nodes_explored = []
        
        while priority_queue:
            total_cost, current_node, path = heapq.heappop(priority_queue)
            
            # Skip if already visited with a lower cost
            if current_node in visited:
                continue
            
            visited.add(current_node)
            nodes_explored.append(current_node)
            
            # Check if goal reached
            if current_node == goal_state:
                return path, total_cost, nodes_explored
            
            # Explore neighbors
            neighbors = self.graph.get(current_node, [])
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    new_cost = total_cost + edge_cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        # No path found
        return None, None, nodes_explored


if __name__ == "__main__":
    from graph_with_costs import create_figure2_graph
    
    # Create graph
    graph = create_figure2_graph()
    
    # Initialize UCS
    ucs = UniformCostSearch(graph)
    
    # Question 2.2: Path from Addis Ababa to Lalibela
    print("=" * 60)
    print("Question 2.2: Uniform Cost Search")
    print("=" * 60)
    initial = "Addis Ababa"
    goal = "Lalibela"
    
    path, total_cost, explored = ucs.search(initial, goal)
    
    if path:
        print(f"\nPath from {initial} to {goal}:")
        print(" -> ".join(path))
        print(f"\nTotal cost: {total_cost}")
        print(f"Path length: {len(path) - 1} edges")
        print(f"Nodes explored: {len(explored)}")
        print(f"Explored nodes: {', '.join(explored)}")
    else:
        print(f"\nNo path found from {initial} to {goal}")
        print(f"Nodes explored: {len(explored)}")

