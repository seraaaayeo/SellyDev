# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/home/hyeok/ros_catkin_ws/install/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/home/hyeok/ros_catkin_ws/install/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/home/hyeok/workspace/catkin_ws/devel_isolated/zed_interfaces;/home/hyeok/workspace/catkin_ws/devel_isolated/zed_examples;/home/hyeok/workspace/catkin_ws/devel_isolated/zed_display_rviz;/home/hyeok/workspace/catkin_ws/devel_isolated/zed_depth_sub_tutorial;/home/hyeok/workspace/catkin_ws/devel_isolated/zed_ar_track_alvar_example;/home/hyeok/workspace/catkin_ws/devel_isolated/ydlidar;/home/hyeok/workspace/catkin_ws/devel_isolated/selly;/home/hyeok/workspace/catkin_ws/devel_isolated/carto_mapper;/home/hyeok/catkin_ws/install_isolated;/home/hyeok/ros_catkin_ws/install;/home/hyeok/workspace/catkin_ws/devel;/opt/ros/melodic".split(';'):
        python_path = os.path.join(workspace, 'lib/python3/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/hyeok/workspace/catkin_ws/devel_isolated/zed_multicamera_example/env.sh')

output_filename = '/home/hyeok/workspace/catkin_ws/build_isolated/zed_multicamera_example/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
