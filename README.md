# How to Run InsperBot on Gazebo

**NOTE:** This instruction was tested on Linux with Ubuntu 20.04 and ROS1 Noetic.

This is the virtual version of InsperBot, He was built by the technical team of Insper's Computer Engineering laboratory, using as base the Turtlebot3 Burger, the InsperBot is a low cost ROS standard platform robot simulated on Gazebo. 

![https://raw.githubusercontent.com/liciascl/liciascl/main/robotsim.gif](https://raw.githubusercontent.com/liciascl/liciascl/main/robotsim.gif)

### Requeriments

- Ubuntu 20.04
- ROS Noetic
- Opencv4

**NOTE:** We have a guide for setup your system with this Requirements **[here](https://github.com/Insper/insperbot/wiki/How-Setup-your-Ubuntu-20.04)** 

### How to Run

clone the repository:

```bash
git clone https://github.com/Insper/insperbot.git
cd ~/catkin_ws
catkin_make
```

### Edit .bashrc

Add this lines in your .bashrc

```bash
export TURTLEBOT3_MODEL=burger
export LC_NUMERIC="en_US.UTF-8"
export GAZEBO_MODEL_PATH=$HOME/catkin_ws/src/insperbot/models:
```

Choose one of the scenarios available **[here](https://github.com/Insper/insperbot/wiki/Useful-Commands)** or create your own by following **[this guide](http://gazebosim.org/tutorials?tut=build_world&cat=build_world)**

### To Enable gripper control

```
roslaunch insperbot arm_control.launch
```

### How to control the robot’s gripper

### Arm (joint1):

![https://raw.githubusercontent.com/Insper/insperbot/main/image/arm.gif](https://raw.githubusercontent.com/Insper/insperbot/main/image/arm.gif)

```bash
Up: 1.5
Forward : 0
Down : -1.5

rostopic pub -1 /joint1_position_controller/command std_msgs/Float64 "data: 0"
```

### Gripper (joint2 and joint3)

![https://raw.githubusercontent.com/Insper/insperbot/main/image/gripper.gif](https://raw.githubusercontent.com/Insper/insperbot/main/image/gripper.gif)

```bash
Closed: 0
Open: -1
rostopic pub -1 /joint2_position_controller/command std_msgs/Float64 "data: 0"
```

### Past Projects Videos

Virtual robot: 

[https://www.youtube.com/playlist?list=PLVU3UhXa4-X9ZWrIV37l9ckvalaP5KiE9](https://www.youtube.com/playlist?list=PLVU3UhXa4-X9ZWrIV37l9ckvalaP5KiE9)

Real and virtual robot:

[https://www.youtube.com/playlist?list=PLVU3UhXa4-X-qIlNL6NVvIizOXXJkkkU1](https://www.youtube.com/playlist?list=PLVU3UhXa4-X-qIlNL6NVvIizOXXJkkkU1)



### INSPER Repositories


[Github 2021.1](https://github.com/insper/robot21.1)

[Github 2020.2](https://github.com/insper/robot202)

[Github 2020.1](https://github.com/insper/robot20)

[Github 2019](https://github.com/insper/robot19)

[Github 2018.2](https://github.com/insper/robot18-2)

[Github 2018.1](https://github.com/insper/robot18)


----

### Authors

[Fabio R de Miranda](https://github.com/mirwox)

[Arnaldo Alves Viana Junior](https://github.com/arnaldojr/)

[Lícia Sales Costa Lima](https://github.com/liciascl)

