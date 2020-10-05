#! /usr/bin/env python 

import rospy
import roslib   
from sensor_msgs.msg import Range
from geometry_msgs.msg import Twist

class SonarSensorRange():

    def __init__(self):
        rospy.init_node("sonar_collision_test")
        nodename = rospy.get_name()
        rospy.loginfo("%s started" % nodename)

        self.vx = 0.8
        self.wz = 1.3
        self.sf = 0.0
        self.sl = 0.0
        self.sr = 0.0

        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
        rospy.Subscriber('pinna_bot/sonar/1',Range ,self.clbk_sonar1)
        rospy.Subscriber('pinna_bot/sonar/2',Range ,self.clbk_sonar2)
        rospy.Subscriber('pinna_bot/sonar/3',Range ,self.clbk_sonar3)


    def spin(self):
        r = rospy.Rate(30)
        then = rospy.Time.now()
        
        #### Main Loop ####
        while not rospy.is_shutdown():
            self.loop()
            r.sleep()
        
        rospy.spin()


    #### Take a decision ###
    def loop(self):
        msg = Twist()
        self.linear_x = 0.0
        self.angular_z = 0.0

        self.state_description = ''

        if self.sf < self.sl:
            if self.sf < self.sr:
                if self.sf < 0.5:
                    self.state_description = 'Turn Left SF'
                    self.linear_x = self.vx - 0.4
                    self.angular_z = self.wz
        elif self.sl < self.sr:
            if self.sl < 0.5:
                self.state_description = 'Turn Rigth SL'
                self.linear_x = self.vx - 0.4
                self.angular_z = -self.wz
        if self.sr < 0.5:
            self.state_description = 'Turn Left SF lallal'
            self.linear_x = self.vx - 0.4
            self.angular_z = self.wz
        else:
            self.state_description = 'Forward'
            self.linear_x = self.vx 
            self.angular_z = 0.0

        
        #rospy.loginfo(self.state_description)
        msg.linear.x = self.linear_x
        msg.angular.z = self.angular_z
        self.pub.publish(msg)


    #### Call sensors ####
    def clbk_sonar1(self,msg):
        self.sf = msg.range
        #rospy.loginfo("CallbackSonar1: %f" % self.sf)

    def clbk_sonar2(self,msg):
        self.sl = msg.range
        #rospy.loginfo("CallbackSonar2: %f" % self.sl)

    def clbk_sonar3(self,msg):        
        self.sr = msg.range
        #rospy.loginfo("CallbackSonar3: %f" % self.sr)

if __name__=='__main__':
    """ main """
    Sonars = SonarSensorRange()
    Sonars.spin()

        


