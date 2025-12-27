# Project Summary - Traveling Ethiopia Search Problem

## Overview
This project implements various search algorithms for solving the Traveling Ethiopia search problem, covering uninformed search, informed search, and adversarial search techniques.

## Implementation Status

### ✅ Question 1: Graph Conversion and BFS/DFS
- **1.1**: Graph converter implemented using adjacency list (dictionary)
- **1.2**: SearchAlgorithm class with BFS and DFS strategies
- Files: `graph_converter.py`, `search_algorithm.py`

### ✅ Question 2: Uniform Cost Search
- **2.1**: Graph with backward costs implemented
- **2.2**: Uniform Cost Search for single goal (Addis Ababa → Lalibela)
- **2.3**: Customized UCS for multiple goal states with local optimum preservation
- Files: `graph_with_costs.py`, `uniform_cost_search.py`, `multi_goal_ucs.py`

### ✅ Question 3: A* Search
- A* search algorithm with heuristic function
- Path from Addis Ababa to Moyale
- Files: `astar_search.py`

### ✅ Question 4: MiniMax Search
- MiniMax algorithm with alpha-beta pruning
- Adversarial search for coffee quality optimization
- Files: `minimax_search.py`

### ✅ Question 5: ROS/Gazebo Robot
- Three-wheel robot URDF with sensors (proximity, gyroscope, RGB camera)
- World file structure with Cartesian coordinates
- ROS-based path planner using uninformed search
- Files: `robot_description/`, `world/`, `ros_package/`

## Key Features

1. **Modular Design**: Each question is self-contained with clear interfaces
2. **Extensible**: Easy to add new search strategies or modify graph structures
3. **Well-Documented**: Code includes docstrings and comments
4. **Testable**: Each question has test files

## Graph Structures

The project uses sample graph structures based on Ethiopian cities. **Important**: You should update the graph edges, costs, and heuristics based on the actual figures (Figure 1, 2, 3, 4, 5) provided in your project instructions.

### Current Sample Structure:
- Nodes: Ethiopian cities (Addis Ababa, Ambo, Buta Jirra, etc.)
- Edges: Connections between cities
- Costs: Travel distances/costs between cities
- Heuristics: Estimated distances to goals

## Usage Examples

### Running Individual Questions
```bash
# Question 1
cd question1
python test_question1.py

# Question 2
cd question2
python test_question2.py

# Question 3
cd question3
python test_question3.py

# Question 4
cd question4
python test_question4.py
```

### Running All Tests
```bash
python run_all_tests.py
```

## Customization Required

Before final submission, you need to:

1. **Update Graph Structures**: 
   - Modify edges in `question1/graph_converter.py` based on Figure 1
   - Update costs in `question2/graph_with_costs.py` based on Figure 2
   - Add heuristics in `question3/astar_search.py` based on Figure 3
   - Adjust adversarial graph in `question4/minimax_search.py` based on Figure 4

2. **Question 5 Enhancements**:
   - Complete the robot URDF with all required sensors
   - Add all state coordinates to the world file based on Figure 5
   - Test the ROS node in actual Gazebo environment

3. **Testing**:
   - Verify all algorithms work with actual graph data
   - Test edge cases and error handling
   - Ensure output matches expected results

## Algorithm Details

### BFS vs DFS
- **BFS**: Explores level by level, finds shortest path (in terms of edges)
- **DFS**: Explores deep first, may find longer paths but uses less memory

### Uniform Cost Search
- Finds optimal path when edge costs vary
- Uses priority queue to explore lowest-cost paths first

### A* Search
- Combines actual cost (g) with heuristic estimate (h)
- More efficient than UCS when good heuristics are available

### MiniMax
- Optimal strategy for adversarial games
- Uses alpha-beta pruning to reduce search space

## Dependencies

- Python 3.7+
- numpy (for Question 5 if needed)
- ROS and Gazebo (for Question 5 only)

## Project Structure
```
.
├── question1/          # BFS/DFS implementation
├── question2/          # Uniform Cost Search
├── question3/          # A* Search
├── question4/          # MiniMax
├── question5/          # ROS/Gazebo
├── README.md           # Main documentation
├── requirements.txt    # Python dependencies
└── run_all_tests.py    # Test runner
```

## Notes

- All search algorithms return the path and exploration information
- Graph structures can be easily modified to match actual figures
- Code follows Python best practices with clear naming and documentation
- Test files demonstrate usage of each algorithm

## Next Steps

1. Review the actual figures and update graph data
2. Test each algorithm with the correct graph structures
3. Complete Question 5 ROS/Gazebo setup
4. Prepare presentation materials
5. Document any assumptions or design decisions

