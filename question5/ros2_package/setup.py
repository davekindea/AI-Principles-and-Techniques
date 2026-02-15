from setuptools import setup, find_packages
import os
from glob import glob

package_name = 'traveling_ethiopia_robot'

setup(
    name=package_name,
    version='0.1.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.world')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='User',
    maintainer_email='user@example.com',
    description='Traveling Ethiopia Figure 5 - path planner and Gazebo world (ROS 2)',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'path_planner = traveling_ethiopia_robot.path_planner_node:main',
        ],
    },
)
