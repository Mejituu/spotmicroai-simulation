#!/usr/bin/env python
import rospy
import sys
from enum import Enum
from std_msgs.msg import Float64
from spotmicroai.msg import LegCommand


def MoveLeg(data, number):
    if data.Legs[number]==1:
        #Create the motor publishers
        pub1 = rospy.Publisher('spotmicroai/'+name+'_shoulder_position_controller/command', Float64,queue_size=10)
        pub2 = rospy.Publisher('spotmicroai/'+name+'_leg_position_controller/command', Float64,queue_size=10)
        pub3 = rospy.Publisher('spotmicroai/'+name+'_foot_position_controller/command', Float64,queue_size=10)


        rate = rospy.Rate(100) # 100 Hz
        print("[ INFO] Moving "+ name)

        for i in range (0,200):
            pub1.publish(data.Theta1)
            pub2.publish(data.Theta2)
            pub3.publish(data.Theta3)
            rate.sleep()

def Leg(name, number):

    #Create the subscriber for the comands
    rospy.Subscriber('spotmicroai/MoveLegs', LegCommand, MoveLeg, number)

    rospy.spin()
    
            
if __name__ == '__main__':

    #Initialize the node
    rospy.init_node("~name", anonymous=True)

    #Get node name
    name = rospy.get_param('~name', 'Leg')
    number = rospy.get_param('~number', 0)
    print("[ INFO] "+name +" node initialized")
    Leg(name, number)