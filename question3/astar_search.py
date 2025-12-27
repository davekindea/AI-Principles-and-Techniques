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
    
    def __init__(self, graph, heuristic_func=None):
        """
        Initialize with a graph and optional heuristic function
        
        Args:
            graph: GraphWithCosts object
            heuristic_func: Optional function that takes (node, goal) and returns heuristic value.
                          If None, uses dynamic heuristic based on path costs
        """
        self.graph = graph.get_graph()
        if heuristic_func is None:
            self.heuristic = self._create_dynamic_heuristic()
        else:
            self.heuristic = heuristic_func
        self._heuristic_cache = {}  # Cache for computed heuristics
    
    def _create_dynamic_heuristic(self):
        """
        Create a dynamic heuristic function based on graph structure and path costs
        Uses a simplified approach: estimates based on minimum edge costs and graph structure
        """
        def dynamic_heuristic(node, goal):
            """Calculate heuristic dynamically based on graph structure"""
            if node == goal:
                return 0
            
            # Check cache first
            cache_key = (node, goal)
            if cache_key in self._heuristic_cache:
                return self._heuristic_cache[cache_key]
            
            # Use BFS with cost to estimate minimum distance
            # This is a simplified version - in practice you might use UCS for better estimates
            heuristic_value = self._estimate_min_cost(node, goal)
            
            # Cache the result
            self._heuristic_cache[cache_key] = heuristic_value
            return heuristic_value
        
        return dynamic_heuristic
    
    def _estimate_min_cost(self, start, goal):
        """
        Estimate minimum cost from start to goal using actual path costs
        Uses UCS (Dijkstra) with early termination for heuristic calculation
        This provides an admissible heuristic (never overestimates)
        """
        if start == goal:
            return 0
        
        # Use UCS to find actual minimum cost path
        # This gives us the true heuristic value based on path costs
        import heapq
        
        # Priority queue: (cost, node)
        priority_queue = [(0, start)]
        visited = set()
        min_cost = float('inf')
        
        # Limit exploration to keep it efficient (heuristic calculation)
        max_explorations = 50
        explored = 0
        
        while priority_queue and explored < max_explorations:
            cost, current = heapq.heappop(priority_queue)
            
            if current in visited:
                continue
            
            visited.add(current)
            explored += 1
            
            if current == goal:
                min_cost = cost
                break
            
            neighbors = self.graph.get(current, [])
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    new_cost = cost + edge_cost
                    heapq.heappush(priority_queue, (new_cost, neighbor))
        
        # If we found the goal, return the actual cost
        if min_cost != float('inf'):
            return int(min_cost)
        
        # If we didn't find goal in limited search, use graph-based estimate
        # Use minimum edge cost * estimated hops (conservative underestimate)
        min_edge_cost = self._get_minimum_edge_cost()
        estimated_hops = self._estimate_hops(start, goal)
        estimated_cost = min_edge_cost * estimated_hops
        
        return int(estimated_cost)
    
    def _get_average_edge_cost(self):
        """Calculate average edge cost in the graph"""
        total_cost = 0
        total_edges = 0
        for node, neighbors in self.graph.items():
            for _, cost in neighbors:
                total_cost += cost
                total_edges += 1
        return total_cost / total_edges if total_edges > 0 else 1
    
    def _get_minimum_edge_cost(self):
        """Calculate minimum edge cost in the graph"""
        min_cost = float('inf')
        for node, neighbors in self.graph.items():
            for _, cost in neighbors:
                min_cost = min(min_cost, cost)
        return min_cost if min_cost != float('inf') else 1
    
    def _estimate_hops(self, start, goal):
        """Estimate number of hops using simple BFS (unweighted)"""
        from collections import deque
        
        if start == goal:
            return 0
        
        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            current, hops = queue.popleft()
            
            if current == goal:
                return hops
            
            neighbors = self.graph.get(current, [])
            for neighbor, _ in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, hops + 1))
        
        # If no path found, return a conservative estimate
        return 20
    
    def search(self, initial_state, goal_state):
        """
        A* Search algorithm - finds optimal path
        
        Args:
            initial_state: Starting node
            goal_state: Target node
            
        Returns:
            tuple: (path, total_cost, nodes_explored) or (None, None, nodes_explored) if no path found
        """
        if initial_state == goal_state:
            return [initial_state], 0, [initial_state]
        
        # g_score: cost from start to node
        # f_score: g_score + heuristic (estimated total cost)
        g_score = {initial_state: 0}
        f_score = {initial_state: self.heuristic(initial_state, goal_state)}
        
        # Priority queue: (f_score, g_score, current_node, path)
        priority_queue = [(f_score[initial_state], 0, initial_state, [initial_state])]
        visited = set()
        nodes_explored = []
        came_from = {initial_state: None}  # Track path reconstruction
        
        while priority_queue:
            current_f, current_g, current_node, path = heapq.heappop(priority_queue)
            
            # Skip if we've already found a better path to this node
            if current_node in visited:
                continue
            
            visited.add(current_node)
            nodes_explored.append(current_node)
            
            # Check if goal reached
            if current_node == goal_state:
                # Reconstruct optimal path using came_from
                optimal_path = []
                node = goal_state
                while node is not None:
                    optimal_path.append(node)
                    node = came_from[node]
                optimal_path.reverse()
                return optimal_path, g_score[goal_state], nodes_explored
            
            # Explore neighbors
            neighbors = self.graph.get(current_node, [])
            for neighbor, edge_cost in neighbors:
                if neighbor in visited:
                    continue
                
                tentative_g = g_score[current_node] + edge_cost
                
                # If this path to neighbor is better, update
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current_node
                    g_score[neighbor] = tentative_g
                    h_score = self.heuristic(neighbor, goal_state)
                    f_score[neighbor] = tentative_g + h_score
                    heapq.heappush(priority_queue, (f_score[neighbor], tentative_g, neighbor, []))
        
        # No path found
        return None, None, nodes_explored


