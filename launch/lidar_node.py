# lidar_node.py
#!/usr/bin/env python3
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # LDROBOT LiDAR publisher node for LD20
    ldlidar_node = Node(
        package='ldlidar_stl_ros2',
        executable='ldlidar_stl_ros2_node',
        name='LD20',
        output='screen',
        parameters=[
            {'product_name': 'LDLiDAR_LD20'},  # Updated for LD20
            {'topic_name': 'scan'},
            {'frame_id': 'base_laser'},
            {'port_name': '/dev/ttyUSB0'},
            {'port_baudrate': 230400},  # Verify this matches LD20's baud rate
            {'laser_scan_dir': True},
            {'enable_angle_crop_func': False},
            {'angle_crop_min': 135.0},
            {'angle_crop_max': 225.0}
        ]
    )

    # base_link to base_laser tf node
    base_link_to_laser_tf_node = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_link_to_base_laser_ld20',
        arguments=['0', '0', '0.18', '0', '0', '0', 'base_link', 'base_laser']
    )

    # Define LaunchDescription variable
    ld = LaunchDescription()

    ld.add_action(ldlidar_node)
    ld.add_action(base_link_to_laser_tf_node)

    return ld