#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean__xfce_panel_plugins.py
# Purpose: Clean local Xfce panel-plugins repository directories
#
# version: 0.1
# updated: 20210201
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time
sys.path.append('./')

from repo_arrays import xfce_panel_plugins_list

os.chdir('../panel-plugins/')

for item in xfce_panel_plugins_list:
    os.chdir(item)
    print('\nCleaning ' + item + ' directory...\n')
    time.sleep(1.5)
    os.system('make -s clean')
    print('\nExiting ' + item + ' directory...\n')
    os.chdir('..')
