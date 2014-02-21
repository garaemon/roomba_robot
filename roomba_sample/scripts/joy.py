#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy 
from nav_msgs.msg import Odometry
from roomba_500_series.msg import DigitLeds
import math
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
    twist.linear.x = 0.3
  elif msg.axes[7] < 0:
    twist.linear.x = -0.3
  twist_pub.publish(twist)

def odomCB(msg):
  global digits_pub
  distance = math.sqrt(msg.pose.pose.position.x * msg.pose.pose.position.x + msg.pose.pose.position.y * msg.pose.pose.position.y)
  # mm
  print distance
  distance_mm = distance
  digits_nums = [int(math.floor(distance_mm / 1000.0)) % 10,
                 int(math.floor(distance_mm / 100.0))  % 10,
                 int(math.floor(distance_mm / 10.0))   % 10,
                 int(math.floor(distance_mm / 1.0))      % 10]
  print digits_nums
  digits_codes = [ord('0') + v for v in reversed(digits_nums)]   #digits[0] => 1 order
  digits = DigitLeds()
  digits.header.stamp = rospy.Time.now()
  digits.digits = digits_codes
  digits_pub.publish(digits)
  
  
def main():
  global twist_pub, digits_pub
  rospy.init_node("roomba_joy_sample") # declare my name
  twist_pub = rospy.Publisher("/cmd_vel", Twist)
  digits_pub = rospy.Publisher("/digit_leds", DigitLeds)
  joy_sub = rospy.Subscriber("/joy", Joy, joyCB)
  
  odom_sub = rospy.Subscriber("/odom", Odometry, odomCB)
  rospy.spin()                        #

if __name__ == "__main__":
  main()
