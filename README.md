# uia_husky_0776
<img src="https://github.com/orjano-max/uia_husky_0776/blob/main/thumbnail_IMG_3990.jpg" width="500" height="500">
This is the git repository for the Husky A200 with serial number 0776. The repository works for other husky UGVs too, but it adds attatchments to the UGV that are specific for this Husky
Launching the husky with these packages will bring up the husky, with the frame addon and lidar running. The lidar will publish point cloud and the pointcloud to laserscan will take care of the conversion from pointcloud to laserscan. The packages UM7 and serial is needed for the IMU, the rest is husky.

## Documentation
Some documentation has been made as a part of a project on the setup of this particulat Husky. The information might be somewhat outdated in certain aspects, but it could useful information regarding how to do setup and how to launch slam, NAV 2 etc.
It can be found here: https://mas514-husky_group.gitlab.io/mas-514-husky/index.html

## Installation
Open terminal

Clone this repo:

~~~bash
git clone https://github.com/orjano-max/uia_husky_0776
~~~

Update submodules in order to download UM7 and serial
~~~bash
cd uia_husky_0776
git submodule update --init --recursive
~~~

Source ros
~~~ bash
source /opt/ros/foxy/setup.bash
~~~

Run rosdep
~~~bash
cd uia_husky_0776
rosdep install --ignore-src --rosdistro foxy -y
~~~

Build the pacakges from the workspace directory
~~~bash
colcon build
~~~


## Run
Install the packages first, then open new terminal.

Source ros and the pacakges
~~~bash
source /opt/ros/foxy/setup.bash
source uia_husky_0776/install/local_setup.bash
~~~

Launch the husky:
~~~bash
ros2 launch husky_group husky.launch.py
~~~
