# Question 5: Run and See the Effect

**5.1** Three-wheel robot (Gazebo) • **5.2** World file (Figure 5 Cartesian) • **5.3** ROS path planner (BFS/DFS)

---

## Option A: See the path (no Gazebo)

From the **project root** (`ai pre`):

```bash
# Path and waypoints for Addis Ababa → Moyale (BFS and DFS)
python question5/run_demo.py
```

Or run the path planner directly with custom start/goal:

```bash
python question5/ros_package/scripts/path_planner.py --initial "Addis Ababa" --goal "Moyale" --strategy bfs
python question5/ros_package/scripts/path_planner.py --initial "Addis Ababa" --goal "Lalibela" --strategy dfs
```

You will see the planned path and waypoints in Cartesian coordinates (Figure 5).

---

## Option B: See the robot move in Gazebo (Docker)

Requires **Docker** and **WSL** (or Linux) with X11 so the Gazebo window can open.

### 1. First-time setup (WSL)

```bash
xhost +local:docker
cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
docker build -t traveling_ethiopia_robot:noetic .
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash
```

Inside the container:

```bash
bash /project/docker/build_and_launch.sh
roslaunch traveling_ethiopia_robot gazebo_world.launch
```

Leave this terminal open (Gazebo with the world and robot).

### 2. Run the path planner (second terminal)

Open a **second** WSL terminal:

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && rosrun traveling_ethiopia_robot path_planner.py"
```

The robot will drive along the planned path (Addis Ababa → … → Moyale) using `/cmd_vel`.

### 3. Custom initial/goal (in the second container)

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && rosrun traveling_ethiopia_robot path_planner.py _initial_state:=Addis\ Ababa _goal_state:=Lalibela _strategy:=dfs"
```

---

## What you have

| Part | What it is |
|------|------------|
| **5.1** | `robot_description/three_wheel_robot.urdf` — three wheels, diff drive, **proximity (ray)**, **gyroscope (IMU)**, **RGB camera**, physics |
| **5.2** | `world/traveling_ethiopia.world` — all Figure 5 states as boxes in **Cartesian coordinates** |
| **5.3** | `ros_package/scripts/path_planner.py` — **uninformed search (BFS/DFS)** from any initial state to any goal, publishes path and drives the robot via `cmd_vel` |

Full Docker steps: **question5/docker/STEP_BY_STEP.md**
