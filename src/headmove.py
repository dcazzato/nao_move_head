#!/usr/bin/env python

import rospy
import sys
import time
from geometry_msgs.msg import Point
from naoqi_driver.naoqi_node import NaoqiNode
from naoqi import (ALBroker, ALProxy, ALModule)



class HEADMOVE:

    def __init__(self, motionProxy):

        # read parameters
        self.motionProxy = motionProxy
        self.subscriber_hpe = rospy.get_param('~subscriber_hpe', 'obstacle_hpe/headposeRad')
        self.fractionMaxSpeedYaw = rospy.get_param('~fractionMaxSpeedYaw')
        self.fractionMaxSpeedPitch = rospy.get_param('~fractionMaxSpeedPitch')



        self.subscriber = rospy.Subscriber(self.subscriber_hpe, Point, self.hpe_callback, queue_size=1)

        print('[NAO_MOVE_HEAD-ROS] Subscribed. Waiting for head pose stream (Point messages).')

    def hpe_callback(self, msg):
        self.motionProxy.stopMove()
        self.motionProxy.moveInit()
        self.motionProxy.setAngles("HeadYaw", msg.x, self.fractionMaxSpeedYaw)
        self.motionProxy.setAngles("HeadPitch", msg.y, self.fractionMaxSpeedPitch)
        #self.motionProxy.stopMove()
        print('[NAO_MOVE_HEAD-ROS] Subscribed. Moving head with angles {},{}'.format(msg.x, msg.y))
        return


def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main():
    rospy.init_node('nao_move_head')
    robotIP = rospy.get_param('~robotIP', '127.0.0.1')

    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except:
        print("[NAO_MOVE_HEAD-ROS] Could not create proxy to ALMotion: %s" % sys.exc_info()[0])
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except:
        print("[NAO_MOVE_HEAD-ROS] Could not create proxy to ALRobotPosture: %s" % sys.exc_info()[0])

    StiffnessOn(motionProxy)
    postureProxy.goToPosture("StandInit", 1.0)

    HEADMOVE(motionProxy)
    while not rospy.is_shutdown():
        rospy.spin()

if __name__ == "__main__":
    main()