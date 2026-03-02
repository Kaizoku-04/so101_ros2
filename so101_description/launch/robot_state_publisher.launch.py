from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import Command, LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description() -> LaunchDescription:
    use_sim_time = LaunchConfiguration('use_sim_time')
    use_joint_state_gui = LaunchConfiguration('use_joint_state_gui')
    use_rviz = LaunchConfiguration('use_rviz')
    rviz_config = LaunchConfiguration('rviz_config')

    robot_description = Command([
        'xacro ',
        PathJoinSubstitution([
            FindPackageShare('so101_description'),
            'urdf',
            'robots',
            'so101.urdf',
        ]),
    ])

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulated clock if true',
        ),
        DeclareLaunchArgument(
            'use_joint_state_gui',
            default_value='true',
            description='Launch joint_state_publisher_gui',
        ),
        DeclareLaunchArgument(
            'use_rviz',
            default_value='true',
            description='Launch RViz2',
        ),
        DeclareLaunchArgument(
            'rviz_config',
            default_value=PathJoinSubstitution([
                FindPackageShare('so101_description'),
                'rviz',
                'so101_description.rviz',
            ]),
            description='Absolute path to RViz config file',
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            output='screen',
            parameters=[
                {'use_sim_time': use_sim_time},
                {'robot_description': robot_description},
            ],
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen',
            condition=IfCondition(use_joint_state_gui),
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config],
            condition=IfCondition(use_rviz),
        ),
    ])
