# imu_node.py
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu

class ImuNode(Node):
    def __init__(self):
        super().__init__('imu_node')
        self.publisher_ = self.create_publisher(Imu, 'imu/data', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.publish_imu)

    def publish_imu(self):
        imu_msg = Imu()
        # Populate Imu message with data from your IMU sensor
        self.publisher_.publish(imu_msg)

def main(args=None):
    rclpy.init(args=args)
    imu_node = ImuNode()
    rclpy.spin(imu_node)
    imu_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()