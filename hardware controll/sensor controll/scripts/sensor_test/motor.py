#!/usr/bin/env python3
import time 
import rospy
from std_msgs.msg import UInt16
import pygame


rospy.init_node('motor', anonymous = True)

pub_motor_speed = rospy.Publisher('motor_speed',UInt16)
pub_motor_angle = rospy.Publisher('motor_angle',UInt16)

def motor():   #
      pygame.init()
      motor_speed = 0
      motor_angle = 65
      gameDisplay = pygame.display.set_mode((128, 128))
      flag = False
      while not rospy.is_shutdown():
            for event in pygame.event.get():
                  if event.type == pygame.KEYDOWN:    
                        key= pygame.key.get_pressed()
                        if key[pygame.K_w]:
                              print("up!")
                              if motor_speed <130:
                                    motor_speed=135
                                    flag =True
                              elif motor_speed <230:
                                    motor_speed+=25
                                    flag =True
                        elif key[pygame.K_s]:
                              print("down!")
                              motor_speed =1
                              flag =True
                        elif key[pygame.K_a]:
                              print("left!")
                              if motor_angle >=35:
                                    motor_angle -= 10
                                    flag =True
                        elif key[pygame.K_d]:
                              print("right!")
                              if motor_angle<115:
                                    motor_angle += 10
                                    flag =True
                        elif key[pygame.K_SPACE]:
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
      pygame.quit()

if __name__=='__main__':
      try:
            motor()
      except rospy.ROSInterruptException:
            pass


