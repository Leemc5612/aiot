from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package="simpleRos", executable="hello_pub_class"),
        Node(package="simpleRos", executable="hello_sub")
        ])