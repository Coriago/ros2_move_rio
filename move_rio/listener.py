import rclpy
from rclpy.node import Node
from rclpy import qos
# from rclpy.duration import Duration
from std_msgs.msg import Float32


class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')

        qos_profile = qos.QoSProfile(
            depth=1,
            reliability=qos.ReliabilityPolicy.BEST_EFFORT,
            durability=qos.DurabilityPolicy.VOLATILE,
        )

        self.subscription = self.create_subscription(Float32, 'joy_control', self.listener_callback,  qos_profile)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        print('test')
        self.get_logger().info('I heard: "%s"' % msg.data)


def main(args=None):
    print('Starting..')
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()