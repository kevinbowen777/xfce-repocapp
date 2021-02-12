#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_panel_plugins.py
# Purpose: Install Xfce4 panel-plugins into system
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')
from repo_arrays import xfce_panel_plugins_list


os.chdir('../panel-plugins')

for item in xfce_panel_plugins_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
