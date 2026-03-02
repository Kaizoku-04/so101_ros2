#!/usr/bin/env python3

from typing import Dict

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64


class JointStateToJointCmd(Node):
    def __init__(self) -> None:
        super().__init__('joint_state_to_joint_cmd')

        self.declare_parameter('robot_name', 'so101')
        robot_name = self.get_parameter('robot_name').get_parameter_value().string_value

        self._joint_publishers: Dict[str, object] = {}
        self._joint_names = [
            'shoulder_pan',
            'shoulder_lift',
            'elbow_flex',
            'wrist_flex',
            'wrist_roll',
            'gripper',
        ]

        for joint_name in self._joint_names:
            topic = f'/model/{robot_name}/joint/{joint_name}/0/cmd_pos'
            self._joint_publishers[joint_name] = self.create_publisher(Float64, topic, 10)

        self.create_subscription(JointState, '/joint_states', self._on_joint_states, 10)

    def _on_joint_states(self, msg: JointState) -> None:
        if not msg.name or not msg.position:
            return

        positions = dict(zip(msg.name, msg.position))

        for joint_name, publisher in self._joint_publishers.items():
            if joint_name not in positions:
                continue
            cmd = Float64()
            cmd.data = float(positions[joint_name])
            publisher.publish(cmd)


def main() -> None:
    rclpy.init()
    node = JointStateToJointCmd()
    try:
        rclpy.spin(node)
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
