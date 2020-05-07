#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64


def Sit():
        
    pub1 = rospy.Publisher('spotmicroai/front_right_foot_position_controller/command', Float64, queue_size=10)
    pub2 = rospy.Publisher('spotmicroai/front_left_foot_position_controller/command', Float64, queue_size=10)
    pub3 = rospy.Publisher('spotmicroai/rear_right_foot_position_controller/command', Float64, queue_size=10)
    pub4 = rospy.Publisher('spotmicroai/rear_left_foot_position_controller/command', Float64, queue_size=10)
    rospy.init_node('Sit', anonymous=True)

    while not rospy.is_shutdown():
        rate = rospy.Rate(10) # 10hz
        pub1.publish(1)
        pub2.publish(1)
        pub3.publish(1.75)
        pub4.publish(1.75)
        rate.sleep()

if __name__ == '__main__':
    try:
        Sit()
    except rospy.ROSInterruptException:
        pass
