#!/usr/bin/env python3
"""
Question 5.3: ROS 2 node - uninformed search (BFS/DFS) path planner for Figure 5.
"""

from collections import deque
import math

from rclpy.node import Node
from rclpy.qos import QoSProfile, ReliabilityPolicy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from .figure5_graph import get_graph_undirected, STATE_COORDINATES


class UninformedSearchPathPlanner:
    """Path planner using BFS or DFS on Figure 5 graph."""

    def __init__(self, graph=None, state_coordinates=None):
        self.graph = graph if graph is not None else get_graph_undirected()
        self.state_coordinates = state_coordinates if state_coordinates is not None else STATE_COORDINATES

    def breadth_first_search(self, initial_state, goal_state):
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
        if strategy.lower() == "bfs":
            return self.breadth_first_search(initial_state, goal_state)
        if strategy.lower() == "dfs":
            return self.depth_first_search(initial_state, goal_state)
        raise ValueError("strategy must be 'bfs' or 'dfs'")

    def path_as_waypoints(self, path):
        return [self.state_coordinates.get(s) for s in path if self.state_coordinates.get(s) is not None]


class PathPlannerNode(Node):
    """ROS 2 node: plans path and optionally publishes cmd_vel to follow waypoints."""

    def __init__(self):
        super().__init__("path_planner")
        self.declare_parameter("initial_state", "Addis Ababa")
        self.declare_parameter("goal_state", "Moyale")
        self.declare_parameter("strategy", "bfs")
        self.declare_parameter("execute_path", False)

        self.planner = UninformedSearchPathPlanner()
        self.path_pub = self.create_publisher(String, "planned_path", 10)
        self.cmd_vel_pub = self.create_publisher(Twist, "cmd_vel", 10)
        qos = QoSProfile(depth=10, reliability=ReliabilityPolicy.BEST_EFFORT)
        self.odom_sub = self.create_subscription(Odometry, "odom", self._odom_cb, qos)

        self.current_position = [0.0, 0.0]
        self.current_path = None
        self.path_index = 0
        self.linear_speed = 0.25
        self.angular_speed = 0.4
        self.dist_thresh = 0.8

    def _odom_cb(self, msg):
        self.current_position[0] = msg.pose.pose.position.x
        self.current_position[1] = msg.pose.pose.position.y

    def run(self):
        initial = self.get_parameter("initial_state").value
        goal = self.get_parameter("goal_state").value
        strategy = self.get_parameter("strategy").value
        execute = self.get_parameter("execute_path").value

        path, explored = self.planner.search(initial, goal, strategy)
        if not path:
            self.get_logger().warn(f"No path from {initial} to {goal}")
            return

        path_str = " -> ".join(path)
        self.get_logger().info(f"Path ({strategy.upper()}): {path_str}")
        self.get_logger().info(f"Path length: {len(path) - 1} edges, nodes explored: {len(explored)}")

        msg = String()
        msg.data = path_str
        self.path_pub.publish(msg)

        if execute:
            self.current_path = path
            self.path_index = 0
            self._execute_timer = self.create_timer(0.1, self._execute_step)
        else:
            self.get_logger().info("Path published on /planned_path. Set execute_path:=true to drive the robot.")

    def _execute_step(self):
        if not self.current_path or self.path_index >= len(self.current_path):
            twist = Twist()
            self.cmd_vel_pub.publish(twist)
            self.destroy_timer(self._execute_timer)
            self.get_logger().info("Path execution finished.")
            return
        waypoints = self.planner.path_as_waypoints(self.current_path)
        if self.path_index >= len(waypoints):
            self.path_index += 1
            return
        wp = waypoints[self.path_index]
        if wp is None:
            self.path_index += 1
            return
        dx = wp[0] - self.current_position[0]
        dy = wp[1] - self.current_position[1]
        dist = math.sqrt(dx * dx + dy * dy)
        if dist < self.dist_thresh:
            self.path_index += 1
            return
        angle = math.atan2(dy, dx)
        twist = Twist()
        if abs(angle) > 0.15:
            twist.angular.z = self.angular_speed if angle > 0 else -self.angular_speed
        else:
            twist.linear.x = self.linear_speed
        self.cmd_vel_pub.publish(twist)


def main(args=None):
    import rclpy
    rclpy.init(args=args)
    node = PathPlannerNode()
    node.run()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
