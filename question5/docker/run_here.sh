#!/bin/bash
# Run from WSL (or Linux). Start Docker first. Allow GUI: xhost +local:docker

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
IMAGE="traveling_ethiopia_robot:noetic"

echo "Building image..."
docker build -t "$IMAGE" "$SCRIPT_DIR"

echo ""
echo "Starting container (project mounted at /project)."
echo "Inside the container, run:"
echo "  /project/docker/build_and_launch.sh"
echo "or copy package, catkin_make, then: roslaunch traveling_ethiopia_robot gazebo_world.launch"
echo ""

docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$PROJECT_DIR":/project:ro \
  "$IMAGE" \
  bash
