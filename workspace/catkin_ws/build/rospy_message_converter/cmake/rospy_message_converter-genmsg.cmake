# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "rospy_message_converter: 3 messages, 0 services")

set(MSG_I_FLAGS "-Irospy_message_converter:/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg;-Istd_msgs:/home/hyeok/ros_catkin_ws/install/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(rospy_message_converter_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" NAME_WE)
add_custom_target(_rospy_message_converter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rospy_message_converter" "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" ""
)

get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" NAME_WE)
add_custom_target(_rospy_message_converter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rospy_message_converter" "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" ""
)

get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" NAME_WE)
add_custom_target(_rospy_message_converter_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "rospy_message_converter" "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_cpp(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_cpp(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rospy_message_converter
)

### Generating Services

### Generating Module File
_generate_module_cpp(rospy_message_converter
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rospy_message_converter
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(rospy_message_converter_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(rospy_message_converter_generate_messages rospy_message_converter_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_cpp _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_cpp _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_cpp _rospy_message_converter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rospy_message_converter_gencpp)
add_dependencies(rospy_message_converter_gencpp rospy_message_converter_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rospy_message_converter_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_eus(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_eus(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rospy_message_converter
)

### Generating Services

### Generating Module File
_generate_module_eus(rospy_message_converter
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rospy_message_converter
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(rospy_message_converter_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(rospy_message_converter_generate_messages rospy_message_converter_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_eus _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_eus _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_eus _rospy_message_converter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rospy_message_converter_geneus)
add_dependencies(rospy_message_converter_geneus rospy_message_converter_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rospy_message_converter_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_lisp(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_lisp(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rospy_message_converter
)

### Generating Services

### Generating Module File
_generate_module_lisp(rospy_message_converter
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rospy_message_converter
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(rospy_message_converter_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(rospy_message_converter_generate_messages rospy_message_converter_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_lisp _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_lisp _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_lisp _rospy_message_converter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rospy_message_converter_genlisp)
add_dependencies(rospy_message_converter_genlisp rospy_message_converter_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rospy_message_converter_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_nodejs(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_nodejs(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rospy_message_converter
)

### Generating Services

### Generating Module File
_generate_module_nodejs(rospy_message_converter
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rospy_message_converter
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(rospy_message_converter_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(rospy_message_converter_generate_messages rospy_message_converter_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_nodejs _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_nodejs _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_nodejs _rospy_message_converter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rospy_message_converter_gennodejs)
add_dependencies(rospy_message_converter_gennodejs rospy_message_converter_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rospy_message_converter_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_py(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter
)
_generate_msg_py(rospy_message_converter
  "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter
)

### Generating Services

### Generating Module File
_generate_module_py(rospy_message_converter
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(rospy_message_converter_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(rospy_message_converter_generate_messages rospy_message_converter_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/TestArray.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_py _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8Array3TestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_py _rospy_message_converter_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/hyeok/workspace/catkin_ws/src/rospy_message_converter/msg/Uint8ArrayTestMessage.msg" NAME_WE)
add_dependencies(rospy_message_converter_generate_messages_py _rospy_message_converter_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(rospy_message_converter_genpy)
add_dependencies(rospy_message_converter_genpy rospy_message_converter_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS rospy_message_converter_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rospy_message_converter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/rospy_message_converter
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(rospy_message_converter_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rospy_message_converter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/rospy_message_converter
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(rospy_message_converter_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rospy_message_converter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/rospy_message_converter
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(rospy_message_converter_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rospy_message_converter)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/rospy_message_converter
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(rospy_message_converter_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter)
  install(CODE "execute_process(COMMAND \"/usr/bin/python3\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter
    DESTINATION ${genpy_INSTALL_DIR}
    # skip all init files
    PATTERN "__init__.py" EXCLUDE
    PATTERN "__init__.pyc" EXCLUDE
  )
  # install init files which are not in the root folder of the generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter
    DESTINATION ${genpy_INSTALL_DIR}
    FILES_MATCHING
    REGEX "${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/rospy_message_converter/.+/__init__.pyc?$"
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(rospy_message_converter_generate_messages_py std_msgs_generate_messages_py)
endif()
