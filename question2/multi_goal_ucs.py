"""
Question 2.3: Customized Uniform Cost Search for multiple goal states
Given "Addis Ababa" as initial state and multiple goal states, generate
a path that visits all goal states preserving local optimum.
"""

import heapq
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question2.graph_with_costs import GraphWithCosts


class MultiGoalUniformCostSearch:
    """Implements customized UCS for visiting multiple goal states"""
    
    def __init__(self, graph):
        """
        Initialize with a graph that has costs
        
        Args:
            graph: GraphWithCosts object
        """
        self.graph = graph.get_graph()
    
    def find_path_to_nearest_goal(self, start, remaining_goals):
        """
        Find the path to the nearest unvisited goal from start
        
        Args:
            start: Starting node
            remaining_goals: Set of unvisited goal nodes
            
        Returns:
            tuple: (path, cost, reached_goal) or (None, None, None) if no goal reachable
        """
        if start in remaining_goals:
            return [start], 0, start
        
        # Priority queue: (total_cost, current_node, path)
        priority_queue = [(0, start, [start])]
        visited = set()
        
        while priority_queue:
            total_cost, current_node, path = heapq.heappop(priority_queue)
            
            if current_node in visited:
                continue
            
            visited.add(current_node)
            
            # Check if we reached a goal
            if current_node in remaining_goals:
                return path, total_cost, current_node
            
            # Explore neighbors
            neighbors = self.graph.get(current_node, [])
            for neighbor, edge_cost in neighbors:
                if neighbor not in visited:
                    new_cost = total_cost + edge_cost
                    new_path = path + [neighbor]
                    heapq.heappush(priority_queue, (new_cost, neighbor, new_path))
        
        return None, None, None
    
    def search(self, initial_state, goal_states):
        """
        Customized UCS that visits all goal states in optimal order
        
        Args:
            initial_state: Starting node
            goal_states: List of goal nodes to visit
            
        Returns:
            tuple: (complete_path, total_cost, visited_goals_order) or None if not all goals reachable
        """
        if not goal_states:
            return [initial_state], 0, []
        
        # Convert to set for efficient lookup
        remaining_goals = set(goal_states)
        current_position = initial_state
        complete_path = [initial_state]
        total_cost = 0
        visited_goals_order = []
        nodes_explored = []
        
        while remaining_goals:
            # Find path to nearest unvisited goal
            path, cost, reached_goal = self.find_path_to_nearest_goal(
                current_position, remaining_goals
            )
            
            if reached_goal is None:
                # Cannot reach remaining goals
                break
            
            # Add path (excluding the starting node to avoid duplication)
            if len(path) > 1:
                complete_path.extend(path[1:])
            total_cost += cost
            visited_goals_order.append(reached_goal)
            remaining_goals.remove(reached_goal)
            current_position = reached_goal
            nodes_explored.extend(path)
        
        if len(visited_goals_order) == len(goal_states):
            return complete_path, total_cost, visited_goals_order
        else:
            # Not all goals were reached
            return complete_path, total_cost, visited_goals_order


if __name__ == "__main__":
    from graph_with_costs import create_figure2_graph
    
    # Create graph
    graph = create_figure2_graph()
    
    # Initialize Multi-Goal UCS
    multi_ucs = MultiGoalUniformCostSearch(graph)
    
    # Question 2.3: Path from Addis Ababa visiting all goal states
    print("=" * 60)
    print("Question 2.3: Customized Uniform Cost Search for Multiple Goals")
    print("=" * 60)
    
    initial = "Addis Ababa"
    goal_states = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", 
                   "Bale", "Sof Oumer", "Arba Minch"]
    
    print(f"\nInitial state: {initial}")
    print(f"Goal states: {', '.join(goal_states)}")
    
    path, total_cost, visited_order = multi_ucs.search(initial, goal_states)
    
    if path:
        print(f"\nComplete path visiting all goals:")
        print(" -> ".join(path))
        print(f"\nOrder of goal visits: {' -> '.join(visited_order)}")
        print(f"\nTotal cost: {total_cost}")
        print(f"Total path length: {len(path) - 1} edges")
        print(f"Number of goals visited: {len(visited_order)}/{len(goal_states)}")
    else:
        print("\nNo valid path found")

