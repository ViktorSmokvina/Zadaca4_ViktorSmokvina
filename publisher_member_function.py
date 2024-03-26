import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

package_name = 'py_pubsub'

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('broj')
        self.publisher_ = self.create_publisher(Int32, '/broj', 10)
        timer_period = 1.0
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Broj: %d' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
