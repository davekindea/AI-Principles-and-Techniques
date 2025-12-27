"""
Test cases for Question 1
"""

from graph_converter import create_figure1_graph
from search_algorithm import SearchAlgorithm


def test_question1():
    """Test Question 1.1 and 1.2"""
    print("=" * 60)
    print("Testing Question 1")
    print("=" * 60)
    
    # Create graph
    converter = create_figure1_graph()
    graph = converter.get_graph()
    
    print(f"\n1.1 Graph converted successfully!")
    print(f"   Total nodes: {len(graph)}")
    print(f"   Sample node 'Addis Ababa' has {len(graph.get('Addis Ababa', []))} neighbors")
    
    # Test search algorithms
    search_alg = SearchAlgorithm(graph)
    
    # Test BFS
    print("\n1.2 Testing BFS:")
    initial = "Addis Ababa"
    goal = "Moyale"
    
    path, explored = search_alg.search(initial, goal, strategy='bfs')
    if path:
        print(f"   [OK] BFS found path: {' -> '.join(path)}")
        print(f"   Path length: {len(path) - 1} edges")
    else:
        print(f"   [FAIL] BFS: No path found")
    
    # Test DFS
    print("\n1.2 Testing DFS:")
    path, explored = search_alg.search(initial, goal, strategy='dfs')
    if path:
        print(f"   [OK] DFS found path: {' -> '.join(path)}")
        print(f"   Path length: {len(path) - 1} edges")
    else:
        print(f"   [FAIL] DFS: No path found")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    test_question1()

