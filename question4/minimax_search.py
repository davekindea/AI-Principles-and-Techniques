"""
Question 4: MiniMax Search Algorithm
Assume an adversary joins the Traveling Ethiopia Search Problem.
The goal of the agent would be to reach a state where it gains
good quality of Coffee. Write a class that shows how MiniMax
search algorithm directs an agent to the best achievable destination.
"""

class MiniMaxSearch:
    """Implements MiniMax algorithm for adversarial search"""
    
    def __init__(self, graph, utility_func, max_depth=5):
        """
        Initialize MiniMax search
        
        Args:
            graph: Dictionary representing the game graph {node: [neighbors]}
            utility_func: Function that takes (node, is_max_player) and returns utility
            max_depth: Maximum depth to search
        """
        self.graph = graph
        self.utility = utility_func
        self.max_depth = max_depth
    
    def minimax(self, node, depth, is_maximizing_player, alpha=float('-inf'), beta=float('inf')):
        """
        MiniMax algorithm with alpha-beta pruning
        
        Args:
            node: Current node
            depth: Current depth
            is_maximizing_player: True if maximizing player (agent), False if minimizing (adversary)
            alpha: Best value for maximizing player
            beta: Best value for minimizing player
            
        Returns:
            tuple: (best_value, best_path)
        """
        # Terminal conditions
        if depth == 0 or node not in self.graph or len(self.graph[node]) == 0:
            utility = self.utility(node, is_maximizing_player)
            return utility, [node]
        
        neighbors = self.graph[node]
        
        if is_maximizing_player:
            # Agent's turn: maximize utility
            max_value = float('-inf')
            best_path = [node]
            
            for neighbor in neighbors:
                value, path = self.minimax(neighbor, depth - 1, False, alpha, beta)
                
                if value > max_value:
                    max_value = value
                    best_path = [node] + path
                
                alpha = max(alpha, value)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            
            return max_value, best_path
        
        else:
            # Adversary's turn: minimize utility
            min_value = float('inf')
            best_path = [node]
            
            for neighbor in neighbors:
                value, path = self.minimax(neighbor, depth - 1, True, alpha, beta)
                
                if value < min_value:
                    min_value = value
                    best_path = [node] + path
                
                beta = min(beta, value)
                if beta <= alpha:
                    break  # Alpha-beta pruning
            
            return min_value, best_path
    
    def search(self, initial_state):
        """
        Find the best path for the agent using MiniMax
        
        Args:
            initial_state: Starting node
            
        Returns:
            tuple: (best_value, best_path)
        """
        value, path = self.minimax(initial_state, self.max_depth, True)
        return value, path


# Utility function: Coffee quality at different locations
def create_coffee_utility_function():
    """
    Create a utility function based on coffee quality at different locations
    Higher values = better coffee quality
    """
    # Coffee quality scores for different cities (0-100 scale)
    # Adjust these based on actual Figure 4 or known coffee regions
    coffee_quality = {
        "Addis Ababa": 60,
        "Jimma": 95,  # Jimma is known for coffee
        "Bedele": 90,
        "Gore": 85,
        "Shashemene": 70,
        "Hawassa": 75,
        "Wolkite": 65,
        "Buta Jirra": 55,
        "Ambo": 50,
        "Nekemte": 60,
        "Gimbi": 70,
        "Worabe": 65,
        "Hossana": 60,
        "Dodola": 55,
        "Dilla": 50,
        "Wolaita Sodo": 65,
        "Arba Minch": 60,
        "Bale": 50,
        "Goba": 45,
        "Sof Oumer": 40,
        "Moyale": 30,
        "Tepi": 80,
        "Mizan": 75,
        "Konso": 60,
        "Yabello": 50,
        "Mega": 45,
        "Gode": 35,
        "Kebri Dehar": 30,
        "Warder": 25,
        "Basketo": 70,
        "Jinka": 65,
        "Key Afer": 60,
        "Turmi": 55,
        "Omorate": 50,
        "Kangatan": 45,
        "Dimeka": 50,
        "Hargelle": 30,
        "Boh": 25,
        "Elidar": 20,
        "Asseb": 15,
        "Dessie": 40,
        "Dollo": 35,
    }
    
    def utility(node, is_maximizing_player):
        """
        Calculate utility for a node
        
        Args:
            node: Current node
            is_maximizing_player: True if agent, False if adversary
            
        Returns:
            int: Utility value
        """
        base_quality = coffee_quality.get(node, 50)  # Default quality
        
        if is_maximizing_player:
            # Agent wants high coffee quality
            return base_quality
        else:
            # Adversary wants to minimize agent's coffee quality
            return -base_quality
    
    return utility


# Create game graph (simplified version - adjust based on Figure 4)
def create_adversarial_graph():
    """
    Create the adversarial game graph
    This represents possible moves for both agent and adversary
    """
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    from question1.graph_converter import create_figure1_graph
    
    converter = create_figure1_graph()
    return converter.get_graph()


if __name__ == "__main__":
    # Create adversarial graph
    graph = create_adversarial_graph()
    
    # Create utility function
    utility_func = create_coffee_utility_function()
    
    # Initialize MiniMax Search
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
    
    # Show coffee quality at final destination
    utility_func_instance = create_coffee_utility_function()
    final_quality = utility_func_instance(best_path[-1], True)
    print(f"Coffee quality at final destination: {final_quality}/100")

