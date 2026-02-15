# Gazebo + ROS Setup for Question 5

You can run the Gazebo world and path planner in three ways:

- **Option 1 (recommended if you stay on Ubuntu 24):** Use **Docker** with Ubuntu 20.04 + ROS Noetic inside the container → use `roslaunch` normally.
- **Option 2:** Use **ROS 2** and **colcon** with the `ros2_package` on Ubuntu 24.04 (no Docker).
- **Option 3:** Use **ROS 1 (Noetic)** natively with the `ros_package` — requires Ubuntu 20.04 in WSL.

---

## Option 1: Docker — Ubuntu 20.04 + ROS Noetic (keep Ubuntu 24 as host)

You keep Ubuntu 24 as your host. Inside a Docker container you run Ubuntu 20.04 + ROS Noetic and use `roslaunch` and Gazebo as usual.

**Full step-by-step:** see **[docker/STEP_BY_STEP.md](docker/STEP_BY_STEP.md)** (recommended) or [docker/README_DOCKER.md](docker/README_DOCKER.md).

### Short version

1. **Allow GUI from Docker (once per session):**
   ```bash
   sudo apt install -y x11-xserver-utils   # if needed
   xhost +local:docker
   ```

2. **Build the image:**
   ```bash
   cd question5/docker
   docker build -t traveling_ethiopia_robot:noetic .
   ```

3. **Run container and mount project:**
   ```bash
   cd question5/docker
   docker run -it --rm --network host -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
     traveling_ethiopia_robot:noetic bash
   ```

4. **Inside the container — copy package, build, launch:**
   ```bash
   cp -r /project/ros_package /catkin_ws/src/traveling_ethiopia_robot
   mkdir -p /catkin_ws/src/traveling_ethiopia_robot/worlds /catkin_ws/src/traveling_ethiopia_robot/urdf
   cp /project/world/traveling_ethiopia.world /catkin_ws/src/traveling_ethiopia_robot/worlds/
   cp /project/robot_description/three_wheel_robot.urdf /catkin_ws/src/traveling_ethiopia_robot/urdf/
   sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
   sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
   cd /catkin_ws && source /opt/ros/noetic/setup.bash && catkin_make && source devel/setup.bash
   roslaunch traveling_ethiopia_robot gazebo_world.launch
   ```

5. **Path planner (in the same container, or a second terminal with a new container using the same volume):**
   ```bash
   source /catkin_ws/devel/setup.bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

On **WSL2**: if Gazebo doesn’t open, set `DISPLAY` (see docker/README_DOCKER.md).  
For persistent workspace (no rebuild each time), use a Docker volume — see docker/README_DOCKER.md.

---

## Option 2: ROS 2 on Ubuntu 24.04 (Noble) — no Docker

This uses the **`question5/ros2_package`** folder. It works on your current Ubuntu 24.04 (Noble) with ROS 2 Jazzy or Humble.

### 1. Install ROS 2 and Gazebo (in WSL Ubuntu)

```bash
# Install ROS 2 Jazzy (for Ubuntu 24.04)
sudo apt update
sudo apt install ros-jazzy-desktop

# Or ROS 2 Humble (if you use Ubuntu 22.04):
# sudo apt install ros-humble-desktop

# Install Gazebo Classic (for the SDF 1.4 world file)
sudo apt install gazebo libgazebo-dev

# Install colcon and other build tools
sudo apt install python3-colcon-common-extensions python3-ament-index-python

# Add to .bashrc so ROS 2 is sourced automatically
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

### 2. Copy the ROS 2 package into a workspace

```bash
mkdir -p ~/ros2_ws/src
cd ~/ros2_ws/src

# Copy the whole question5 folder from Windows (adjust path if needed)
cp -r "/mnt/c/Users/dawit/Desktop/ai pre/question5" .

# The ROS 2 package is inside question5 — create a link so colcon finds it
ln -sf question5/ros2_package traveling_ethiopia_robot
```

### 3. Build with colcon

```bash
cd ~/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build --packages-select traveling_ethiopia_robot
source install/setup.bash
```

### 4. Run the Gazebo world

```bash
source ~/ros2_ws/install/setup.bash
ros2 launch traveling_ethiopia_robot gazebo_world_launch.py
```

You should see Gazebo open with the Figure 5 state space (colored boxes for each city).

### 5. Run the path planner (in another terminal)

```bash
source ~/ros2_ws/install/setup.bash
ros2 run traveling_ethiopia_robot path_planner --ros-args -p initial_state:=Addis\ Ababa -p goal_state:=Moyale -p strategy:=bfs
```

To use a different strategy or goal:

```bash
ros2 run traveling_ethiopia_robot path_planner --ros-args \
  -p initial_state:=Addis\ Ababa -p goal_state:=Lalibela -p strategy:=dfs
```

The planned path is published on the `/planned_path` topic.

### If `gazebo` is not available on Ubuntu 24.04

If `sudo apt install gazebo` fails, you can still run the world with **Gazebo Sim (gz sim)** if installed:

```bash
sudo apt install gz-harmonic
```

Then run the world manually (the launch file uses `gazebo` by default):

```bash
source ~/ros2_ws/install/setup.bash
# Get path to installed world file
WORLD=$(ros2 pkg prefix traveling_ethiopia_robot)/share/traveling_ethiopia_robot/worlds/traveling_ethiopia.world
gz sim $WORLD
```

Note: `gz sim` may require a newer SDF format; if it fails, use Gazebo Classic (`gazebo`) when available.

---

## Option 3: ROS 1 (Noetic) on Ubuntu 20.04 (native WSL)

Use this if you prefer the original **`ros_package`** (catkin, `roslaunch`).

1. **Install Ubuntu 20.04 in WSL:**
   ```bash
   wsl --install -d Ubuntu-20.04
   ```
   Open **Ubuntu 20.04** from the Start menu.

2. **Inside Ubuntu 20.04**, install ROS Noetic and Gazebo:
   ```bash
   sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu focal main" > /etc/apt/sources.list.d/ros-latest.list'
   curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
   sudo apt update
   sudo apt install ros-noetic-desktop-full
   sudo apt install ros-noetic-gazebo-ros-pkgs ros-noetic-gazebo-ros-control
   ```

3. **Create workspace and copy package:**
   ```bash
   source /opt/ros/noetic/setup.bash
   mkdir -p ~/catkin_ws/src
   cd ~/catkin_ws/src
   cp -r "/mnt/c/Users/dawit/Desktop/ai pre/question5" .
   mv question5/ros_package traveling_ethiopia_robot
   mkdir -p traveling_ethiopia_robot/worlds traveling_ethiopia_robot/urdf
   cp question5/world/traveling_ethiopia.world traveling_ethiopia_robot/worlds/
   cp question5/robot_description/three_wheel_robot.urdf traveling_ethiopia_robot/urdf/
   ```

4. **Build and run:**
   ```bash
   cd ~/catkin_ws
   catkin_make
   source devel/setup.bash
   roslaunch traveling_ethiopia_robot gazebo_world.launch
   ```

5. **Path planner (other terminal):**
   ```bash
   source ~/catkin_ws/devel/setup.bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

---

## Summary

| Your system              | Use this |
|--------------------------|----------|
| **Ubuntu 24.04, want roslaunch** | **Option 1:** Docker (Ubuntu 20.04 + ROS Noetic in container) |
| **Ubuntu 24.04, no Docker**      | **Option 2:** `ros2_package` + colcon + ROS 2 |
| **Ubuntu 20.04 (native WSL)**    | **Option 3:** `ros_package` + catkin + ROS 1 Noetic |
