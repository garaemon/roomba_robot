#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy 
from nav_msgs.msg import Odometry
from roomba_500_series.msg import DigitLeds
from std_msgs.msg import Bool
import math
twist_pub = None

def joyCB(msg):
  global twist_pub, brush_pub
  # 6 -> l/r
  # 7 -> u/d
  factor = 1.0
  twist = Twist()
  if msg.axes[6] > 0:
    twist.angular.z = 0.1
  elif msg.axes[6] < 0:
    twist.angular.z = -0.1
  if msg.axes[7] > 0:
    twist.linear.x = 0.1
  elif msg.axes[7] < 0:
    twist.linear.x = -0.1
  if msg.buttons[2] == 1:
    brush_pub.publish(Bool(True))
  elif msg.buttons[1] == 1:
    brush_pub.publish(Bool(False))
  if msg.buttons[0] == 1:
    factor = 10.0
  twist.linear.x = twist.linear.x * factor
  twist.angular.z = twist.angular.z * factor
  twist_pub.publish(twist)

def odomCB(msg):
  global digits_pub
  distance = math.sqrt(msg.pose.pose.position.x * msg.pose.pose.position.x + msg.pose.pose.position.y * msg.pose.pose.position.y)
  # mm
  distance_mm = distance
  digits_nums = [int(math.floor(distance_mm / 1000.0)) % 10,
                 int(math.floor(distance_mm / 100.0))  % 10,
                 int(math.floor(distance_mm / 10.0))   % 10,
                 int(math.floor(distance_mm / 1.0))      % 10]
  digits_codes = [ord('0') + v for v in reversed(digits_nums)]   #digits[0] => 1 order
  digits = DigitLeds()
  digits.header.stamp = rospy.Time.now()
  digits.digits = digits_codes
  digits_pub.publish(digits)
  
  
def main():
  global twist_pub, digits_pub, brush_pub
  rospy.init_node("roomba_joy_sample") # declare my name
  twist_pub = rospy.Publisher("/cmd_vel", Twist)
  digits_pub = rospy.Publisher("/digit_leds", DigitLeds)
  brush_pub = rospy.Publisher("/brush", Bool)
  joy_sub = rospy.Subscriber("/joy", Joy, joyCB)
  
  odom_sub = rospy.Subscriber("/odom", Odometry, odomCB)
  rospy.spin()                        #

if __name__ == "__main__":
  main()
