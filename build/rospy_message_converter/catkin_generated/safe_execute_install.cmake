execute_process(COMMAND "/home/hyeok/workspace/catkin_ws/build/rospy_message_converter/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/hyeok/workspace/catkin_ws/build/rospy_message_converter/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
