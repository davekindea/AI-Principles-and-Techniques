#!/bin/bash
# Run this script INSIDE Ubuntu 20.04 (WSL or native) after installing ROS Noetic.
# It sets up the catkin workspace so you can run:
#   source ~/catkin_ws/devel/setup.bash
#   roslaunch traveling_ethiopia_robot gazebo_world.launch

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WS="$HOME/catkin_ws"
SRC="$WS/src"

echo "Script dir: $SCRIPT_DIR"
echo "Workspace:  $WS"

# Source ROS (Noetic)
if [ -f /opt/ros/noetic/setup.bash ]; then
  source /opt/ros/noetic/setup.bash
else
  echo "ROS Noetic not found. Install with: sudo apt install ros-noetic-desktop-full"
  exit 1
fi

mkdir -p "$SRC"
cd "$SRC"

# If question5 is not in src, copy or link it
if [ ! -d "$SRC/question5" ]; then
  if [ -d "$SCRIPT_DIR" ] && [ -f "$SCRIPT_DIR/world/traveling_ethiopia.world" ]; then
    cp -r "$SCRIPT_DIR" "$SRC/question5"
    echo "Copied question5 into $SRC"
  else
    echo "Copy question5 folder to $SRC (e.g. cp -r /mnt/c/Users/dawit/Desktop/ai\\ pre/question5 $SRC/)"
    exit 1
  fi
fi

# The catkin package is ros_package; catkin expects package in src/
# So we need traveling_ethiopia_robot to be a folder in src with package.xml
if [ ! -d "$SRC/traveling_ethiopia_robot" ]; then
  cp -r "$SRC/question5/ros_package" "$SRC/traveling_ethiopia_robot"
  mkdir -p "$SRC/traveling_ethiopia_robot/worlds" "$SRC/traveling_ethiopia_robot/urdf"
  cp "$SRC/question5/world/traveling_ethiopia.world" "$SRC/traveling_ethiopia_robot/worlds/"
  cp "$SRC/question5/robot_description/three_wheel_robot.urdf" "$SRC/traveling_ethiopia_robot/urdf/"
  echo "Created traveling_ethiopia_robot package with world and urdf"
fi

# Fix CMakeLists to use local worlds/ and urdf/ (no ../)
CMAKE="$SRC/traveling_ethiopia_robot/CMakeLists.txt"
if [ -f "$CMAKE" ] && grep -q "CMAKE_CURRENT_SOURCE_DIR.*../world" "$CMAKE"; then
  sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' "$CMAKE"
  sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' "$CMAKE"
  echo "Updated CMakeLists.txt to use local worlds/ and urdf/"
fi

# Build
cd "$WS"
catkin_make

echo ""
echo "Done. Run:"
echo "  source $WS/devel/setup.bash"
echo "  roslaunch traveling_ethiopia_robot gazebo_world.launch"
echo ""
echo "In another terminal, run the path planner:"
echo "  source $WS/devel/setup.bash"
echo "  rosrun traveling_ethiopia_robot path_planner.py"
echo ""
