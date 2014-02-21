#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

twist_pub = None

def joyCB(msg):
  global twist_pub
  # 6 -> l/r
  # 7 -> u/d
  twist = Twist()
  if msg.axes[6] > 0:
    twist.angular.z = 0.3
  elif msg.axes[6] < 0:
    twist.angular.z = -0.3
  if msg.axes[7] > 0:
    twist.linear.x = 0.1
  elif msg.axes[7] < 0:
    twist.linear.x = -0.1
  twist_pub.publish(twist)

def main():
  global twist_pub
  rospy.init_node("roomba_joy_sample") # declare my name
  twist_pub = rospy.Publisher("/cmd_vel", Twist)
  joy_sub = rospy.Subscriber("/joy", Joy, joyCB)
  rospy.spin()                        #

if __name__ == "__main__":
  main()
