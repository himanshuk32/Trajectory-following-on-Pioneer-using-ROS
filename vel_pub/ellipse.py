#!/usr/bin/env python

# imports
import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Vector3
from math import *

my_pi = 3.14159
# parameters
topic_cmd_vel = '/RosAria/cmd_vel'
update_interval = 0.1 # [s]

vel_max = input("Enter the max velocity (in m/s): ")	
a = input("Enter the semi-X axis length (in metre): ")
b = input("Enter the semi-Y axis length (in metre): ")

# launch node and create a publisher
rospy.init_node('ellipse')
pub = rospy.Publisher(topic_cmd_vel, Twist,queue_size=10)

count = 0 
omega = 0.2

# loop until shutdown
while not rospy.is_shutdown():
     
	vel_x = -a * sin(count*update_interval*omega)
	vel_y = b * cos(count*update_interval*omega) 
	vel_linear = sqrt( vel_x*vel_x + vel_y*vel_y)
	
	count  = count + 1

	if count > 2 * my_pi / (update_interval*omega):
	   count = 0 
	
	# publish the defined linear and angular velocity
	pub.publish(Twist(Vector3(vel_linear, 0, 0), Vector3(0, 0, omega)))
	
	# sleep the defined interval
	rospy.sleep(update_interval)
