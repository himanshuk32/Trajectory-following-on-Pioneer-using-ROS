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
vel_max = input("Enter the maximum velocity (in m/s): ")	
a = input("Enter length of square in metre:" )

# launch node and create a publisher
rospy.init_node('square')
pub = rospy.Publisher(topic_cmd_vel, Twist,queue_size=10)

count = 0
count1= 0
omega = 0 
# loop until shutdown
while not rospy.is_shutdown():
        
	if ( vel_max * count * update_interval < a):
	   vel_linear = vel_max
	   omega = 0 
	   count = count+1
	else :
	   count1 = count1+1 
	   vel_linear = 0
	   omega = my_pi/2
	   if count1 == 10:
	      omega = 0
	      count1 = 0
	      count = 0
	      
	# publish the defined linear and angular velocity
	pub.publish(Twist(Vector3(vel_linear, 0, 0), Vector3(0, 0, omega)))
	
	# sleep the defined interval
	rospy.sleep(update_interval)
