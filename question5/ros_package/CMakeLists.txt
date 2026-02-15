cmake_minimum_required(VERSION 3.0.2)
project(traveling_ethiopia_robot)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
  sensor_msgs
  gazebo_ros
)

catkin_package()

include_directories(
  ${catkin_INCLUDE_DIRS}
)

# Install Python scripts and launch files
catkin_install_python(PROGRAMS
  scripts/path_planner.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

install(DIRECTORY launch/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/launch
)

install(DIRECTORY config/
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/config
  OPTIONAL
)

# Install world and robot description (from question5 parent folder)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/worlds
)
install(FILES ${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/urdf
)
