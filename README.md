# nao_move_head

Simple Aldebaran NAO and Pepper robots head controller integrated into ROS. It works with Aldebaran NAO and Pepper robots, as well as with virtual version in rviz environments (http://wiki.ros.org/nao/Tutorials/Getting-Started).

# Table of contents
+ [Disclaimer](#disclaimer)
+ [Repository information](#repository-information)
+ [Repository requirements and dependencies](#repository-requirements-and-dependencies)
	- [System Requirements and Compatibility](#system-requirements-and-compatibility)
	- [Dependencies](#dependencies)
+ [Installation Instructions](#installation-instructions)
	- [Pre-requirements](#pre-requirements)
	- [Installation steps](#installation-steps)
+ [ROS Launcher](#ROS-Launcher)
+ [License](#license)
+ [Citation](#citation)
+ [Contributors](#contributors)


# Disclaimer
You are using this software at your own risk. The authors decline any responsibility for personal injuries and/or property damage.

# Repository information

This repository is formed by a ROS package: 
 
 + nao_move_head: Simple NAO head controller integrated into ROS.

# Repository requirements and dependencies

## System Requirements and Compatibility

This package is running under:

+ Ubuntu: 16.04 and above
+ ROS: Kinetic and built with catkin tools

This package has been tested under:

+ Ubuntu: 16.04
+ ROS: Kinetic

## Dependencies

+ nao_qi

# Installation Instructions

## Pre-requirements
Install all the system and ROS dependencies (for example, using rosdep install, or apt-get, or directly from source).

## Installation steps

1. Create your ROS catkin workspace as usual.
3. Inside your workspace, download the nao_move_head repository:
    git clone https://github.com/dcazzato/nao_move_head ./
4. Compile your ROS catkin workspace as usual (catkin build recommended!)
	
	
# ROS Launcher
The package includes a launcher called nao_move_head.launch.

Configurable ROS launch parameters:

+ subscriber_hpe: name of the subscriber that published head pose angles
+ fractionMaxSpeedYaw: The fraction of maximum speed to use for the yaw angle (see  http://doc.aldebaran.com/2-1/naoqi/motion/control-joint-api.html)
+ fractionMaxSpeedPitch: The fraction of maximum speed to use for the pitch angle (see  http://doc.aldebaran.com/2-1/naoqi/motion/control-joint-api.html)
+ robotIP: the IP address to communicate the command to the robot.

# License
All distributed software are subject to the 3-clause BSD license. See the LICENSE file. 


# Citation

Please cite this paper in your publications if it helps your research:

```
@inproceedings{cazzato2019real,
  title={Real-Time Human Head Imitation for Humanoid Robots},
  author={Cazzato, Dario and Cimarelli, Claudio and Sanchez-Lopez, Jose Luis and Olivares-Mendez, Miguel A and Voos, Holger},
  booktitle={Proceedings of the 2019 3rd International Conference on Artificial Intelligence and Virtual Reality},
  pages={65--69},
  year={2019}
}
```

# Contributors

List of people that have contributed:

+ Dario Cazzato (dcazzato85@gmail.com): Main Author, Maintainaince, Debugging, Testing and Documentation.

Feel free to fork the project and send your contributions.
	


