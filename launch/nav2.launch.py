from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nav2_bringup',
            executable='nav2_bringup',
            name='nav2_bringup',
            output='screen',
            parameters=[
                {"use_sim_time": False},
                {"autostart": True},
                {"map_subscribe_transient_local": True},
                {"use_composition": True},
            ],
        ),
    ])