# so101_bringup

Launch helpers and startup scripts for the SO-101 ROS 2 stack.

## Gazebo launcher script

After building and sourcing your workspace, you can launch Gazebo with:

```bash
ros2 run so101_bringup so101_gazebo.sh
```

Environment overrides:

- `SO101_WORLD` (default: `pick_and_place_demo.world`)
- `SO101_USE_CAMERA` (default: `false`)
- `SO101_USE_RVIZ` (default: `true`)

Example:

```bash
SO101_WORLD=empty.world SO101_USE_RVIZ=false ros2 run so101_bringup so101_gazebo.sh
```
