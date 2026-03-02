#!/usr/bin/env bash
set -eo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

ROS_DISTRO_DEFAULT="${ROS_DISTRO:-jazzy}"
ROS_SETUP="/opt/ros/${ROS_DISTRO_DEFAULT}/setup.bash"
LOCAL_SETUP="${WORKSPACE_ROOT}/install/setup.bash"
  
if [[ -f "${ROS_SETUP}" ]]; then
  # shellcheck disable=SC1090
  source "${ROS_SETUP}"
else
  echo "[ERROR] ROS setup not found: ${ROS_SETUP}" >&2
  echo "Set ROS_DISTRO to your installed distro (e.g. humble, jazzy) and try again." >&2
  exit 1
fi

if [[ -f "${LOCAL_SETUP}" ]]; then
  # shellcheck disable=SC1090
  source "${LOCAL_SETUP}"
else
  echo "[WARN] Workspace overlay not found: ${LOCAL_SETUP}" >&2
  echo "[WARN] Launching with underlay only. Build this workspace first if package is not found." >&2
fi

WORLD_FILE="${SO101_WORLD:-pick_and_place_demo.world}"
USE_CAMERA="${SO101_USE_CAMERA:-false}"
USE_RVIZ="${SO101_USE_RVIZ:-true}"

exec ros2 launch so101_gazebo so101.gazebo.launch.py \
  world_file:="${WORLD_FILE}" \
  use_camera:="${USE_CAMERA}" \
  use_rviz:="${USE_RVIZ}" \
  "$@"
