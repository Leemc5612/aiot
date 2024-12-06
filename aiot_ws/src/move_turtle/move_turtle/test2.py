import rclpy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

MAX_VEL = 1.0
TARGET_DISTANCE = 1.0  # 1 meter

class Move_turtle(Node):
    def __init__(self):
        super().__init__("hello_pub")
        self.create_timer(0.1, self.twist_pub)
        self.create_timer(1 / 60, self.update)
        self.pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.create_subscription(LaserScan, "/scan", self.laser_callback, 10)
        self.create_subscription(Odometry, "/odom", self.odom_callback, 10)
        
        self.twist = Twist()
        self.start_position = None
        self.distance_travelled = 0.0

    def twist_pub(self):
        self.restrain()
        self.pub.publish(self.twist)

    def laser_callback(self, msg: LaserScan):
        # 필요한 데이터만 사용
        pass

    def odom_callback(self, msg: Odometry):
        if self.start_position is None:
            self.start_position = msg.pose.pose.position
        else:
            # 거리 계산
            delta_x = msg.pose.pose.position.x - self.start_position.x
            delta_y = msg.pose.pose.position.y - self.start_position.y
            self.distance_travelled = math.sqrt(delta_x**2 + delta_y**2)

    def update(self):
        if self.distance_travelled < TARGET_DISTANCE:
            self.twist.linear.x = 0.1  # 속도
        else:
            self.twist.linear.x = 0.0  # 목표 거리 도달 후 멈춤
            rclpy.shutdown()  # 종료

    def restrain(self):
        # 속도 제한
        self.twist.linear.x = min(max(self.twist.linear.x, -MAX_VEL), MAX_VEL)

def main():
    rclpy.init()
    node = Move_turtle()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.pub.publish(Twist())  # 멈추기
        node.destroy_node()

if __name__ == "__main__":
    main()
