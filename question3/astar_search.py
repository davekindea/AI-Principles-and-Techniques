"""
Question 3: A* Search algorithm
Given Figure 3 (state space graph with heuristic and backward cost),
write a class that uses A* search to generate a path from "Addis Ababa"
to goal state "Moyale".
"""

import heapq
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question2.graph_with_costs import GraphWithCosts


class AStarSearch:
    """Implements A* search algorithm with heuristic function"""
    
    def __init__(self, graph, heuristic_func):
        """
        Initialize with a graph and heuristic function
        
        Args:
            graph: GraphWithCosts object
            heuristic_func: Function that takes (node, goal) and returns heuristic value
        """
        self.graph = graph.get_graph()
        self.heuristic = heuristic_func
    
    def search(self, initial_state, goal_state):
        """
        A* Search algorithm
        
        Args:
            initial_state: Starting node
            goal_state: Target node
            
        Returns:
            tuple: (path, total_cost, nodes_explored) or (None, None, nodes_explored) if no path found
        """
        if initial_state == goal_state:
            return [initial_state], 0, [initial_state]
        
        # Priority queue: (f_score, g_score, current_node, path)
        # f_score = g_score + h_score (heuristic)
        g_score = {initial_state: 0}
        f_score = {initial_state: self.heuristic(initial_state, goal_state)}
        
        priority_queue = [(f_score[initial_state], 0, initial_state, [initial_state])]
        visited = set()
        nodes_explored = []
        
        while priority_queue:
            current_f, current_g, current_node, path = heapq.heappop(priority_queue)
            
            # Skip if already visited with better cost
            if current_node in visited:
                continue
            
            visited.add(current_node)
            nodes_explored.append(current_node)
            
            # Check if goal reached
            if current_node == goal_state:
                return path, g_score[current_node], nodes_explored
            
            # Explore neighbors
            neighbors = self.graph.get(current_node, [])
            for neighbor, edge_cost in neighbors:
                if neighbor in visited:
                    continue
                
                tentative_g = g_score[current_node] + edge_cost
                
                # If this path to neighbor is better, update
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    g_score[neighbor] = tentative_g
                    h_score = self.heuristic(neighbor, goal_state)
                    f_score[neighbor] = tentative_g + h_score
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (f_score[neighbor], tentative_g, neighbor, new_path))
        
        # No path found
        return None, None, nodes_explored


# Heuristic function examples
def create_heuristic_function():
    """
    Create a heuristic function for Ethiopian cities
    This is a sample - adjust based on actual Figure 3 heuristics
    """
    # Sample heuristic values (straight-line distance approximation or given values)
    # In practice, these would come from Figure 3
    heuristic_values = {
        "Addis Ababa": {"Moyale": 780},
        "Ambo": {"Moyale": 800},
        "Buta Jirra": {"Moyale": 750},
        "Wolkite": {"Moyale": 700},
        "Shashemene": {"Moyale": 650},
        "Hawassa": {"Moyale": 600},
        "Dilla": {"Moyale": 550},
        "Moyale": {"Moyale": 0},
        # Add more heuristic values as needed
    }
    
    def heuristic(node, goal):
        """Return heuristic value from node to goal"""
        if node == goal:
            return 0
        
        # Check if we have a stored heuristic value
        if node in heuristic_values and goal in heuristic_values[node]:
            return heuristic_values[node][goal]
        
        # Default: return a large value if not found (makes it less optimal)
        # In practice, you'd want to fill in all heuristic values from Figure 3
        return 1000
    
    return heuristic


# Alternative: Simple distance-based heuristic (if coordinates available)
def create_distance_heuristic():
    """
    Create a distance-based heuristic if city coordinates are available
    """
    # Sample coordinates (latitude, longitude) - adjust based on actual data
    city_coordinates = {
        "Addis Ababa": (9.1450, 38.7667),
        "Moyale": (3.5167, 39.0583),
        # Add more coordinates as needed
    }
    
    def distance_heuristic(node, goal):
        """Calculate Euclidean distance heuristic"""
        if node == goal:
            return 0
        
        if node not in city_coordinates or goal not in city_coordinates:
            return 1000  # Default large value
        
        from math import sqrt
        lat1, lon1 = city_coordinates[node]
        lat2, lon2 = city_coordinates[goal]
        
        # Approximate distance (simplified)
        return sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2) * 100  # Scale factor
    
    return distance_heuristic


if __name__ == "__main__":
    from graph_with_costs import create_figure2_graph
    
    # Create graph (using Figure 2 structure, but with heuristics from Figure 3)
    graph = create_figure2_graph()
    
    # Create heuristic function
    heuristic_func = create_heuristic_function()
    
    # Initialize A* Search
    astar = AStarSearch(graph, heuristic_func)
    
    # Question 3: Path from Addis Ababa to Moyale
    print("=" * 60)
    print("Question 3: A* Search Algorithm")
    print("=" * 60)
    
    initial = "Addis Ababa"
    goal = "Moyale"
    
    path, total_cost, explored = astar.search(initial, goal)
    
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

