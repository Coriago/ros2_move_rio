from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='move_rio',
            namespace='move_rio_ns',
            executable='talker',
            name='talker_node'
        ),
        Node(
            package='move_rio',
            namespace='move_rio_ns',
            executable='listener',
            name='listener_node'
        )
    ])