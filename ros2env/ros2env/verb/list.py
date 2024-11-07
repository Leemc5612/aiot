import os

from ros2env.verb import VerbExtension


def get_ros_env_list():
    ros_env_list = f"ROS_VERSION \t: {os.getenv('ROS_VERSION', 'None')}\n"
    ros_env_list += f"ROS_DISTRO \t: {os.getenv('ROS_DISTRO', 'None')}\n"
    ros_env_list += f"ROS_PYTHON_V \t : {os.getenv('ROS_PYTHON', 'None')}\n"
    return ros_env_list

def get_dds_env_list():
    ros_env_list = f"ROS_VERSION \t: {os.getenv('ROS_DOMAIN_ID', 'None')}\n"
    ros_env_list = f"DDS_VENDOR \t: {os.getenv('RMW_', 'None')}\n"

    return ros_env_list

def get_ros_env_list():
    ros_env_list = f"ROS_VERSION : {os.getenv('ROS_VERSION', 'None')}"
    return ros_env_list    

class ListVerb(VerbExtension):

    def add_arguments(self, parser, cli_name):
        parser.add_argument('-a', '--all', action ="store_true", help='display')

    def main(self, *, args):
        # message = None
        # if args.all:
        message = get_ros_env_list()
        print(message)