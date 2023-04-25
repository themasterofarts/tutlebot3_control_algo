#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

from numpy import *
import time
import math 

pi = math.pi
t_start = time.time()



"""# variable parameters 
"""

n_states = 3
n_controls = 2
N = 100                                                                         #Prediction horizon(same as control horizon)
delta_T = 0.2                                                                   #timestamp bw two predictions
                      
# if theta target is > pi, write as a negative angle
X_target = array([2,1,pi], dtype = 'f')                                          
error_allowed = 5e-2


Q_x = 100                                                                       # gains to control error in x,y,theta during motion
Q_y = 100
Q_theta = 6
R1 = 300                                                                        # gains to control magnitude of V and omega                                                                                                           
R2 = 75

error_allowed_in_g = 1e-100                                                     # error in contraints (should be ~ 0)

"""# parameters that depend on simulator 
"""
n_bound_var = n_states                                                          #although theta will never have any bound but, we need to specify it because X is part of OPT_variables           
x_bound_max = inf                      
x_bound_min = -inf                     
y_bound_max = inf                     
y_bound_min = -inf                                                                                
theta_bound_max = inf                     
theta_bound_min = -inf                     


v_max = 0.22
v_min = -v_max
omega_max = 2.84                                                
omega_min = -omega_max

global x,y,theta,qx,qy,qz,qw,V,omega                                        # (x,y,theta) will store the current position and orientation 
                                                                            # qx,qy,qz,qw will store the quaternions of the bot position
                                                                            # V and omega will store the inputs to the bot(Speed and Angular Velocity)                                                                                                                                                                                        
  

global total_path_points                                                                                                                                        
total_path_points = 0                                                                                                                                                                            
global path                                                                                                                                         

def odomfunc(odom):

    global x,y,qx,qy,qz,qw,theta
    x = odom.pose.pose.position.x 
    y = odom.pose.pose.position.y 
    qx = odom.pose.pose.orientation.x                                       # quaternions of location
    qy = odom.pose.pose.orientation.y
    qz = odom.pose.pose.orientation.z 
    qw = odom.pose.pose.orientation.w

    theta = math.atan2(2*(qx*qy+qw*qz),1-2*(qy*qy+qz*qz))                   # finding yaw from quaternions



def pathfunc(Path):                                                                                                                                       

    global total_path_points,path
    if total_path_points == 0:        
        total_path_points = len(Path.poses)
        path = np.zeros((total_path_points,2))													
        
    for i in range(0,total_path_points):                                                                                                                
        path[i][0] = Path.poses[i].pose.position.x
        path[i][1] = Path.poses[i].pose.position.y   

    