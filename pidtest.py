#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import casadi as ca
from numpy import *
import time
import math 

pi = math.pi
t_start = time.time()

"""# variable parameters 
"""

n_states = 3
n_controls = 2
delta_T = 0.2

#timestamp bw two predictions
#if theta target is > pi, write as a negative angle
X_target = array([5,3,pi/2], dtype = 'f')                                                                            
error_allowed = 5e-2         

global x,y,theta,vx,vy,qx,qy,qz,qw,V,omega                                                                              # (x,y,theta) will store the current position and orientation 
                                                                                                                        # qx,qy,qz,qw will store the quaternions of the bot position
                                                                                                                        # V and omega will store the inputs to the bot(Speed and Angular Velocity) 
     
    
    
def odomfunc(odom):

    global x,y,qx,qy,qz,qw,vx,vy,theta
    x = odom.pose.pose.position.x 
    y = odom.pose.pose.position.y 
    qx = odom.pose.pose.orientation.x                                                                                   # quaternions of location
    qy = odom.pose.pose.orientation.y
    qz = odom.pose.pose.orientation.z 
    qw = odom.pose.pose.orientation.w

    theta = math.atan2(2*(qx*qy+qw*qz),1-2*(qy*qy+qz*qz))                                                               # finding yaw from quaternions
 
 def my_mainfunc():
    
    rospy.init_node('pidtest', anonymous=True)

    rospy.Subscriber('/odom', Odometry , odomfunc)    
    instance = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

# Initialisation des variables pour le contrôleur PID
    Kp = 1.0 # Coefficient proportionnel
    Ki = 0.1 # Coefficient intégral
    Kd = 0.01 # Coefficient dérivé
    last_error = 0.0
    total_error = 0.0
    target_pose = None
    
    
    #code qui permet de calculer la commande pid a envoyer 
    
    msg = Twist()
    msg.linear.x = V                                                                                             # linear.y always zero, linear.x is the speed of a diff. bot
    msg.linear.y = 0                            
    msg.linear.z = 0
    msg.angular.x = 0
    msg.angular.y = 0
    msg.angular.z = omega
        
    instance.publish(msg)

    
    rate = rospy.Rate(10) # 10hz    
    rate.sleep()                                                                                                       # rate.sleep() to run odomfunc once
    
    msg = Twist()

 


t_end = time.time()