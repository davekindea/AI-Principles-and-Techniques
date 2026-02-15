# Step-by-Step: Run Question 5 with Docker (Gazebo + ROS Noetic)

Follow these steps in order.

---

## If you installed Docker inside Ubuntu (WSL or native Ubuntu)

You can skip “Docker Desktop” and “Open WSL”. Do this instead:

1. **Start Docker daemon** (if it’s not already running):
   ```bash
   sudo systemctl start docker
   ```
   Or: `sudo service docker start`

2. **Check Docker works:**
   ```bash
   docker --version
   docker run hello-world
   ```

3. **Optional:** Allow your user to run Docker without `sudo`:
   ```bash
   sudo usermod -aG docker $USER
   ```
   Then log out and log back in (or restart WSL).

4. **Project path:**
   - If the project is on the **Windows disk** and you’re in WSL, use:
     ```bash
     cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
     ```
     and use `/project` as in the steps below (the `docker run` mounts this folder as `/project`).
   - If you **copied the project into Ubuntu** (e.g. `~/question5`), use:
     ```bash
     cd ~/question5/docker
     ```
     and in `docker run` use: `-v "$HOME/question5":/project:ro` instead of the `/mnt/c/...` path.

Then continue from **Step 3** (Allow Docker to show GUI) below.

---

## Step 1: Start Docker

- **Docker inside Ubuntu (WSL or native):** Run `sudo systemctl start docker` (or `sudo service docker start`). Then run `docker --version`.
- **Windows with Docker Desktop:** Open Docker Desktop and wait until it says “Docker Desktop is running”. Then run `docker --version`.

You should see something like `Docker version 24.x.x`.

---

## Step 2: Open a terminal in Ubuntu

- **WSL:** Open “Ubuntu” from the Start menu or run `wsl`.
- **Native Ubuntu:** Open the Terminal app.
- You should see a prompt like `yourname@hostname:~$`.

---

## Step 3: Allow Docker to show GUI (Gazebo window)

In the WSL terminal, run:

```bash
sudo apt install -y x11-xserver-utils
xhost +local:docker
```

If it says “unable to open display”, you may need to set DISPLAY (see the note at the end).

---

## Step 4: Go to the project folder in WSL

Your Windows folder `C:\Users\dawit\Desktop\ai pre\question5` is available in WSL as:

```bash
cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"
```

Check you are in the right place:

```bash
ls
```

You should see `Dockerfile`, `docker-compose.yml`, `README_DOCKER.md`, etc.

---

## Step 5: Build the Docker image

Still in `question5/docker`, run:

```bash
docker build -t traveling_ethiopia_robot:noetic .
```

Wait until it finishes (first time can take several minutes). You should see “Successfully built” and “Successfully tagged”.

---

## Step 6: Run the container and get a shell inside it

Run (use one line, or copy the whole block):

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
  traveling_ethiopia_robot:noetic \
  bash
```

You should see a new prompt like `root@...` — you are now **inside the container**.

---

## ⚠️ "No such file or directory" for /project/... ?

That means the project was **not mounted** at `/project`, or the wrong folder was mounted.

**1. Check what’s inside /project:**
```bash
ls -la /project
```
- If you see **`No such file or directory`**: the container was started **without** the volume. Exit with `exit`, then start the container again with the exact `docker run` command from **Step 6** (including the `-v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro` part).
- If you see **`question5`** (and no `world` or `ros_package` directly): the **parent folder** was mounted. Use **PROJ=/project/question5** in the commands below.
- If you see **`world`**, **`ros_package`**, **`robot_description`**: use **PROJ=/project**.

**2. Set PROJ and copy (run in one go):**
```bash
# If /project has world, ros_package, robot_description directly:
PROJ=/project
# OR if /project only has question5 inside it, use:
# PROJ=/project/question5

