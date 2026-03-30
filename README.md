# SO101 ROS 2 

## Overview
The `so101_ros2` project contains the ROS 2 packages for the SO101 open-source robotic arm. This workspace provides a comprehensive simulation environment for a 6-DOF robotic arm equipped with a gripper. It includes the robot's physical URDF description, comprehensive 3D meshes, RViz configurations, and a full Gazebo simulation setup utilizing ROS 2 Control (`gz_ros2_control`).

## Architecture
The workspace is structured into the following main packages:
- **`so101_bringup`**: Contains top-level convenience scripts (`so101_gazebo.sh`) to quickly start the simulation and visualization environments.
- **`so101_description`**: Contains the physical description of the robot, including the URDF (written in Xacro format) and 3D STL meshes for all links (base, shoulder, upper arm, lower arm, wrist, and moving jaw). It also contains the RViz default configurations and the `robot_state_publisher` launch sequence.
- **`so101_gazebo`**: Provides the primary simulation environment setup for Gazebo. Features include launch files to spawn the robot, control configurations (`ros2_controllers.yaml` for joint trajectory controllers), various world files (e.g., `pick_and_place_demo.world`), and residential simulation models. It bridges ROS 2 and Gazebo using `ros_gz_bridge` and `ros_gz_image`.
- **`so101_ros2`**: A metapackage that aggregates the dependencies of the aforementioned modules.

The robot itself is a 6-DOF arm modeling `sts3215` servo motors. The controllable joints are `shoulder_pan`, `shoulder_lift`, `elbow_flex`, `wrist_flex`, `wrist_roll`, and `gripper`. Operation of the arm and gripper in simulation is handled by standard `joint_trajectory_controller` instances (`arm_controller` and `gripper_controller`).

## Getting Started

### Prerequisites
- **Operating System:** Ubuntu 24.04
- **ROS 2:** Jazzy 
- **Gazebo Sim:** Harmonic

Ensure you have the required ROS 2 packages installed:
```bash
sudo apt update
sudo apt install ros-jazzy-ros-gz-sim ros-jazzy-ros-gz-bridge ros-jazzy-ros-gz-image
sudo apt install ros-jazzy-gz-ros2-control ros-jazzy-ros2-control ros-jazzy-ros2-controllers
sudo apt install ros-jazzy-joint-state-publisher-gui ros-jazzy-xacro
```

### Installation
1. Source your ROS 2 environment:
   ```bash
   source /opt/ros/jazzy/setup.bash
   ```
2. Create a colcon workspace (if you haven't already) and clone this repository:
   ```bash
   mkdir -p ~/so101_ws/src
   cd ~/so101_ws/src
   # Clone the repository here...
   ```
3. Install missing ROS dependencies automatically using `rosdep`:
   ```bash
   cd ~/so101_ws
   rosdep update
   rosdep install --from-paths src --ignore-src -r -y
   ```
4. Build the workspace:
   ```bash
   colcon build
   ```

## Usage

1. Source the workspace overlay:
   ```bash
   source ~/so101_ws/install/setup.bash
   ```

2. **Launch the Gazebo simulation:**
   The easiest way to launch the simulated robot in a pick-and-place environment is by using the provided bash script, which natively handles ROS environment sourcing and default arguments:
   ```bash
   ./src/so101_ros2/so101_bringup/scripts/so101_gazebo.sh
   ```
   **Alternatively**, you can use the standard ROS 2 launch command:
   ```bash
   ros2 launch so101_gazebo so101.gazebo.launch.py
   ```
   *Optional Launch Arguments:*
   - `world_file`: Set the Gazebo world file (default: `pick_and_place_demo.world`).
   - `use_camera`: (Not implemented yet) Enable the RGBD camera frame bridging (`true`/`false`, default: `false`).
   - `use_rviz`: Open RViz for standard ROS 2 visualization (`true`/`false`, default: `true`).