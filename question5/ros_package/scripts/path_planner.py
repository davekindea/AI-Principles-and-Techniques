#!/usr/bin/env python3
"""
Question 5.3: ROS-based class using uninformed search strategy (BFS or DFS).
Generates a path for the robot from any given initial state to the goal state
in the Figure 5 state space. Uses shared BFS/DFS when the repo root is on path.
"""

from collections import deque
import math
import os
import sys

_script_dir = os.path.dirname(os.path.abspath(__file__))
if _script_dir not in sys.path:
    sys.path.insert(0, _script_dir)
# Repo root (ai pre) for shared algorithms
_repo_root = os.path.abspath(os.path.join(_script_dir, "..", "..", ".."))
if _repo_root not in sys.path:
    sys.path.insert(0, _repo_root)

try:
    from figure5_graph import get_graph_undirected, STATE_COORDINATES
except ImportError:
    STATE_COORDINATES = {}
    def get_graph_undirected():
        return {}

try:
    from shared.search_algorithms import breadth_first_search as _bfs_shared, depth_first_search as _dfs_shared
    _USE_SHARED = True
except ImportError:
    _USE_SHARED = False


class UninformedSearchPathPlanner:
    """
    ROS-based path planner using uninformed search (BFS or DFS).
    Uses the Figure 5 state space graph to plan a path from initial to goal state.
    """

    def __init__(self, graph=None, state_coordinates=None):
        """
        Initialize with Figure 5 graph and state coordinates.

        Args:
            graph: Dict {state: [neighbors]}. If None, uses figure5_graph.
            state_coordinates: Dict {state: (x, y, z)}. If None, uses figure5_graph.
        """
        self.graph = graph if graph is not None else get_graph_undirected()
        self.state_coordinates = state_coordinates if state_coordinates is not None else STATE_COORDINATES

    def breadth_first_search(self, initial_state, goal_state):
        """BFS: uses shared algorithm when available. Returns (path, nodes_explored)."""
        if _USE_SHARED:
            return _bfs_shared(self.graph, initial_state, goal_state)
        if initial_state == goal_state:
            return [initial_state], [initial_state]
        queue = deque([(initial_state, [initial_state])])
        visited = {initial_state}
        nodes_explored = [initial_state]
        while queue:
            node, path = queue.popleft()
            for neighbor in self.graph.get(node, []):
                if neighbor == goal_state:
                    return path + [neighbor], nodes_explored + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    nodes_explored.append(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None, nodes_explored

    def depth_first_search(self, initial_state, goal_state):
        """DFS: uses shared algorithm when available. Returns (path, nodes_explored)."""
        if _USE_SHARED:
            return _dfs_shared(self.graph, initial_state, goal_state)
        if initial_state == goal_state:
            return [initial_state], [initial_state]
        stack = [(initial_state, [initial_state])]
        visited = {initial_state}
        nodes_explored = [initial_state]
        while stack:
            node, path = stack.pop()
            for neighbor in self.graph.get(node, []):
                if neighbor == goal_state:
                    return path + [neighbor], nodes_explored + [neighbor]
                if neighbor not in visited:
                    visited.add(neighbor)
                    nodes_explored.append(neighbor)
                    stack.append((neighbor, path + [neighbor]))
        return None, nodes_explored

    def search(self, initial_state, goal_state, strategy="bfs"):
        """
        Generate a path from initial_state to goal_state.

        Args:
            initial_state: Start state name (e.g. "Addis Ababa").
            goal_state: Goal state name (e.g. "Moyale").
            strategy: "bfs" or "dfs".

        Returns:
            tuple: (path, nodes_explored) or (None, nodes_explored).
        """
        if strategy.lower() == "bfs":
            return self.breadth_first_search(initial_state, goal_state)
        if strategy.lower() == "dfs":
            return self.depth_first_search(initial_state, goal_state)
        raise ValueError("strategy must be 'bfs' or 'dfs'")

    def get_coordinates(self, state):
        """Return (x, y, z) for a state, or None."""
        return self.state_coordinates.get(state)

    def path_as_waypoints(self, path):
        """Return list of (x, y, z) for each state in path."""
        return [self.state_coordinates.get(s) for s in path if self.state_coordinates.get(s) is not None]


# ROS node that uses the planner
def main_ros():
    import rospy
    from geometry_msgs.msg import Twist
    from nav_msgs.msg import Odometry
    from std_msgs.msg import String

    rospy.init_node("path_planner", anonymous=True)

    initial = rospy.get_param("~initial_state", "Addis Ababa")
    goal = rospy.get_param("~goal_state", "Moyale")
    strategy = rospy.get_param("~strategy", "bfs")

    planner = UninformedSearchPathPlanner()
    path, explored = planner.search(initial, goal, strategy)

    if path:
        path_str = " -> ".join(path)
        rospy.loginfo("Path (%s): %s", strategy.upper(), path_str)
        rospy.loginfo("Path length: %d edges", len(path) - 1)
        rospy.loginfo("Nodes explored: %d", len(explored))

        # Publish path on topic for other nodes
        pub = rospy.Publisher("/planned_path", String, queue_size=1, latch=True)
        pub.publish(path_str)

        # Drive robot along the path using cmd_vel
        cmd_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
        rate = rospy.Rate(15)
        waypoints = planner.path_as_waypoints(path)
        current_pos = [0.0, 0.0]
        current_yaw = 0.0
        wp_index = 0
        dist_thresh = 1.0
        linear_speed = 0.4
        angular_speed = 0.8
        odom_received = [False]

        def odom_cb(msg):
            nonlocal current_pos, current_yaw
            current_pos[0] = msg.pose.pose.position.x
            current_pos[1] = msg.pose.pose.position.y
            q = msg.pose.pose.orientation
            siny_cosp = 2 * (q.w * q.z + q.x * q.y)
            cosy_cosp = 1 - 2 * (q.y * q.y + q.z * q.z)
            current_yaw = math.atan2(siny_cosp, cosy_cosp)
            odom_received[0] = True

        rospy.Subscriber("/odom", Odometry, odom_cb)
        rospy.loginfo("Robot will follow the path. Waiting for odometry...")
        for _ in range(100):
            if odom_received[0]:
                break
            rospy.sleep(0.1)
        rospy.loginfo("Starting movement along path: %s -> ... -> %s", path[0], path[-1])

        try:
            while not rospy.is_shutdown() and wp_index < len(waypoints):
                wp = waypoints[wp_index]
                if wp is None:
                    wp_index += 1
                    continue
                
                dx = wp[0] - current_pos[0]
                dy = wp[1] - current_pos[1]
                dist = math.sqrt(dx * dx + dy * dy)
                
                if dist < dist_thresh:
                    rospy.loginfo("Reached waypoint %d/%d: %s", wp_index + 1, len(path), path[wp_index])
                    wp_index += 1
                    continue

                # Target angle in world frame (point toward waypoint)
                target_angle = math.atan2(dy, dx)
                # Angle error relative to robot orientation
                angle_error = target_angle - current_yaw
                
                # Normalize to [-pi, pi]
                while angle_error > math.pi: angle_error -= 2 * math.pi
                while angle_error < -math.pi: angle_error += 2 * math.pi
                
                twist = Twist()
                if abs(angle_error) > 0.2:
                    twist.angular.z = angular_speed if angle_error > 0 else -angular_speed
                else:
                    twist.linear.x = linear_speed
                
                cmd_pub.publish(twist)
                rate.sleep()
            
            rospy.loginfo("Path execution finished successfully.")
        except Exception as e:
            rospy.logerr("Error during path execution: %s", str(e))
            import traceback
            rospy.logerr(traceback.format_exc())

        twist = Twist()
        cmd_pub.publish(twist)
        rospy.loginfo("Robot stopped. Path complete.")
    else:
        rospy.logwarn("No path found from %s to %s", initial, goal)

    rospy.spin()


if __name__ == "__main__":
    try:
        import rospy
    except ImportError:
        rospy = None
    if rospy is not None:
        try:
            main_ros()
        except rospy.ROSInterruptException:
            pass
    else:
        # Standalone test when ROS is not available
        import argparse
        parser = argparse.ArgumentParser(description="Run Uninformed Search Path Planner (Standalone)")
        parser.add_argument("--initial", default="Addis Ababa", help="Initial state")
        parser.add_argument("--goal", default="Moyale", help="Goal state")
        parser.add_argument("--strategy", default="bfs", choices=["bfs", "dfs"], help="Search strategy")
        args = parser.parse_args()

        planner = UninformedSearchPathPlanner()
        path, explored = planner.search(args.initial, args.goal, args.strategy)
        
        if path:
            print(f"Path ({args.strategy.upper()}): {' -> '.join(path)}")
            print(f"Path length: {len(path) - 1} edges")
            print(f"Nodes explored: {len(explored)}")
            waypoints = planner.path_as_waypoints(path)
            if waypoints and any(w for w in waypoints):
                print("Waypoints (x, y) in meters (Figure 5 Cartesian):")
                for i, (name, wp) in enumerate(zip(path, waypoints)):
                    if wp:
                        print(f"  {i+1}. {name}: ({wp[0]:.1f}, {wp[1]:.1f})")
        else:
            print(f"No path found from {args.initial} to {args.goal}")
