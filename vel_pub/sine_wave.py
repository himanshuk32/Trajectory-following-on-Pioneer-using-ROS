#!/usr/bin/env python

# imports
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from math import *

# parameters
topic_cmd_vel = '/RosAria/cmd_vel'
update_interval = 0.1 # [s]
my_pi = 3.14159
vel_max = input("Enter the max velocity (in m/s): ")	
A = input("Enter the amplitude of your sine wave (in metre): ")

# launch node and create a publisher
rospy.init_node('sine_wave')
pub = rospy.Publisher(topic_cmd_vel, Twist,queue_size=10)

count = 0 
omega = 0.2
flag = 1
# loop until shutdown
while not rospy.is_shutdown():
        
	vel_x = A*count * update_interval*omega
	vel_y = A * cos(count * update_interval*omega)
	vel_linear = flag * sqrt( vel_x*vel_x + vel_y*vel_y)
	
	count  = count + 1
	if count > my_pi/ (update_interval*omega):
	   omega = (-1)*omega
	if count > 2 * my_pi / (update_interval*omega):
	  # flag = flag*(-1)
	   count = 0 
	
	# publish the defined linear and angular velocity
	pub.publish(Twist(Vector3(vel_linear, 0, 0), Vector3(0, 0, omega)))
	
	# sleep the defined interval
	rospy.sleep(update_interval)
