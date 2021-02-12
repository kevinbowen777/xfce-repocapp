#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_apps.py
# Purpose: Install Xfce apps into system
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')
from repo_arrays import xfce_apps_list


os.chdir('../apps')

for item in xfce_apps_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
