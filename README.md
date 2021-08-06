# InsperBot
ROS + Gazebo Simulator - Computational Robotics Insper.


 <img src="https://raw.githubusercontent.com/liciascl/liciascl/main/robotsim.gif" width="400">   <img src="/image/rodando.gif" width="290">  


### Requeriments

- Ubuntu 20.04 
- ROS Noetic 
- Opencv4

[How configure your sistem with this requeriments](https://github.com/Insper/404/blob/master/README.md)

### How to Run

``` bash

git clone https://github.com/Insper/insperbot.git
cd ~/catkin_ws
catkin_make

``` 

### Edit .bashrc

Add this lines in your .bashrc

``` bash
export TURTLEBOT3_MODEL=burger 
export LC_NUMERIC="en_US.UTF-8"
export GAZEBO_MODEL_PATH=$HOME/catkin_ws/src/insperbot/models:

``` 



### Choose one of this Scenarios

```bash
roslaunch insperbot burger_4_andar.launch
```

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/burger_4_andar.png" width="650" height="350">

```bash
roslaunch insperbot caixas.launch
```

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/caixas.png" width="650" height="350">

roslaunch insperbot circuito.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/circuito.png" width="650" height="350">

roslaunch insperbot corredor.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/corredor.png" width="650" height="350">


roslaunch insperbot corrida_de_obstaculos.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/corrida_de_obstaculos.png" width="650" height="350">


roslaunch insperbot cruzamento.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/cruzamento.png" width="650" height="350">


roslaunch insperbot encaixotado.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/encaixotado.png" width="650" height="350">


roslaunch insperbot forca.launch 

roslaunch insperbot forca_random.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/forca.png" width="650" height="350">


roslaunch insperbot formas.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/formas.png" width="650" height="350">


roslaunch insperbot labirinto.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/labirinto.png" width="650" height="350">


roslaunch insperbot mesa.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/mesa.png" width="650" height="350">


roslaunch insperbot pista_s2.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/pista_s2.png" width="650" height="350">

roslaunch insperbot pista_u.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/pista_u.png" width="650" height="350">

roslaunch insperbot retangulos.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/retangulos.png" width="650" height="350">

roslaunch insperbot salinha.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/salinha.png" width="650" height="350">

roslaunch insperbot zig-zag.launch

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/zig-zag.png" width="650" height="350">


### To Enable gripper control

``` bash

roslaunch insperbot arm_control.launch     

```

### How to control the robot's gripper

#### Arm (joint1):

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/arm.gif" width="400">


``` bash
Up: 1.5

Forward : 0

Down : -1.5

rostopic pub -1 /joint1_position_controller/command std_msgs/Float64 "data: 0"

```
#### Gripper (joint2 and joint3)

<img src="https://raw.githubusercontent.com/Insper/insperbot/main/image/gripper.gif" width="400">

``` bash
Closed: 0

Open: -1 

rostopic pub -1 /joint2_position_controller/command std_msgs/Float64 "data: 0"

```

### Past Projects Videos

Virtual robot:
https://www.youtube.com/playlist?list=PLVU3UhXa4-X9ZWrIV37l9ckvalaP5KiE9

Real and virtual robot:
https://www.youtube.com/playlist?list=PLVU3UhXa4-X-qIlNL6NVvIizOXXJkkkU1


### INSPER Robótica Computacional - 3.o semestre Engenharia de Computação 

![Github 2021.1](https://github.com/insper/robot21.1)

![Github 2020.2](https://github.com/insper/robot202)

![Github 2020.1](https://github.com/insper/robot20)

![Github 2019](https://github.com/insper/robot19)

![Github 2018.2](https://github.com/insper/robot18-2)

![Github 2018.1](https://github.com/insper/robot18)


### Authors

![Fabio R de Miranda](https://github.com/mirwox)
![Arnaldo Alves Viana Junior](https://github.com/arnaldojr/)
![Lícia Sales Costa Lima](https://github.com/liciascl)




