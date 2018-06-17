# Trajectory following on P3-DX

System requirement:                                           
  a) Ubuntu with 12.04 or higher version                                      
  b) ROS with Hydro or higher version                                 
  c) rosaria                                         

Step 1) Open a terminal and type the following:                                        
           git clone https://github.com/himanshuk32/Trajectory-following-using-ROS                        
           cd catkin_ws/src                                                
           catkin_create_pkg trajectories rosaria rospy roscpp                                                       
           cd ..                                              
           catkin_make                                                                                        
   
Step 2) Now, copy the python files of the repository to the "trajectories" folder(located in catkin_ws/src)                           
        Now, in a terminal type:                             
           cd catkin_ws                                
           catkin_make                                                                                       
           
Step 3) Now, refer to http://wiki.ros.org/ROSARIA/Tutorials/How%20to%20use%20ROSARIA for some basics of rosaria                           
        Get connected to robot and then type (in a new terminal shell):                                       
           rosrun trajectories <file_name>.py                              
           
