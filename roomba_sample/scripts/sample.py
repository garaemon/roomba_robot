#!/usr/bin/env python

import roslib
import rospy

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry


# global object
twist_pub = None
initial_odom = None

def odomCB(msg):                          #callback functoin for /odom, msg = nav_msgs/Odom
  global twist_pub, initial_odom
  # msg.pose.pose.position.{x,y,z}, msg.pose.pose.orientation.{x,y,z,w}
  if not initial_odom:
      initial_odom = msg                  #at the first time, just remember the first value
  else:
      if msg.pose.pose.position.x - initial_odom.pose.pose.position.x > 0.1:
          twist = Twist()                 #make a message to be published to /cmd_vel
          twist.linear.x = 0.0
          twist.linear.y = 0.0
          twist.linear.z = 0.0
          twist.angular.x = 0.0
          twist.angular.y = 0.0
          twist.angular.z = 0.0
          twist_pub.publish(twist)
          rospy.loginfo("over 10cm!")
  

def main():
  global twist_pub
  rospy.init_node("roomba_sample") # declare my name
  twist_pub = rospy.Publisher("/cmd_vel", Twist)
  odom_sub = rospy.Subscriber("/odom", Odometry, odomCB)

  twist = Twist()
  twist.linear.x = 0.1
  rospy.sleep(1)
  twist_pub.publish(twist)
  rospy.spin()
  # while not rospy.is_shutdown():
  #   rospy.sleep(1)

if __name__ == "__main__":
  main()
