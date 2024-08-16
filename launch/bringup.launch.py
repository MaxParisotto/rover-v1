from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Motor Controller Node
        Node(
            package='rover-v1',
            executable='motor_controller_node',
            name='motor_controller',
            output='screen',  # Added output for better debugging
            parameters=[{'use_sim_time': False}],  # Example parameter
        ),
        
        # LiDAR Node
        Node(
            package='rover-v1',
            executable='lidar_node',
            name='lidar',
            output='screen',  # Added output for better debugging
            parameters=[{'use_sim_time': False}],  # Example parameter
        ),
        
        # IMU Node
        Node(
            package='rover-v1',
            executable='imu_node',
            name='imu',
            output='screen',  # Added output for better debugging
            parameters=[{'use_sim_time': False}],  # Example parameter
        ),
        
        # Camera Node
        Node(
            package='rover-v1',
            executable='camera_node',
            name='camera',
            output='screen',  # Added output for better debugging
            parameters=[{'use_sim_time': False}],  # Example parameter
        ),
        
        # SLAM Toolbox Node
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen',
            parameters=[
                {'use_sim_time': False},  # Set to True if using simulated time
                {'odom_frame': 'odom'},
                {'map_frame': 'map'},
                {'base_frame': 'base_link'},
                {'scan_topic': 'scan'},
                {'imu_topic': 'imu/data'},  # Replace with your actual IMU topic
            ],
        ),
        
        # Navigation2 Bringup Node
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2',
            output='screen',
            parameters=[
                {'use_sim_time': False},  # Set to True if using simulated time
                {'map_subscribe_transient_local': True},
            ],
            remappings=[
                ('/tf', 'tf'),
                ('/tf_static', 'tf_static')
            ],
        ),
    ])