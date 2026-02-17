# Step-by-Step: Run Question 5 with Docker (Gazebo + ROS Noetic)

Follow these steps in order. **Project is always mounted at `/project`** (the `question5` folder: `ros_package`, `world`, `robot_description`, etc.).

---

## Quick run (after first-time setup)

If you already built the image and ran `build_and_launch.sh` once (with a persistent volume), you can start Gazebo with:

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && roslaunch traveling_ethiopia_robot gazebo_world.launch"
```

Path planner (second terminal):

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && rosrun traveling_ethiopia_robot path_planner.py"
```

---

## First-time setup

### Step 1: Start Docker and allow GUI

- **Docker in Ubuntu (WSL or native):**  
  `sudo systemctl start docker` (or `sudo service docker start`).  
  Then: `sudo apt install -y x11-xserver-utils` and **`xhost +local:docker`**
- **Windows + Docker Desktop:** Start Docker Desktop. For Gazebo window you need an X server (e.g. VcXsrv) and set `DISPLAY` in WSL if you use WSL.

Check Docker: `docker --version`

---

### Step 2: Go to project folder

In WSL (or Linux), your Windows path `C:\Users\dawit\Desktop\ai pre\question5` is:

```bash
cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
```

If the project is inside Ubuntu (e.g. `~/question5`), use:

```bash
cd ~/question5/docker
```

---

### Step 3: Build the Docker image

```bash
docker build -t traveling_ethiopia_robot:noetic .
```

Wait until you see “Successfully built” and “Successfully tagged”.

---

### Step 4: Run the container and get a shell

Use the path that matches your setup. **WSL with project on Windows disk:**

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash
```

**If the project is in Ubuntu (e.g. ~/question5):**

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "$HOME/question5":/project:ro \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash
```

You should get a prompt like `root@...` — you are **inside the container**.

---

### Step 5: Inside the container — build the package

Run the helper script (it copies the package from `/project`, fixes paths, and runs `catkin_make`):

```bash
bash /project/docker/build_and_launch.sh
```

If you see “Error: /project not mounted”, exit the container and start it again with the `-v ...:/project:ro` option from Step 4.

When the script finishes, you get a shell with the workspace built and sourced.

---

### Step 6: Launch Gazebo

In the **same** container:

```bash
roslaunch traveling_ethiopia_robot gazebo_world.launch
```

Gazebo should open with the Figure 5 world and the three-wheel robot. Leave this terminal running.

---

### Step 7: Run the path planner (second terminal)

1. Open a **second** WSL/terminal window.
2. Start another container that uses the **same** workspace volume (no need to mount `/project` or rebuild):

   ```bash
   docker run -it --rm --network host \
     -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     -v traveling_ethiopia_ws:/catkin_ws \
     traveling_ethiopia_robot:noetic \
     bash
   ```

3. Inside this second container:

   ```bash
   source /catkin_ws/devel/setup.bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

You should see the planned path (e.g. Addis Ababa → … → Moyale) and the robot will move along it.

---

## Using docker-compose

From `question5/docker`:

```bash
# Allow GUI
xhost +local:docker

# Build and run a shell (project and workspace volume are set by compose)
docker-compose run --rm rosnoetic bash
```

Inside the container:

```bash
bash /project/docker/build_and_launch.sh
roslaunch traveling_ethiopia_robot gazebo_world.launch
```

In a second terminal (same workspace volume):

```bash
docker-compose run --rm rosnoetic bash -c "source /catkin_ws/devel/setup.bash && rosrun traveling_ethiopia_robot path_planner.py"
```

**Note:** On WSL/Linux, the compose file mounts `/tmp/.X11-unix` for the Gazebo window. On Windows (PowerShell) without WSL, that path may not exist; use the `docker run` flow from Steps 4–7 and see README_DOCKER.md for DISPLAY.

---

## If Gazebo doesn’t open (DISPLAY)

- In WSL, run: `echo $DISPLAY`. If empty, try:
  ```bash
  export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
  ```
  Then run `xhost +local:docker` again and start the container.
- On **Windows 10** you may need **VcXsrv** or **X410** and set DISPLAY to your Windows IP.

---

## Checklist

| Step | What to do |
|------|------------|
| 1 | Start Docker, run `xhost +local:docker` |
| 2 | `cd question5/docker` |
| 3 | `docker build -t traveling_ethiopia_robot:noetic .` |
| 4 | `docker run -it --rm ... -v ...:/project:ro -v traveling_ethiopia_ws:/catkin_ws ... bash` |
| 5 | Inside: `bash /project/docker/build_and_launch.sh` |
| 6 | Inside: `roslaunch traveling_ethiopia_robot gazebo_world.launch` |
| 7 | Second terminal: new container with same volume, then `source devel/setup.bash` and `rosrun traveling_ethiopia_robot path_planner.py` |

You’re done when Gazebo shows the world and robot, and the path planner runs in the second terminal with the robot moving along the path.
