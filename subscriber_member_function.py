import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

package_name = 'py_pubsub'

class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('kvadrat broja')
        self.subscription = self.create_subscription(
            Int32,
            '/broj',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(Int32, '/kvadrat_broja', 10)
        self.subscription

    def listener_callback(self, msg):
        kvadrat = msg.data ** 2
        msg_out = Int32()
        msg_out.data = kvadrat
        self.publisher_.publish(msg_out)
        self.get_logger().info('Kvadrat broja %d je %d' % (msg.data, kvadrat))

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
