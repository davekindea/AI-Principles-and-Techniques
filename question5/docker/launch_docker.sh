#!/bin/bash
PROJECT_DIR="/mnt/c/Users/dawit/Desktop/ai pre/question5"
docker run -d --name ethiopia_sim \
    --network host \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v "$PROJECT_DIR":/project:ro \
    traveling_ethiopia_robot:noetic \
    sleep infinity
