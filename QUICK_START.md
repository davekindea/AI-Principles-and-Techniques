# Quick Start Guide

## Running the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run All Tests
```bash
python run_all_tests.py
```

### 3. Run Individual Questions

#### Question 1: BFS/DFS
```bash
cd question1
python test_question1.py
```

#### Question 2: Uniform Cost Search
```bash
cd question2
python test_question2.py
```

#### Question 3: A* Search
```bash
cd question3
python test_question3.py
```

#### Question 4: MiniMax
```bash
cd question4
python test_question4.py
```

## Important Notes

⚠️ **Before Submission:**
1. Update graph edges, costs, and heuristics based on actual figures (Figure 1-5)
2. Test all algorithms with the correct graph data
3. Complete Question 5 ROS/Gazebo setup if required
4. Verify all outputs match expected results

## File Locations

- **Question 1**: `question1/graph_converter.py`, `question1/search_algorithm.py`
- **Question 2**: `question2/uniform_cost_search.py`, `question2/multi_goal_ucs.py`
- **Question 3**: `question3/astar_search.py`
- **Question 4**: `question4/minimax_search.py`
- **Question 5**: `question5/` (ROS/Gazebo files)

## Customization

All graph structures are in:
- `question1/graph_converter.py` - Figure 1 graph
- `question2/graph_with_costs.py` - Figure 2 graph with costs
- `question3/astar_search.py` - Heuristic values (update based on Figure 3)
- `question4/minimax_search.py` - Adversarial graph (update based on Figure 4)
- `question5/world/traveling_ethiopia.world` - World coordinates (update based on Figure 5)

## Troubleshooting

- **Import errors**: Make sure you're running from the project root directory
- **Path not found**: Check that all cities in your queries exist in the graph
- **Question 5**: Requires ROS and Gazebo to be installed and configured

