# bringup.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='your_package',
            executable='motor_controller_node',
            name='motor_controller'
        ),
        Node(
            package='your_package',
            executable='lidar_node',
            name='lidar'
        ),
        Node(
            package='your_package',
            executable='imu_node',
            name='imu'
        ),
        Node(
            package='your_package',
            executable='camera_node',
            name='camera'
        ),
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            name='slam_toolbox',
            output='screen'
        ),
        Node(
            package='nav2_bringup',
            executable='bringup_launch.py',
            name='nav2',
            output='screen'
        ),
    ])