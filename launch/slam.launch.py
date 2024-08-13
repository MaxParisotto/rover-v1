#!/usr/bin/env python3

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='async_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {"use_sim_time": False},
                {"queue_size": 1000}, 
                {"resolution": 0.05},  # Map resolution in meters per cell
                {"max_scan_range": 8.0}  # Maximum Lidar range to consider in meters
            ],
            remappings=[
                ('scan', '/throttled_scan')
            ]
        ),
    ])