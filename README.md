# ros-nanodet
nanodet in ROS
Nanodet is one of my favorite object detection algorithm.  
This code deploys Nanodet in ROS environment for fast detection in embedded hardware.  
  
Nanodet是我很喜欢的一个轻量而高效的检测算法，我把它部署到了ROS环境中以在低性能嵌入式硬件上使用  

## Requirements
I've tested the code in the environment below:   
ROS Noetic  
opencv_python>=4.0   
  
opencv的版本有cv2.dnn就行  

## Usage
mkdir -p nanodet_ros/src  
cd nanodet_ros/src  
git clone https://github.com/stunback/ros-nanodet.git  
catkin_make  

In three terminals:  
source devel/setup.bash  

first:  
roscore  

second:  
rosrun usb_cam usb_cam_node  

third:  
rosrun nanodet_ros ros_nanodet.py   


## Others
A C++ Nanodet ros demo should be added soon  
  
我也在进行C++版本的Nanodet ros部署  

# Reference
https://github.com/hpc203/nanodet-opncv-dnn-cpp-python.git  
