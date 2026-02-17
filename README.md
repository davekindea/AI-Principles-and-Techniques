# Traveling Ethiopia Search Problem

**AI project: search algorithms applied to the Traveling Ethiopia state-space (Figures 1–5).**

---

## Overview

This repository implements the assignments for an AI course: uninformed search (BFS, DFS), informed search (UCS, A*), and adversarial search (MiniMax) on graphs derived from the Traveling Ethiopia problem, plus a ROS/Gazebo simulation (Question 5) using BFS/DFS path planning.

| Question | Topic            | Algorithm(s)        | Main outputs              |
|----------|------------------|---------------------|---------------------------|
| 1        | State-space graph | **Graph**, **BFS**, **DFS** | Path, nodes explored      |
| 2        | Cost-based graph | **UCS**             | Path, total cost          |
| 3        | Heuristic search | **A***              | Path, total cost          |
| 4        | Adversarial      | **Minimax** (α–β)   | Best value, best path     |
| 5        | Robot simulation | **BFS** / **DFS**   | Path execution in Gazebo  |

All core algorithms live in **`shared/search_algorithms.py`**; each question uses the appropriate one with its own graph data.

---

## Requirements

- **Python 3.7+** (for Questions 1–4)
- **ROS Noetic** and **Gazebo** (optional, for Question 5 only)
- Dependencies: `pip install -r requirements.txt`

---

## Project Structure

```
ai pre/
├── shared/                      # Shared search algorithms
│   ├── __init__.py
│   └── search_algorithms.py     # BFS, DFS, UCS, A*, Minimax
├── question1/                   # Graph + BFS/DFS (Figure 1)
│   ├── graph_converter.py        # State-space → adjacency list
│   ├── search_algorithm.py      # SearchAlgorithm(BFS/DFS)
│   └── test_question1.py
├── question2/                    # UCS (Figure 2)
│   ├── graph_with_costs.py       # Weighted graph
│   ├── uniform_cost_search.py    # UCS (Addis Ababa → Lalibela)
│   ├── multi_goal_ucs.py        # Multi-goal UCS
│   └── test_question2.py
├── question3/                    # A* (Figures 2 + 3)
│   ├── heuristics.py            # Figure 3 heuristic values
│   ├── astar_search.py          # A* (Addis Ababa → Moyale)
│   └── test_question3.py
├── question4/                    # Minimax (Figure 4)
│   ├── minimax_search.py        # MiniMax + coffee utility
│   └── test_question4.py
├── question5/                    # ROS/Gazebo (Figure 5)
│   ├── robot_description/       # Three-wheel robot URDF
│   ├── world/                   # Gazebo world + coordinates
│   ├── ros_package/             # ROS 1 path planner (BFS/DFS)
│   ├── ros2_package/            # ROS 2 path planner (optional)
│   ├── docker/                  # Docker setup (Noetic + Gazebo)
│   └── README.md               # Q5 run instructions
├── requirements.txt
├── run_all_tests.py            # Run tests for Q1–Q4
└── README.md                   # This file
```

---

## Quick Start

### 1. Install and run all tests (Q1–Q4)

```bash
cd "ai pre"
pip install -r requirements.txt
python run_all_tests.py
```

### 2. Run by question

```bash
# From project root (recommended)
python -m question1.test_question1
python -m question2.test_question2
python -m question3.test_question3
python -m question4.test_question4
```

Or from each folder:

```bash
cd question1 && python test_question1.py
cd question2 && python test_question2.py
cd question3 && python test_question3.py
cd question4 && python test_question4.py
```

### 3. Run demos (path/cost output)

```bash
python question1/search_algorithm.py    # BFS/DFS Addis Ababa → Moyale
python question2/uniform_cost_search.py  # UCS Addis Ababa → Lalibela
python question3/astar_search.py        # A* Addis Ababa → Moyale
python question4/minimax_search.py     # Minimax from Addis Ababa
```

### 4. Question 5 (Interactive Intelligent Systems — Figure 5)

- **See the path (no Gazebo):**  
  `python question5/run_demo.py`  
  Shows BFS/DFS path and waypoints in Cartesian coordinates.
- **See the robot move in Gazebo:**  
  Use Docker: see **`question5/RUN_QUESTION5.md`** and **`question5/docker/STEP_BY_STEP.md`**.

---

## Algorithm and data mapping

| Item        | Location |
|------------|----------|
| Figure 1 graph | `question1/graph_converter.py` |
| Figure 2 costs | `question2/graph_with_costs.py` |
| Figure 3 heuristics | `question3/heuristics.py` |
| Figure 4 adversarial / coffee | `question4/minimax_search.py` |
| Figure 5 world / coordinates | `question5/world/`, `question5/ros_package/scripts/figure5_graph.py` |

---

## License and attribution

Course project — AI principles and techniques.  
Addis Ababa University Institute of Technology.
