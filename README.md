# PinnaBot Simulator 
Metapackage of a mobile robot model using ROS and Gazebo. The aim of this project is to provide a simulator to test algorithms and new routines in different customize environments. In the same way, to offer an educational platform of mobile robotic at the National University of San Luis

![SensorSonar_beer2](https://user-images.githubusercontent.com/63516549/159553102-1682f312-9d41-4701-b767-63ff9d34888c.png)

# Requirements
- Git: To download and manage the source code.
- Ubuntu 18.04: Operating System necessary to run.
- ROS: ROS Melodic Morenia. It's the framework of the project.
- Gazebo: The simulator with physics engine.

# Contents
The repository contents:

![structure2](https://user-images.githubusercontent.com/63516549/159554071-69bf4ae5-c806-4ba9-8914-847349613fa6.png)

- Description package: It contents the Robot Model(URDF), the Collada meshes and launch files to run the robot "Pinnabot".   
- Gazebo package: Folder with differents worlds or environments of Gazebo. 
- Control package: Package with a generic PID control of ROS-Control and an odometry service.  
- Example package: Folder with use's examples.

# Details
This package contain:
- 3 Worlds: 
  * LABME(National Univesity of San Luis) 
  * Gas Station(Gazebo community) 
  * Willow Garage(Gazebo community)
- 1 mobile robot with: 
  * Lidar laser scan
  * Camera
  * 3 sonar sensors
  * 1 castor wheel
  * 2 locomotion wheels

![Sensor_all_GasSt2](https://user-images.githubusercontent.com/63516549/159553575-d13333c0-55db-4c0b-847f-14f050b12900.png)

# Usage
First, install ROS. Instrucctions (http://wiki.ros.org/melodic/Installation/Ubuntu) [Desktop-Full install recommended]  

Then, create a work sapace:

``` 
    mkdir -p ~/simulation_ws/src
    cd ~/simulation/
    catkin_make
```

It's convenient if the ROS environment variables are automatically added to your bash session every time a new shell is launched:
```
   echo "source /simulation_ws/devel/setup.bash" >> ~/.bashrc
   source ~/.bashrc
 ```
 The project is ready to use.
 
 # Example
To run an example you must run the command:

`   roslaunch pinnabot_example sonar_test.launch`
 
 It's an example of an application of an algorithm to avoid obstacles with 3 sonar sensors.
 
 

                                   

