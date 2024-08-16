import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import serial

class ServoControllerNode(Node):
    def __init__(self):
        super().__init__('servo_controller_node')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.serial_port = serial.Serial('/dev/ttyUSB0', 115200, timeout=1)  # Adjust for your setup

    def listener_callback(self, msg):
        linear_speed = msg.linear.x
        angular_speed = msg.angular.z
        self.get_logger().info(f'Received speed command: linear={linear_speed}, angular={angular_speed}')

        # Convert the linear and angular speed to servo commands
        left_speed = linear_speed - angular_speed
        right_speed = linear_speed + angular_speed

        # Create your command to send to the servos
        command = f'L{left_speed} R{right_speed}\n'
        self.serial_port.write(command.encode())

def main(args=None):
    rclpy.init(args=args)
    servo_controller_node = ServoControllerNode()
    rclpy.spin(servo_controller_node)
    servo_controller_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()