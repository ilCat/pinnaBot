#! /usr/bin/env python
import rospy

from sensor_msgs.msg import Range

def clbk_Range(msg):
    rospy.loginfo(msg.range)

def main():
    rospy.init_node('reading_sonar')

    sub=rospy.Subscriber('Pinna_bot/sonar/1',Range ,clbk_Range)
   

    rospy.spin()

if __name__ =='__main__':
    main()

