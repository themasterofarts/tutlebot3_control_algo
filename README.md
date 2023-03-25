# tutlebot3_control_algo
my control algorithms on the turtlebot3

A Good way to follow this repository is to install ROS on your computer through
http://wiki.ros.org/ROS/Installation

Then you can configure your catkin workspace 
http://wiki.ros.org/ROS/Installation

After following closely the twelve first tutorials , you will
need to install different packages associated to the turtlebot3
closely follow all the steps included in chapter 6 of 

https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/

Once you are done with that you will need some configurations done 
to execute this code:


1- create a new folder in your catkin_ws/src/turtlebot3_navigation 
2- set up your environment variables with cmd line 
   
     cat  ~/.bashrc 
    
    open the file with cmd line
   
     gedit ~/.bashrc 
add this new line to your .bashrc file 
     
     export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-package
     
 3- Now you can download the content of this repo in your created folder
 and run any script using the following command lines:
 
     export TURTLEBOT3_MODEL=burger

     roslaunch turtlebot3_gazebo turtlebot3_world.launch
 
     rosrun turtlebot3_navigation script
   