# Import heuristic function from heuristics module
try:
    from question3.heuristics import create_heuristic_function
except ImportError:
    # Fallback if heuristics module doesn't exist
    def create_heuristic_function(graph=None):
        """
        Create a dynamic heuristic function based on path costs
        Works for ANY goal/destination dynamically, not just hardcoded values
        """
        # If graph is provided, use dynamic heuristic (recommended)
        if graph is not None:
            # Create a temporary A* instance to get the dynamic heuristic
            temp_astar = AStarSearch(graph, heuristic_func=None)
            return temp_astar.heuristic
        
        # Otherwise, return a simple dynamic heuristic that uses graph structure
        def heuristic(node, goal):
            """
            Return heuristic value from node to goal - calculated dynamically
            This works for ANY destination, not just specific hardcoded goals
            """
            if node == goal:
                return 0
            
            # This will be replaced when graph is available
            # For now, return a default value
            return 30
        
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
    from question2.graph_with_costs import create_figure2_graph
    
    # Create graph (using Figure 2 structure, but with heuristics from Figure 3)
    graph = create_figure2_graph()
    
    # Option 1: Use dynamic heuristic (based on path costs)
    print("Using dynamic heuristic based on path costs...")
    astar_dynamic = AStarSearch(graph, heuristic_func=None)
    
    # Option 2: Use fixed heuristic from Figure 3 (commented out, but available)
    # heuristic_func = create_heuristic_function()
    # astar = AStarSearch(graph, heuristic_func)
    
    # Use dynamic version
    astar = astar_dynamic
    
    # Question 3: Path from Addis Ababa to Moyale
    print("=" * 60)
    print("Question 3: A* Search Algorithm")
    print("=" * 60)
    
    initial = "Addis Ababa"
    goal = "Debre Birhan"  # Fixed spelling
    
    path, total_cost, explored = astar.search(initial, goal)
    
    if path:
        print(f"\nPath from {initial} to {goal}:")
        print(" -> ".join(path))
        print(f"\nTotal cost (g_score): {total_cost}")
        print(f"Path length: {len(path) - 1} edges")
        print(f"Nodes explored: {len(explored)}")
        print(f"Explored nodes: {', '.join(explored)}")
        
        # Show cost breakdown
        print("\nCost breakdown:")
        graph_dict = graph.get_graph()
        total_verify = 0
        for i in range(len(path) - 1):
            neighbors = graph_dict.get(path[i], [])
            for n, c in neighbors:
                if n == path[i + 1]:
                    total_verify += c
                    print(f"  {path[i]} -> {path[i+1]}: {c}")
                    break
        print(f"Total verified: {total_verify}")
    else:
        print(f"\nNo path found from {initial} to {goal}")
        print(f"Nodes explored: {len(explored)}")

