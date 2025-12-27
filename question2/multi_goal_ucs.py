"""
Question 2.3: Customized Uniform Cost Search for multiple goal states
Given "Addis Ababa" as initial state and multiple goal states, generate
a path that visits all goal states preserving local optimum.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question2.graph_with_costs import GraphWithCosts
from question2.uniform_cost_search import UniformCostSearch


class MultiGoalUniformCostSearch:
    """Implements customized UCS for visiting multiple goal states"""
    
    def __init__(self, graph):
        """
        Initialize with a graph that has costs
        
        Args:
            graph: GraphWithCosts object
        """
        self.graph = graph.get_graph()
        self.ucs = UniformCostSearch(graph)
    
    def search(self, initial_state, goal_states):
        """
        Customized UCS that visits all goal states
        
        Args:
            initial_state: Starting node
            goal_states: List of goal nodes to visit
            
        Returns:
            tuple: (complete_path, total_cost, visited_goals_order)
        """
        if not goal_states:
            return [initial_state], 0, []
        
        remaining_goals = set(goal_states)
        current_position = initial_state
        complete_path = [initial_state]
        total_cost = 0
        visited_goals_order = []
        max_iterations = len(goal_states) * 10  # Prevent infinite loops
        iteration = 0
        
        while remaining_goals and iteration < max_iterations:
            iteration += 1
            
            # Find the nearest unvisited goal from current position
            best_goal = None
            best_cost = float('inf')
            best_path = None
            
            for goal in remaining_goals:
                path, cost, _ = self.ucs.search(current_position, goal)
                if path and cost < best_cost:
                    best_goal = goal
                    best_cost = cost
                    best_path = path
            
            if best_goal is None:
                # Cannot reach any remaining goals from current position
                # Try going back to initial state
                path_back, cost_back, _ = self.ucs.search(current_position, initial_state)
                if path_back:
                    if len(path_back) > 1:
                        complete_path.extend(path_back[1:])
                    total_cost += cost_back
                    current_position = initial_state
                    continue  # Try again from initial state
                else:
                    # Cannot reach initial state either - break
                    break
            
            # Visit the best goal
            if len(best_path) > 1:
                complete_path.extend(best_path[1:])
            total_cost += best_cost
            visited_goals_order.append(best_goal)
            remaining_goals.remove(best_goal)
            current_position = best_goal
        
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
                   "Bale", "Sof Oumer", "Bahir Dar"]
    
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
