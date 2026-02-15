@echo off
REM Run Gazebo + ROS Noetic via Docker. Start Docker Desktop first.
cd /d "%~dp0"

echo Checking Docker...
docker info >nul 2>&1
if errorlevel 1 (
    echo Docker is not running. Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo Building image (first time may take a few minutes)...
docker build -t traveling_ethiopia_robot:noetic .
if errorlevel 1 (
    echo Build failed.
    pause
    exit /b 1
)

echo.
echo Starting container. You will get a bash shell inside.
echo Then run these commands one by one:
echo.
echo   cp -r /project/ros_package /catkin_ws/src/traveling_ethiopia_robot
echo   mkdir -p /catkin_ws/src/traveling_ethiopia_robot/worlds /catkin_ws/src/traveling_ethiopia_robot/urdf
echo   cp /project/world/traveling_ethiopia.world /catkin_ws/src/traveling_ethiopia_robot/worlds/
echo   cp /project/robot_description/three_wheel_robot.urdf /catkin_ws/src/traveling_ethiopia_robot/urdf/
echo   sed -i "s|\${CMAKE_CURRENT_SOURCE_DIR}/../world/traveling_ethiopia.world|\${CMAKE_CURRENT_SOURCE_DIR}/worlds/traveling_ethiopia.world|g" /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
echo   sed -i "s|\${CMAKE_CURRENT_SOURCE_DIR}/../robot_description/three_wheel_robot.urdf|\${CMAKE_CURRENT_SOURCE_DIR}/urdf/three_wheel_robot.urdf|g" /catkin_ws/src/traveling_ethiopia_robot/CMakeLists.txt
echo   cd /catkin_ws ^&^& source /opt/ros/noetic/setup.bash ^&^& catkin_make ^&^& source devel/setup.bash
echo   roslaunch traveling_ethiopia_robot gazebo_world.launch
echo.
pause

docker run -it --rm --network host -e DISPLAY=host.docker.internal:0 -e QT_X11_NO_MITSHM=1 -v "%CD%\..":/project:ro traveling_ethiopia_robot:noetic bash
