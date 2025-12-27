#!/usr/bin/env python3
"""
Question 5.3: ROS-based path planner using uninformed search strategy
This node uses BFS or DFS to generate a path for the robot to travel
from any given initial state to the given goal state.
"""

import rospy
from geometry_msgs.msg import Twist, Point
from nav_msgs.msg import Odometry
from std_msgs.msg import String
import sys
import os

# Add parent directory to path to import search algorithms
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from question1.search_algorithm import SearchAlgorithm
from question1.graph_converter import create_figure1_graph


class ROSPathPlanner:
    """ROS node for path planning using uninformed search"""
    
    def __init__(self, initial_state, goal_state, strategy='bfs'):
        """
        Initialize the path planner
        
        Args:
            initial_state: Starting location
            goal_state: Target location
            strategy: 'bfs' or 'dfs'
        """
        rospy.init_node('path_planner', anonymous=True)
        
        # Create graph and search algorithm
        converter = create_figure1_graph()
        graph = converter.get_graph()
        self.search_alg = SearchAlgorithm(graph)
        
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.strategy = strategy
        
        # Publishers and Subscribers
        self.cmd_vel_pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.path_pub = rospy.Publisher('/planned_path', String, queue_size=10)
        self.odom_sub = rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        # State coordinates (from world file)
        self.state_coordinates = self.load_state_coordinates()
        
        # Current position
        self.current_position = None
        self.current_path = None
        self.path_index = 0
        
        # Control parameters
        self.linear_speed = 0.2
        self.angular_speed = 0.5
        self.distance_threshold = 0.5  # meters
        
    def load_state_coordinates(self):
        """
        Load state coordinates from world file
        This should match the coordinates in the .world file
        """
        # Sample coordinates - adjust based on actual Figure 5
        coordinates = {
            "Addis Ababa": (0, 0, 0),
            "Ambo": (5, 0, 0),
            "Buta Jirra": (3, 2, 0),
            "Wolkite": (2, -3, 0),
            # Add more coordinates based on Figure 5
        }
        return coordinates
    
    def odom_callback(self, msg):
        """Callback for odometry updates"""
        self.current_position = (
            msg.pose.pose.position.x,
            msg.pose.pose.position.y,
            msg.pose.pose.position.z
        )
    
    def plan_path(self):
        """Plan path from initial to goal state"""
        rospy.loginfo(f"Planning path from {self.initial_state} to {self.goal_state} using {self.strategy.upper()}")
        
        path, explored = self.search_alg.search(
            self.initial_state, 
            self.goal_state, 
            strategy=self.strategy
        )
        
        if path:
            self.current_path = path
            self.path_index = 0
            
            # Publish path
            path_str = " -> ".join(path)
            self.path_pub.publish(path_str)
            rospy.loginfo(f"Path found: {path_str}")
            rospy.loginfo(f"Path length: {len(path) - 1} edges")
            
            return True
        else:
            rospy.logwarn(f"No path found from {self.initial_state} to {self.goal_state}")
            return False
    
    def get_next_waypoint(self):
        """Get the next waypoint in the path"""
        if self.current_path and self.path_index < len(self.current_path):
            return self.current_path[self.path_index]
        return None
    
    def move_to_waypoint(self, waypoint):
        """
        Move robot towards a waypoint
        This is a simplified implementation
        """
        if waypoint not in self.state_coordinates:
            rospy.logwarn(f"Waypoint {waypoint} not found in coordinates")
            return False
        
        if self.current_position is None:
            return False
        
        target = self.state_coordinates[waypoint]
        current = self.current_position
        
        # Calculate distance and angle
        dx = target[0] - current[0]
        dy = target[1] - current[1]
        distance = (dx**2 + dy**2)**0.5
        
        if distance < self.distance_threshold:
            # Reached waypoint
            return True
        
        # Calculate angle
        import math
        angle = math.atan2(dy, dx)
        
        # Create twist message
        twist = Twist()
        
        # Simple control: turn first, then move forward
        if abs(angle) > 0.1:  # Need to turn
            twist.angular.z = self.angular_speed if angle > 0 else -self.angular_speed
        else:  # Move forward
            twist.linear.x = self.linear_speed
        
        self.cmd_vel_pub.publish(twist)
        return False
    
    def execute_path(self):
        """Execute the planned path"""
        rate = rospy.Rate(10)  # 10 Hz
        
        while not rospy.is_shutdown() and self.current_path:
            waypoint = self.get_next_waypoint()
            
            if waypoint is None:
                rospy.loginfo("Path execution complete!")
                # Stop robot
                twist = Twist()
                self.cmd_vel_pub.publish(twist)
                break
            
            rospy.loginfo(f"Moving to waypoint {self.path_index + 1}/{len(self.current_path)}: {waypoint}")
            
            reached = self.move_to_waypoint(waypoint)
            
            if reached:
                rospy.loginfo(f"Reached {waypoint}")
                self.path_index += 1
            
            rate.sleep()
    
    def run(self):
        """Main run method"""
        rospy.loginfo("Path Planner Node Started")
        
        # Wait for odometry
        rospy.sleep(1)
        
        # Plan path
        if self.plan_path():
            # Execute path
            self.execute_path()
        else:
            rospy.logerr("Failed to plan path")


if __name__ == '__main__':
    try:
        # Get parameters from ROS parameter server or use defaults
        initial = rospy.get_param('~initial_state', 'Addis Ababa')
        goal = rospy.get_param('~goal_state', 'Moyale')
        strategy = rospy.get_param('~strategy', 'bfs')
        
        planner = ROSPathPlanner(initial, goal, strategy)
        planner.run()
        
    except rospy.ROSInterruptException:
        pass

