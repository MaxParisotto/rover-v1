from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False,  # Set to True if you're using simulated time
                'odom_frame': 'odom',
                'map_frame': 'map',
                'base_frame': 'base_link',
                'scan_topic': 'scan',
                'imu_topic': 'imu/data',  # Adjust this if you have a different topic for IMU data
                'map_update_interval': 0.1,  # Update interval for publishing the map
                'mode': 'mapping',  # Set the mode to 'mapping' for continuous map updates
            }],
        ),
    ])