#/!bin/bash
#!/usr/bin/env python
#import sys
import rospy
from vision.msg import vision
#mport  vision.msg as vmsg

if __name__ == '__main__':

    pub  = rospy.Publisher( 'hello',vision ,queue_size=100)
    rospy.init_node('talker', anonymous = True)
    posx = 5
    posy = 6
    posz = 7
    vision.x = posx
    vision.y = posy
    vision.z = posz
    pub.publish(vision)