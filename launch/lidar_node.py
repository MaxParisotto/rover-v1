# lidar_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class LidarNode(Node):
    def __init__(self):
        super().__init__('lidar_node')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_scan)

    def publish_scan(self):
        scan_msg = LaserScan()
        # Populate LaserScan message with data from your Lidar sensor
        self.publisher_.publish(scan_msg)

def main(args=None):
    rclpy.init(args=args)
    lidar_node = LidarNode()
    rclpy.spin(lidar_node)
    lidar_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()