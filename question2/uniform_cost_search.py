"""
Question 2.2: Uniform Cost Search algorithm
Assuming "Addis Ababa" as initial state, generate a path to "Lalibela"
"""

import heapq
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question2.graph_with_costs import GraphWithCosts, create_figure2_graph


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
        Uniform Cost Search algorithm - finds minimum cost path
        
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
        visited = set()  # Track visited nodes (only mark when popped with optimal cost)
        min_cost = {initial_state: 0}  # Track minimum cost to reach each node
        nodes_explored = []
        
        while priority_queue:
            total_cost, current_node, path = heapq.heappop(priority_queue)
            
            # Skip if we've already visited this node (we found optimal path to it)
            # This ensures we only process each node once with its optimal cost
            if current_node in visited:
                continue
            
            # Skip if we found a better path to this node after it was added to queue
            # This handles the case where we added a node with higher cost, then found a better path
            if current_node in min_cost and min_cost[current_node] < total_cost:
                continue
            
            # Mark as visited when we pop it (guaranteed to be optimal at this point)
            # In UCS, when a node is popped from the priority queue, it has the minimum cost
            visited.add(current_node)
            nodes_explored.append(current_node)
            
            # Check if goal reached - when we pop from queue, we have optimal path
            if current_node == goal_state:
                return path, total_cost, nodes_explored
            
            # Explore neighbors
            neighbors = self.graph.get(current_node, [])
            for neighbor, edge_cost in neighbors:
                if neighbor in visited:
                    continue
                
                new_cost = total_cost + edge_cost
                
                # Only add to queue if this is a better path to the neighbor
                # This prevents adding duplicate entries with higher costs
                if neighbor not in min_cost or new_cost < min_cost[neighbor]:
                    min_cost[neighbor] = new_cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        # No path found
        return None, None, nodes_explored


if __name__ == "__main__":
    # Create graph (all edges are bidirectional)
    graph = create_figure2_graph()
    
    # Initialize UCS
    ucs = UniformCostSearch(graph)
    
    # Question 2.2: Path from Addis Ababa to Lalibela
    print("=" * 60)
    print("Question 2.2: Uniform Cost Search")
    print("=" * 60)
    initial = "Addis Ababa"
    goal = "Gondar"
    
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
