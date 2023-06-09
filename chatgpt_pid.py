#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist, PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion

pi = math.pi
t_start = time.time()



# variable parameters 

n_states = 3
n_controls = 2
delta_T = 0.2                                                                   #timestamp bw two predictions
                      
# if theta target is > pi, write as a negative angle
X_target = array([2,1,pi], dtype = 'f')                                          
error_allowed = 5e-2


error_allowed_in_g = 1e-100

def odometry_callback(self, odom_msg):
    # Mise à jour de la pose actuelle du robot
    self.current_pose = odom_msg.pose.pose
        
def target_pose_callback(self, pose_msg):
    # Mise à jour de la cible de pose
    self.target_pose = pose_msg.pose
        
def calculate_error(self):
    # Calcul de l'erreur de position actuelle par rapport à la cible de position
    current_x = self.current_pose.position.x
    current_y = self.current_pose.position.y
    target_x = self.target_pose.position.x
    target_y = self.target_pose.position.y
    error = ((target_x - current_x)**2 + (target_y - current_y)**2)**0.5
    return error
        
def calculate_twist(self, error):
    # Calcul de la commande de mouvement en utilisant le contrôleur PID
    p_term = self.Kp * error
    self.total_error += error
    i_term = self.Ki * self.total_error
    d_term = self.Kd * (error - self.last_error)
    self.last_error = error
    twist = Twist()
    twist.linear.x = p_term + i_term + d_term
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    return twist           
def pidcontroller():
    # Initialisation du noeud ROS
    rospy.init_node('pidcontroller', anonymous=True)
        
    # Initialisation des variables pour le contrôleur PID
    Kp = 1.0 # Coefficient proportionnel
    Ki = 0.1 # Coefficient intégral
    Kd = 0.01 # Coefficient dérivé
    last_error = 0.0
    total_error = 0.0
    target_pose = None
        
    # Abonnement aux topics de pose et de la commande de mouvement
    rospy.Subscriber('/odom', Odometry, odometry_callback)
    self.velocity_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        
    # Abonnement au topic de la cible de pose
    rospy.Subscriber('/move_base_simple/goal', PoseStamped, target_pose_callback)
        
    # Boucle principale du contrôleur
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        if self.target_pose is not None:
            # Calcul de la commande de mouvement en utilisant le contrôleur PID
            error = calculate_error()
            twist = calculate_twist(error)
            velocity_publisher.publish(twist)
    rate.sleep()


    t_end = time.time()
    
    print ("Total Time taken = " , t_end - t_start)        
if __name__ == '__main__':
    try:
        pidcontroller()
    except rospy.ROSInterruptException:
        pass
