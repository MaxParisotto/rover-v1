import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
import numpy as np
from cv_bridge import CvBridge

class BayerToRGBNode(Node):

    def __init__(self):
        super().__init__('bayer_to_rgb_node')
        self.bridge = CvBridge()
        self.image_sub = self.create_subscription(
            Image,
            '/image_raw',
            self.image_callback,
            10)
        self.image_pub = self.create_publisher(
            Image,
            '/image_rgb',
            10)

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
        rgb_image = cv2.cvtColor(cv_image, cv2.COLOR_BAYER_RG2RGB)
        rgb_msg = self.bridge.cv2_to_imgmsg(rgb_image, encoding="rgb8")
        self.image_pub.publish(rgb_msg)

def main(args=None):
    rclpy.init(args=args)
    node = BayerToRGBNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
