#!/usr/bin/env python
#import sys
import rospy
from vision.msg import vision
#mport  vision.msg as vmsg

def callback(vision):
    px = vision.x
    py = vision.y
    pz = vision.z
    print('x = ',px)
    print('y = ',py)
    print('z = ',pz)

if __name__ == '__main__':
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("africa", vision, callback)
    rospy.spin()
    