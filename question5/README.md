# Question 5: Interactive Intelligent Systems

Figure 5 is a relaxed state space graph for the Traveling Ethiopia search problem. This folder contains:

- **5.1** A three-wheel functional robot for Gazebo (physics + sensors)
- **5.2** A `.world` file with all Figure 5 states in a Cartesian coordinate system
- **5.3** A ROS-based class that uses uninformed search (BFS/DFS) to generate a path from any initial state to a goal state

---

## Structure

```
question5/
├── robot_description/
│   └── three_wheel_robot.urdf   # 5.1 Three-wheel robot (physics, sensors)
├── world/
│   ├── traveling_ethiopia.world # 5.2 World with all states (Cartesian)
│   └── figure5_states.py        # State coordinates and graph data
├── ros_package/                  # 5.3 ROS package
│   ├── package.xml
│   ├── CMakeLists.txt
│   ├── scripts/
│   │   ├── figure5_graph.py      # Figure 5 graph for path planner
│   │   └── path_planner.py      # Uninformed search (BFS/DFS) + ROS node
│   └── launch/
│       └── gazebo_world.launch  # Launch Gazebo world + spawn robot
└── README.md
```

---

## 5.1 Three-Wheel Robot (Gazebo)

- **URDF:** `robot_description/three_wheel_robot.urdf`
- **Layout:** Two driven front wheels (differential drive) + one passive rear wheel (caster).
- **Physics:** Inertial properties, collision, and `libgazebo_ros_diff_drive.so` for odometry and `cmd_vel`.
- **Sensors:**
  - **Proximity:** Ray sensor (laser) on `laser_link`, topic `scan` (`libgazebo_ros_ray_sensor.so`; on Melodic you may need `libgazebo_ros_laser.so`).
  - **Gyroscope/IMU:** `libgazebo_ros_imu.so`, topic `imu`.
  - **RGB camera:** `libgazebo_ros_camera.so` on `camera_link`, topics `image_raw`, `camera_info`.

---

## 5.2 World File (Figure 5 States)

- **File:** `world/traveling_ethiopia.world`
- **Format:** SDF 1.4; Cartesian coordinates (x, y, z) in meters.
- **Addis Ababa** at origin `(0, 0, 0.5)`; **Moyale** at `(4, -48, 0.5)`; other states placed to form the relaxed Figure 5 graph.
- **Physics:** ODE, gravity, realistic timestep and contact.

---

## 5.3 ROS Path Planner (Uninformed Search)

- **Class:** `UninformedSearchPathPlanner` in `ros_package/scripts/path_planner.py`
- **Graph:** Figure 5 relaxed state space in `figure5_graph.py` (same as in the world).
- **Strategies:** BFS or DFS; path from any initial state to any goal state in the graph.

**Without ROS (standalone):**

```bash
cd question5/ros_package/scripts
python path_planner.py
```

**With ROS:**

1. Copy the whole `question5` folder into your catkin source (e.g. `catkin_ws/src/question5`).
2. Build and source:

   ```bash
   cd catkin_ws
   catkin_make
   source devel/setup.bash
   ```

3. Launch Gazebo with the world and spawn the robot:

   ```bash
   roslaunch traveling_ethiopia_robot gazebo_world.launch
   ```

   (Package name is `traveling_ethiopia_robot`; the launch file lives in `question5/ros_package/launch` and is installed into the package share.)

4. In another terminal, run the path planner (default: Addis Ababa → Moyale, BFS). **The robot will automatically move along the planned path** (publishing `/cmd_vel`):

   ```bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

   Or with parameters:

   ```bash
   rosrun traveling_ethiopia_robot path_planner.py _initial_state:=Addis Ababa _goal_state:=Lalibela _strategy:=dfs
   ```

---

## Requirements

- **ROS:** Noetic or Melodic (with `gazebo_ros`)
- **Gazebo:** Gazebo 9+ (classic)
- **Python:** 3.x (for standalone path planner)

---

## ROS 2 (recommended on Ubuntu 24.04)

Use the **`ros2_package`** folder with **colcon** and **ROS 2** so you can run on Ubuntu 24.04 (Noble) without switching to Ubuntu 20.04:

```bash
# In WSL (Ubuntu 24.04): install ROS 2 Jazzy, Gazebo, colcon (see SETUP_GAZEBO.md)
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
cp -r "/mnt/c/Users/dawit/Desktop/ai pre/question5" .
ln -sf question5/ros2_package traveling_ethiopia_robot
cd ~/ros2_ws && colcon build --packages-select traveling_ethiopia_robot && source install/setup.bash
ros2 launch traveling_ethiopia_robot gazebo_world_launch.py
# In another terminal:
ros2 run traveling_ethiopia_robot path_planner --ros-args -p initial_state:=Addis\ Ababa -p goal_state:=Moyale -p strategy:=bfs
```

See **[SETUP_GAZEBO.md](SETUP_GAZEBO.md)** for full steps.

## Troubleshooting (WSL / Ubuntu 24.04)

If you see **`roslaunch` not found** or **`catkin_make` not found**, use the **ROS 2** workflow above (Option 1 in SETUP_GAZEBO.md). Alternatively:

- **Option 2 in SETUP_GAZEBO.md:** Use Ubuntu 20.04 in WSL and the **`ros_package`** (ROS 1 + catkin).

---

## Note

If your ROS distro uses the older laser plugin name, in `three_wheel_robot.urdf` change `libgazebo_ros_ray_sensor.so` to `libgazebo_ros_laser.so` in the proximity sensor block.
