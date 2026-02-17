#!/bin/bash
# Run this script INSIDE the Docker container (e.g. bash /project/docker/build_and_launch.sh).
# Requires: container started with -v /path/to/question5:/project:ro
# It copies the ROS package from /project, builds it, then drops you in a shell.

set -e
source /opt/ros/noetic/setup.bash

PROJECT=/project
SRC=/catkin_ws/src
PKG=traveling_ethiopia_robot

if [ ! -d "$PROJECT/ros_package" ]; then
  echo "Error: /project not mounted or wrong path. Start container with: -v /path/to/question5:/project:ro"
  exit 1
fi

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
echo "Build done. Launch Gazebo in this terminal:"
echo "  roslaunch traveling_ethiopia_robot gazebo_world.launch"
echo ""
echo "Then open a second terminal and run another container (same volume), then:"
echo "  source /catkin_ws/devel/setup.bash"
echo "  rosrun traveling_ethiopia_robot path_planner.py"
echo ""
exec bash
