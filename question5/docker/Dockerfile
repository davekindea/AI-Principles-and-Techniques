# Ubuntu 20.04 + ROS Noetic + Gazebo for Traveling Ethiopia (Question 5)
FROM osrf/ros:noetic-desktop-full-focal

ENV DEBIAN_FRONTEND=noninteractive

# Install Gazebo 9 and ROS-Gazebo integration
RUN apt-get update && apt-get install -y --no-install-recommends \
    ros-noetic-gazebo-ros-pkgs \
    ros-noetic-gazebo-ros-control \
    ros-noetic-robot-state-publisher \
    ros-noetic-joint-state-publisher \
    ros-noetic-xacro \
    python3-rosdep \
    python3-rosinstall \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Create catkin workspace
RUN mkdir -p /catkin_ws/src
WORKDIR /catkin_ws

# Source ROS in shell
RUN echo "source /opt/ros/noetic/setup.bash" >> /etc/bash.bashrc

CMD ["bash"]
