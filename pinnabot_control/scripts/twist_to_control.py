#! /usr/bin/env python

import rospy
import roslib
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist

def clbk_twist(msg):
    dX = msg.linear.x
    dR = msg.angular.z
    Transform(dX,dR)

def Transform(dx,dr):
    right = 0.0
    left = 0.0
    wheel_separation = 0.24  #Dist betwen wheels [m] 
    wheel_radius=0.0438 #Wheel radius [m]

    # dx = (l + r) / 2
    # dr = (r - l) / w
            
    vel_wheel_right = 1.0 * dx + dr * wheel_separation * wheel_separation_multiplier / 2 
    vel_wheel_left = 1.0 * dx - dr * wheel_separation * wheel_separation_multiplier / 2

    #frec_Wheel = vel_Wheel/ Radius_Wheel

    left = vel_wheel_left / (wheel_radius * wheel_radius_multiplier)
    right = vel_wheel_right / (wheel_radius * wheel_radius_multiplier)

    #rospy.loginfo("publishing: (%d, %d)", left, right) 
    #rospy.loginfo("param wheel_radius_multiplier wheel_separation_multiplier: (%d, %d)", wheel_radius_multiplier, wheel_separation_multiplier)
                
    pub_lmotor.publish(left)
    pub_rmotor.publish(right)


def main():
    global pub_lmotor
    global pub_rmotor
    global wheel_separation_multiplier #Dist betwen wheel MULTIPLIER
    global wheel_radius_multiplier #Wheel radius MULTIPLIER

    rospy.init_node("twist_to_control")
    nodename = rospy.get_name() 
    rospy.loginfo("%s started" % nodename)

    
    wheel_radius_multiplier = None
    wheel_separation_multiplier = None
    wheel_separation_multiplier = rospy.get_param("/pinna_bot/twist_to_control_parameter/wheel_separation_multiplier", 1.0)
    wheel_radius_multiplier = rospy.get_param("/pinna_bot/twist_to_control_parameter/wheel_radius_multiplier", 1.0)
    
    pub_lmotor = rospy.Publisher('/pinna_bot/wheelLeft_velocity_controller/command', Float64,queue_size=1)
    pub_rmotor = rospy.Publisher('/pinna_bot/wheelRight_velocity_controller/command', Float64,queue_size=1)
    sub = rospy.Subscriber('/cmd_vel',Twist ,clbk_twist)

    rospy.spin()
    

if __name__ == '__main__':
    main()
