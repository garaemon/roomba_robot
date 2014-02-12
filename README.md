# roomba_robot [![Build Status](https://travis-ci.org/garaemon/roomba_robot.png?branch=master)](https://travis-ci.org/garaemon/roomba_robot)
hydro fork of roomba_robot, originally from http://isr-uc-ros-pkg.googlecode.com/svn/stacks/roomba_robot/trunk/

## how to install
```sh
# prepare ros
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'
wget http://packages.ros.org/ros.key -O - | sudo apt-key add -
sudo apt-get update
sudo apt-get install python-catkin-pkg python-rosdep python-wstool ros-hydro-catkin ros-hydro-ros ros-hydro-tf ros-hydro-nav-msgs
# prepare catkin ws
mkdir -p ros_catkin_ws/hydro/src
cd ros_catkin_ws/hydro/src
catkin_init_workspace
wstool init
wstool set --git roomba_robot https://github.com/garaemon/roomba_robot.git
wstool update
# compile
cd ..
catkin_make
catkin_make install
# source environments
source install/setup.bash
# ENJOY!!
```
