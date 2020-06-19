#!/usr/bin/env python3
import time 
import rospy
from std_msgs.msg import UInt16
import sys, select, termios, tty

rospy.init_node('motor', anonymous = True)

pub_motor_speed = rospy.Publisher('motor_speed',UInt16)
pub_motor_angle = rospy.Publisher('motor_angle',UInt16)

settings = termios.tcgetattr(sys.stdin)


def getKey():
    tty.setraw(sys.stdin.fileno())
    rlist, _, _ = select.select([sys.stdin], [], [], 0.1)
    if rlist:
        key = sys.stdin.read(1)
    else:
        key = ''
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, settings)
    return key

def motor():   #
      motor_speed = 0
      motor_angle = 65
      flag = False
      while not rospy.is_shutdown():
            key = getKey()
            if key == 'w':    
                  print("up!")
                  if motor_speed <130:
                        motor_speed=135
                        flag =True
                  elif motor_speed <230:
                        motor_speed+=25
                        flag =True
            elif key == 's':    
                  print("down!")
                  motor_speed =1
                  flag =True
            elif key == 'a':   
                  print("left!")
                  if motor_angle >=35:
                        motor_angle -= 10
                        flag =True
            elif key == 'd':
                  print("right!")
                  if motor_angle<115:
                        motor_angle += 10
                        flag =True
            elif key =='0':
                  print("stop!")
                  motor_speed = 0
                  motor_angle = 65
                  flag =True

            if flag ==False:
                  continue
            flag =False
            rospy.loginfo(motor_angle)
            rospy.loginfo(motor_speed)
            pub_motor_speed.publish(motor_speed)
            pub_motor_angle.publish(motor_angle)
            #rate.sleep()

if __name__=='__main__':
      try:
            motor()
      except rospy.ROSInterruptException:
            pass


