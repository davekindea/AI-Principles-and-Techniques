# Traveling Ethiopia Search Problem - AI Project

This project implements various search algorithms for solving the Traveling Ethiopia search problem as part of the Artificial Intelligence: Principles and Techniques course.

## Project Structure

```
.
├── question1/
│   ├── graph_converter.py      # Converts graph to data structure
│   ├── search_algorithm.py     # BFS and DFS implementation
│   └── test_question1.py       # Test cases
├── question2/
│   ├── graph_with_costs.py     # Graph with backward costs
│   ├── uniform_cost_search.py  # UCS implementation
│   ├── multi_goal_ucs.py       # Customized UCS for multiple goals
│   └── test_question2.py        # Test cases
├── question3/
│   ├── astar_search.py         # A* search implementation
│   └── test_question3.py       # Test cases
├── question4/
│   ├── minimax_search.py       # MiniMax algorithm
│   └── test_question4.py       # Test cases
├── question5/
│   ├── robot_description/      # Robot URDF files
│   ├── world/                  # Gazebo world files
│   ├── ros_package/           # ROS nodes
│   └── README.md              # Question 5 specific instructions
└── requirements.txt
```

## Requirements

- Python 3.7+
- For Question 5: ROS (Noetic/Melodic), Gazebo

## Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Question 1: BFS and DFS
```bash
cd question1
python test_question1.py
# Or run individually:
python graph_converter.py
python search_algorithm.py
```

### Question 2: Uniform Cost Search
```bash
cd question2
python test_question2.py
# Or run individually:
python uniform_cost_search.py
python multi_goal_ucs.py
```

### Question 3: A* Search
```bash
cd question3
python test_question3.py
# Or run individually:
python astar_search.py
```

### Question 4: MiniMax
```bash
cd question4
python test_question4.py
# Or run individually:
python minimax_search.py
```

### Question 5: ROS/Gazebo
See `question5/README.md` for detailed instructions.

## Implementation Details

### Question 1
- Converts state space graph (Figure 1) to adjacency list data structure
- Implements Breadth-First Search (BFS) and Depth-First Search (DFS)

### Question 2
- Converts graph with backward costs (Figure 2) to weighted adjacency list
- Implements Uniform Cost Search (UCS) for single goal
- Implements customized UCS for multiple goal states with local optimum preservation

### Question 3
- Uses graph with both heuristic values and backward costs (Figure 3)
- Implements A* search algorithm with heuristic function

### Question 4
- Implements MiniMax algorithm with alpha-beta pruning
- Models adversarial search where agent tries to reach good coffee quality locations

### Question 5
- Three-wheel robot design in Gazebo with sensors (proximity, gyroscope, RGB camera)
- World file with Cartesian coordinates for all states
- ROS-based path planner using uninformed search

## Notes

- The graph structures in the code are sample implementations. You should adjust the edges, costs, and heuristics based on the actual figures provided in the project instructions.
- For Question 5, ensure ROS and Gazebo are properly installed and configured.

## Author

AI Principles and Techniques Course Project  
Addis Ababa University Institute of Technology

