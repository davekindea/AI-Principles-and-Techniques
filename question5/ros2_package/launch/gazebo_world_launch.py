#!/usr/bin/env python3
"""ROS 2 launch: start Gazebo with the Traveling Ethiopia Figure 5 world."""

import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():
    pkg_share = get_package_share_directory("traveling_ethiopia_robot")
    world_file = os.path.join(pkg_share, "worlds", "traveling_ethiopia.world")

    # Prefer Gazebo Sim (gz sim) for Ubuntu 24.04
    gazebo_cmd = ["gz", "sim", world_file]

    return LaunchDescription([
        DeclareLaunchArgument("world", default_value=world_file, description="Path to world file"),
        ExecuteProcess(
            cmd=gazebo_cmd,
            output="screen",
        ),
    ])
