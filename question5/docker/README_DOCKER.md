# Run Question 5 with Docker (Ubuntu 20.04 + ROS Noetic)

You keep **Ubuntu 24** (or WSL) as your host. Inside Docker you run **Ubuntu 20.04 + ROS Noetic** and use `roslaunch` and Gazebo as usual.

**How to run (WSL/Linux):** See **STEP_BY_STEP.md** for the full flow. In short: build image → run container with project + workspace volume → inside run `bash /project/docker/build_and_launch.sh` → `roslaunch traveling_ethiopia_robot gazebo_world.launch` → in a second terminal run another container and `rosrun traveling_ethiopia_robot path_planner.py`.

---

## Prerequisites

- Docker installed (you said this is already done).
- On **WSL2**: allow GUI apps (X server). Either:
  - Install **WSLg** (Windows 11): usually works without extra steps, or
  - Install **VcXsrv** or **X410** on Windows and set `DISPLAY` in WSL to point to it.

---

## Step 1: Allow Docker to show GUI (X11)

On your **host** (WSL2 Ubuntu or Linux), in a terminal:

```bash
# Allow Docker to connect to your X server (so Gazebo can open a window)
xhost +local:docker
```

If `xhost` is not found, install it:

```bash
sudo apt install x11-xserver-utils
xhost +local:docker
```

On **Windows with WSL2**: if you use WSLg, often nothing else is needed. If Gazebo doesn’t open, install VcXsrv, start “XLaunch”, then in WSL:

```bash
export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
xhost +local:docker
```

---

## Step 2: Build the Docker image

From your project root (the folder that contains `question5`):

```bash
cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
docker build -t traveling_ethiopia_robot:noetic .
```

Wait until the build finishes.

---

## Step 3: Run the container and set up the workspace

Run a shell inside the container and mount the project:

```bash
cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
docker run -it --rm \
  --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
  traveling_ethiopia_robot:noetic \
  bash
```

You are now inside the container. Then:

```bash
# Copy package into workspace and build (first time only)
cp -r /project/ros_package /catkin_ws/src/traveling_ethiopia_robot
mkdir -p /catkin_ws/src/traveling_ethiopia_robot/worlds /catkin_ws/src/traveling_ethiopia_robot/urdf
cp /project/world/traveling_ethiopia.world /catkin_ws/src/traveling_ethiopia_robot/worlds/
cp /project/robot_description/three_wheel_robot.urdf /catkin_ws/src/traveling_ethiopia_robot/urdf/

# Fix CMakeLists paths (use local worlds/ and urdf/)
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt

# Build
cd /catkin_ws
source /opt/ros/noetic/setup.bash
catkin_make
source devel/setup.bash
```

---

## Step 4: Launch Gazebo inside the container

Still inside the same container:

```bash
source /catkin_ws/devel/setup.bash
roslaunch traveling_ethiopia_robot gazebo_world.launch
```

Gazebo should open with the Figure 5 world and the robot.

---

## Step 5: Run the path planner (second terminal)

Open a **second terminal** on your host. Attach to the **same** running container (if you left it running) or start a new one that shares the same workspace.

**Option A – New container, same workspace (use a volume):**

First time you must have built in a container that used a volume (see “Optional: persist workspace” below). Then run a second container with the same volume and run the planner:

```bash
docker run -it --rm \
  --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && rosrun traveling_ethiopia_robot path_planner.py"
```

**Option B – Same container:**  
If you only closed Gazebo but the first container is still open, in that same container run:

```bash
source /catkin_ws/devel/setup.bash
rosrun traveling_ethiopia_robot path_planner.py
```

---

## Optional: persist workspace (so you don’t rebuild every time)

First time, run with a named volume and build once:

```bash
docker run -it --rm \
  --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash
```

Inside the container, run the same copy + `catkin_make` + `source` as in Step 3. After that, next time you can start with:

```bash
docker run -it --rm \
  --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && roslaunch traveling_ethiopia_robot gazebo_world.launch"
```

No need to copy or build again.

---

## Quick reference

| Step | Command |
|------|--------|
| 1. X11 | `xhost +local:docker` |
| 2. Build image | `cd question5/docker && docker build -t traveling_ethiopia_robot:noetic .` |
| 3. Run container | `docker run -it --rm --network host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v "/path/to/question5":/project:ro -v traveling_ethiopia_ws:/catkin_ws traveling_ethiopia_robot:noetic bash` |
| 4. Inside: build | `bash /project/docker/build_and_launch.sh` |
| 5. Inside: Gazebo | `roslaunch traveling_ethiopia_robot gazebo_world.launch` |
| 6. Path planner | Second terminal: new container with `-v traveling_ethiopia_ws:/catkin_ws`, then `source devel/setup.bash` and `rosrun traveling_ethiopia_robot path_planner.py` |

For a full walkthrough, see **STEP_BY_STEP.md**.
