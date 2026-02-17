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
echo Then run:
echo   bash /project/docker/build_and_launch.sh
echo   roslaunch traveling_ethiopia_robot gazebo_world.launch
echo.
echo For best experience (persisted build), use WSL and run: bash run_here.sh
echo.
pause

docker run -it --rm --network host -e DISPLAY=host.docker.internal:0 -e QT_X11_NO_MITSHM=1 -v "%CD%\..":/project:ro -v traveling_ethiopia_ws:/catkin_ws traveling_ethiopia_robot:noetic bash
