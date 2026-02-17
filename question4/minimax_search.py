"""
Question 4: MiniMax Search Algorithm
Assume an adversary joins the Traveling Ethiopia Search Problem.
The goal of the agent would be to reach a state where it gains
good quality of Coffee. Uses shared MiniMax algorithm with alpha-beta pruning.
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from shared.search_algorithms import MiniMaxSearch as SharedMiniMax


class MiniMaxSearch(SharedMiniMax):
    """MiniMax: uses shared MiniMax with alpha-beta pruning and coffee utility."""
    pass


# Utility function: Coffee quality at different locations
def create_coffee_utility_function():
    """
    Create a utility function based on coffee quality at different locations
    Uses the provided utility values for terminal states
    """
    # Utility values for terminal states (cities) as provided
    utility_values = {
        "Shambu": 4,
        "Fincha": 5,
        "Gimbi": 8,
        "Limu": 8,
        "Hossana": 6,
        "Durame": 5,
        "Bench Naji": 5,
        "Bench Maji": 5,  # Alternative spelling
        "Tepi": 6,
        "Kaffa": 7,
        "Dilla": 9,
        "Chiro": 6,
        "Harar": 10,
    }
    
    # Default utility for non-terminal states (can be adjusted)
    default_utility = 0
    
    def utility(node, is_maximizing_player):
        """
        Utility at a node (e.g. leaf). Same payoff for both players:
        agent maximizes it, adversary minimizes it.
        """
        base_utility = utility_values.get(node, default_utility)
        return base_utility

    return utility


# Figure 4: Adversarial Traveling Ethiopia (from "Figure 4 Adversary Traveling Ethiopia.jpg")
# Initial: Addis Ababa. Agent and adversary alternate moves. Terminal nodes have utility (coffee quality).
def create_adversarial_graph():
    """
    Create the adversarial game graph from Figure 4.
    Structure: Addis Ababa -> Ambo/Adama -> ... -> terminal nodes (Shambu, Fincha, etc.).
    """
    return {
        "Addis Ababa": ["Ambo", "Adama"],
        "Ambo": ["Gedo", "Nekemte", "Buta Jirra"],
        "Adama": ["Diredawa", "Mojo"],
        "Gedo": ["Shambu", "Fincha"],
        "Nekemte": ["Gimbi", "Limu"],
        "Diredawa": ["Harar", "Chiro"],
        "Mojo": ["Dilla", "Kaffa"],
        "Buta Jirra": ["Worabe", "Wolkite"],
        "Worabe": ["Hossana", "Durame"],
        "Wolkite": ["Bench Naji", "Tepi"],
        # Terminal nodes (no successors)
        "Shambu": [],
        "Fincha": [],
        "Gimbi": [],
        "Limu": [],
        "Hossana": [],
        "Durame": [],
        "Bench Naji": [],
        "Tepi": [],
        "Kaffa": [],
        "Dilla": [],
        "Chiro": [],
        "Harar": [],
    }


if __name__ == "__main__":
    # Create adversarial graph
    graph = create_adversarial_graph()
    
    # Create utility function
    utility_func = create_coffee_utility_function()
    
    # Initialize MiniMax Search (depth 4: enough to reach any terminal in Figure 4)
    minimax = MiniMaxSearch(graph, utility_func, max_depth=4)
    
    # Question 4: Find best path for agent
    print("=" * 60)
    print("Question 4: MiniMax Search Algorithm")
    print("=" * 60)
    
    initial = "Addis Ababa"
    
    print(f"\nInitial state: {initial}")
    print("Agent's goal: Reach a state with good coffee quality")
    print("Adversary's goal: Prevent agent from reaching good coffee")
    
    best_value, best_path = minimax.search(initial)
    
    print(f"\nBest path for agent:")
    print(" -> ".join(best_path))
    print(f"\nExpected utility value: {best_value}")
    print(f"Final destination: {best_path[-1]}")
    
    # Show utility value at final destination
    utility_func_instance = create_coffee_utility_function()
    final_utility = utility_func_instance(best_path[-1], True)
    print(f"Utility value at final destination: {final_utility}")
    
    # Show all terminal states with their utility values
    print("\nTerminal States and Utility Values:")
    print("-" * 40)
    terminal_states = {
        "Shambu": 4, "Fincha": 5, "Gimbi": 8, "Limu": 8,
        "Hossana": 6, "Durame": 5, "Bench Naji": 5, "Tepi": 6,
        "Kaffa": 7, "Dilla": 9, "Chiro": 6, "Harar": 10
    }
    for state, utility in sorted(terminal_states.items(), key=lambda x: x[1], reverse=True):
        print(f"  {state}: {utility}")

