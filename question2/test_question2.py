"""
Test cases for Question 2
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from question2.graph_with_costs import create_figure2_graph
from question2.uniform_cost_search import UniformCostSearch
from question2.multi_goal_ucs import MultiGoalUniformCostSearch


def test_question2():
    """Test Question 2.1, 2.2, and 2.3"""
    print("=" * 60)
    print("Testing Question 2")
    print("=" * 60)
    
    # Create graph with costs
    graph = create_figure2_graph()
    graph_dict = graph.get_graph()
    
    print(f"\n2.1 Graph with costs converted successfully!")
    print(f"   Total nodes: {len(graph_dict)}")
    sample_node = "Addis Ababa"
    if sample_node in graph_dict:
        neighbors = graph_dict[sample_node]
        print(f"   Sample node '{sample_node}' has {len(neighbors)} neighbors with costs")
        print(f"   Example: {neighbors[0] if neighbors else 'No neighbors'}")
    
    # Test UCS
    print("\n2.2 Testing Uniform Cost Search (Addis Ababa -> Lalibela):")
    ucs = UniformCostSearch(graph)
    initial = "Addis Ababa"
    goal = "Lalibela"
    
    path, cost, explored = ucs.search(initial, goal)
    if path:
        print(f"   [OK] UCS found path: {' -> '.join(path)}")
        print(f"   Total cost: {cost}")
    else:
        print(f"   [FAIL] UCS: No path found")
    
    # Test Multi-Goal UCS
    print("\n2.3 Testing Multi-Goal Uniform Cost Search:")
    multi_ucs = MultiGoalUniformCostSearch(graph)
    goal_states = ["Axum", "Gondar", "Lalibela", "Babile", "Jimma", 
                   "Bale", "Sof Oumer", "Arba Minch"]
    
    path, total_cost, visited_order = multi_ucs.search(initial, goal_states)
    if path:
        print(f"   [OK] Multi-Goal UCS found path visiting {len(visited_order)} goals")
        print(f"   Order: {' -> '.join(visited_order)}")
        print(f"   Total cost: {total_cost}")
    else:
        print(f"   [FAIL] Multi-Goal UCS: No path found")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_question2()

