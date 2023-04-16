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
