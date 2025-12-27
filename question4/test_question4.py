"""
Test cases for Question 4
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question4.minimax_search import MiniMaxSearch, create_coffee_utility_function, create_adversarial_graph


def test_question4():
    """Test Question 4: MiniMax Search"""
    print("=" * 60)
    print("Testing Question 4")
    print("=" * 60)
    
    # Create adversarial graph
    graph = create_adversarial_graph()
    
    # Create utility function
    utility_func = create_coffee_utility_function()
    
    # Initialize MiniMax Search
    minimax = MiniMaxSearch(graph, utility_func, max_depth=4)
    
    print("\n4. Testing MiniMax Search (Addis Ababa as initial):")
    initial = "Addis Ababa"
    
    best_value, best_path = minimax.search(initial)
    if best_path:
        print(f"   [OK] MiniMax found best path: {' -> '.join(best_path)}")
        print(f"   Expected utility: {best_value}")
        print(f"   Final destination: {best_path[-1]}")
        
        # Show coffee quality
        utility_func_instance = create_coffee_utility_function()
        final_quality = utility_func_instance(best_path[-1], True)
        print(f"   Coffee quality at destination: {final_quality}/100")
    else:
        print(f"   [FAIL] MiniMax: No path found")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_question4()

