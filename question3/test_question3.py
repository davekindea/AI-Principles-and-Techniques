"""
Test cases for Question 3
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question3.astar_search import AStarSearch, create_heuristic_function
from question2.graph_with_costs import create_figure2_graph


def test_question3():
    """Test Question 3: A* Search"""
    print("=" * 60)
    print("Testing Question 3")
    print("=" * 60)
    
    # Create graph
    graph = create_figure2_graph()
    
    # Create heuristic function
    heuristic_func = create_heuristic_function()
    
    # Initialize A* Search
    astar = AStarSearch(graph, heuristic_func)
    
    print("\n3. Testing A* Search (Addis Ababa -> Moyale):")
    initial = "Addis Ababa"
    goal = "Moyale"
    
    path, cost, explored = astar.search(initial, goal)
    if path:
        print(f"   [OK] A* found path: {' -> '.join(path)}")
        print(f"   Total cost: {cost}")
        print(f"   Nodes explored: {len(explored)}")
    else:
        print(f"   [FAIL] A*: No path found")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_question3()