cp -r $PROJ/ros_package /catkin_ws/src/traveling_ethiopia_robot
mkdir -p /catkin_ws/src/traveling_ethiopia_robot/worlds /catkin_ws/src/traveling_ethiopia_robot/urdf
cp $PROJ/world/traveling_ethiopia.world /catkin_ws/src/traveling_ethiopia_robot/worlds/
cp $PROJ/robot_description/three_wheel_robot.urdf /catkin_ws/src/traveling_ethiopia_robot/urdf/
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
```

---

## ✅ Already did apt install + catkin_make? Do the rest now

If you are **inside the container** and already ran `apt update`, `apt install -y python3-catkin-tools build-essential ros-noetic-catkin`, and `catkin_make` in `~/catkin_ws`, do the following.

**1. Copy the package and world/URDF (if not done yet).**  
First set **PROJ**: run `ls /project`. If you see `question5` only, set `PROJ=/project/question5`. If you see `world`, `ros_package`, `robot_description`, set `PROJ=/project`. Then:
```bash
PROJ=/project
# or: PROJ=/project/question5   (if you mounted the parent "ai pre" folder)
cp -r $PROJ/ros_package /catkin_ws/src/traveling_ethiopia_robot
mkdir -p /catkin_ws/src/traveling_ethiopia_robot/worlds /catkin_ws/src/traveling_ethiopia_robot/urdf
cp $PROJ/world/traveling_ethiopia.world /catkin_ws/src/traveling_ethiopia_robot/worlds/
cp $PROJ/robot_description/three_wheel_robot.urdf /catkin_ws/src/traveling_ethiopia_robot/urdf/
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
```

**2. Build again (so the package is compiled):**
```bash
cd /catkin_ws
source /opt/ros/noetic/setup.bash
catkin_make
source devel/setup.bash
```

**3. Launch Gazebo:**
```bash
roslaunch traveling_ethiopia_robot gazebo_world.launch
```

**4. Path planner (in the same container, or a second terminal/container):**
```bash
source /catkin_ws/devel/setup.bash
rosrun traveling_ethiopia_robot path_planner.py
```

---

## Step 7: Inside the container — make the package visible and add world/urdf

Catkin only sees packages that are **directly under** `src/`. Your package is in `question5/ros_package`, so create a **symlink** named `traveling_ethiopia_robot` and add `worlds/` and `urdf/`:

```bash
cd /catkin_ws/src
ln -sf question5/ros_package traveling_ethiopia_robot
mkdir -p traveling_ethiopia_robot/worlds traveling_ethiopia_robot/urdf
cp question5/world/traveling_ethiopia.world traveling_ethiopia_robot/worlds/
cp question5/robot_description/three_wheel_robot.urdf traveling_ethiopia_robot/urdf/
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' traveling_ethiopia_robot/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' traveling_ethiopia_robot/CMakeLists.txt
```

If your project is mounted at `/project` (and you don’t have `question5` in src), use this instead:

```bash
cd /catkin_ws/src
cp -r /project/ros_package traveling_ethiopia_robot
mkdir -p traveling_ethiopia_robot/worlds traveling_ethiopia_robot/urdf
cp /project/world/traveling_ethiopia.world traveling_ethiopia_robot/worlds/
cp /project/robot_description/three_wheel_robot.urdf traveling_ethiopia_robot/urdf/
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g' traveling_ethiopia_robot/CMakeLists.txt
sed -i 's|${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g' traveling_ethiopia_robot/CMakeLists.txt
```

---

## Step 8: Inside the container — build the workspace

```bash
cd /catkin_ws
```

```bash
source /opt/ros/noetic/setup.bash
```

```bash
catkin_make
```

Wait until it finishes with “Build succeeded” (or similar). Then:

```bash
source devel/setup.bash
```

---

## Step 9: Launch Gazebo (world + robot)

Still inside the same container:

```bash
roslaunch traveling_ethiopia_robot gazebo_world.launch
```

Gazebo should open with the Figure 5 world and the three-wheel robot. Leave this terminal running.

---

## Step 10: Run the path planner (second terminal)

1. Open a **second** WSL terminal (new tab or window).
2. Run the same `docker run` command as in Step 6 to start another container:
   ```bash
   docker run -it --rm --network host \
     -e DISPLAY=$DISPLAY \
     -v /tmp/.X11-unix:/tmp/.X11-unix \
     -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
     -v traveling_ethiopia_ws:/catkin_ws \
     traveling_ethiopia_robot:noetic \
     bash
   ```
   **Note:** This uses a volume `traveling_ethiopia_ws` so the second container can use the same built workspace. So the **first time** you do this, you should have run Step 6 with the volume. See “Optional: use a volume” below.

   **Simpler option:** If you only have one container running (Gazebo), open a **new terminal**, run the same `docker run` command **without** the extra volume. Then inside that new container you must repeat Steps 7 and 8 (copy package, build), then run:
   ```bash
   source /catkin_ws/devel/setup.bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

3. If your **first** container was started **with** the volume (see below), then in the second container run only:
   ```bash
   source /catkin_ws/devel/setup.bash
   rosrun traveling_ethiopia_robot path_planner.py
   ```

You should see the planned path (e.g. Addis Ababa → … → Moyale) in the terminal.

---

## Optional: Use a volume so you don’t rebuild every time

**First time only**, run the container with a named volume and do Steps 7–8 inside it:

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v "/mnt/c/Users/dawit/Desktop/ai pre/question5":/project:ro \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash
```

Then inside the container do Steps 7 and 8 (copy, sed, catkin_make, source). After that, next time you can run:

```bash
docker run -it --rm --network host \
  -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  -v traveling_ethiopia_ws:/catkin_ws \
  traveling_ethiopia_robot:noetic \
  bash -c "source /catkin_ws/devel/setup.bash && roslaunch traveling_ethiopia_robot gazebo_world.launch"
```

No need to copy or build again.

---

## If Gazebo doesn’t open (DISPLAY / WSL)

If you see “cannot open display” or Gazebo doesn’t show a window:

1. In WSL, run:
   ```bash
   echo $DISPLAY
   ```
   If it’s empty, try:
   ```bash
   export DISPLAY=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}'):0
   ```
   Then run `xhost +local:docker` again and start the container.

2. On **Windows 11**, WSLg is usually enough. On **Windows 10**, you may need to install **VcXsrv** or **X410** and set DISPLAY to your Windows IP as above.

---

## Quick checklist

| Step | What to do |
|------|------------|
| 1 | Start Docker Desktop |
| 2 | Open WSL (Ubuntu) |
| 3 | `xhost +local:docker` |
| 4 | `cd "/mnt/c/Users/dawit/Desktop/ai pre/question5/docker"` |
| 5 | `docker build -t traveling_ethiopia_robot:noetic .` |
| 6 | `docker run -it --rm ...` (mount project, get bash) |
| 7 | Inside container: copy package, worlds, urdf, sed |
| 8 | Inside container: `cd /catkin_ws`, `source ...`, `catkin_make`, `source devel/setup.bash` |
| 9 | Inside container: `roslaunch traveling_ethiopia_robot gazebo_world.launch` |
| 10 | Second terminal: new container (or same with volume), then `rosrun traveling_ethiopia_robot path_planner.py` |

You’re done when Gazebo shows the world and robot, and the path planner prints the path in the second terminal.
