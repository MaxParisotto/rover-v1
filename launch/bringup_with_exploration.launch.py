from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        # Motor Controller Node
        Node(
            package='rover-v1',
            executable='motor_controller_node',
            name='motor_controller',
            output='screen',
        ),
        
        # LiDAR Node
        Node(
            package='rover-v1',
            executable='lidar_node',
            name='lidar',
            output='screen',
        ),
        
        # IMU Node
        Node(
            package='rover-v1',
            executable='imu_node',
            name='imu',
            output='screen',
        ),
        
        # Camera Node
        Node(
            package='rover-v1',
            executable='camera_node',
            name='camera',
            output='screen',
        ),
        
        # SLAM Toolbox Node
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[{
                'use_sim_time': False,
                'odom_frame': 'odom',
                'map_frame': 'map',
                'base_frame': 'base_link',
                'scan_topic': 'scan',
                'imu_topic': 'imu/data',
                'mode': 'mapping',  # SLAM mode for continuous map building
            }],
        ),

        # Simple Exploration Node (for example purposes, replace with your own logic)
        Node(
            package='rover-v1',
            executable='exploration_node',  # You'll need to write this
            name='exploration_node',
            output='screen',
        ),
    ])