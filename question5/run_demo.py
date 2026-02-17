#!/usr/bin/env python3
"""
Question 5 demo: run uninformed search path planner (no ROS/Gazebo required).
Shows the planned path and waypoints in Figure 5 Cartesian coordinates.
From project root: python question5/run_demo.py
Or: cd question5 && python run_demo.py
"""
import sys
import os

# Allow importing path_planner and figure5_graph
_here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_here, "ros_package", "scripts"))
sys.path.insert(0, os.path.dirname(_here))

from path_planner import UninformedSearchPathPlanner


def main():
    print("=" * 60)
    print("Question 5: Uninformed Search Path Planner (Figure 5)")
    print("=" * 60)
    planner = UninformedSearchPathPlanner()
    initial, goal = "Addis Ababa", "Moyale"
    for strategy in ("bfs", "dfs"):
        path, explored = planner.search(initial, goal, strategy)
        if path:
            print(f"\n{strategy.upper()}: {' -> '.join(path)}")
            print(f"  Edges: {len(path) - 1}, Nodes explored: {len(explored)}")
            waypoints = planner.path_as_waypoints(path)
            if waypoints and any(w for w in waypoints):
                print("  Waypoints (x, y) m:", end=" ")
                coords = [f"({wp[0]:.0f},{wp[1]:.0f})" for wp in waypoints if wp]
                print(" -> ".join(coords[:5]), "..." if len(coords) > 5 else "")
        else:
            print(f"\n{strategy.upper()}: No path")
    print("\nTo see the robot follow this path in Gazebo, use Docker:")
    print("  See question5/docker/STEP_BY_STEP.md")
    print("=" * 60)


if __name__ == "__main__":
    main()
