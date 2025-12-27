# Question 5: Interactive Intelligent Systems

This question involves:
1. Designing a three-wheel functional robot using Gazebo
2. Creating a .world file with all states from Figure 5
3. Writing a ROS-based class using uninformed search strategy

## Structure

- `robot_description/`: URDF files for the three-wheel robot
- `world/`: Gazebo world files
- `ros_package/`: ROS nodes for path planning

## Requirements

- ROS (Noetic or Melodic)
- Gazebo
- Python 3

## Setup Instructions

1. Source your ROS workspace:
   ```bash
   source /opt/ros/noetic/setup.bash  # or melodic
   ```

2. Create a catkin workspace if needed:
   ```bash
   mkdir -p ~/catkin_ws/src
   cd ~/catkin_ws/src
   ```

3. Copy this question5 directory to your catkin workspace

4. Build the workspace:
   ```bash
   cd ~/catkin_ws
   catkin_make
   source devel/setup.bash
   ```

5. Launch Gazebo with the world:
   ```bash
   roslaunch traveling_ethiopia_robot gazebo_world.launch
   ```

6. Run the path planning node:
   ```bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

## Note

This is a template structure. You'll need to:
- Design the actual robot URDF with three wheels, physics engine, and sensors
- Create the world file with Cartesian coordinates for all states
- Implement the ROS node with search algorithm

