#!/bin/bash
# Run this script INSIDE the Docker container (from /catkin_ws).
# It copies the ROS 1 package, builds it, and optionally launches Gazebo.

set -e
source /opt/ros/noetic/setup.bash

PROJECT=/project
SRC=/catkin_ws/src
PKG=traveling_ethiopia_robot

# Copy package into workspace if not already there
if [ ! -d "$SRC/$PKG" ]; then
  echo "Setting up $PKG in workspace..."
  mkdir -p "$SRC"
  cp -r "$PROJECT/ros_package" "$SRC/$PKG"
  mkdir -p "$SRC/$PKG/worlds" "$SRC/$PKG/urdf"
  cp "$PROJECT/world/traveling_ethiopia.world" "$SRC/$PKG/worlds/"
  cp "$PROJECT/robot_description/three_wheel_robot.urdf" "$SRC/$PKG/urdf/"
  # Fix CMakeLists to use local worlds/ and urdf/
  sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' "$SRC/$PKG/CMakeLists.txt" 2>/dev/null || true
  sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' "$SRC/$PKG/CMakeLists.txt" 2>/dev/null || true
fi

# Build
cd /catkin_ws
catkin_make
source devel/setup.bash

echo ""
echo "Build done. To launch Gazebo:"
echo "  source /catkin_ws/devel/setup.bash"
echo "  roslaunch traveling_ethiopia_robot gazebo_world.launch"
echo ""
echo "In another terminal (attach to same container or run second container):"
echo "  source /catkin_ws/devel/setup.bash"
echo "  rosrun traveling_ethiopia_robot path_planner.py"
echo ""

# If we have a TTY and user wants to launch, uncomment:
# roslaunch traveling_ethiopia_robot gazebo_world.launch
exec bash
