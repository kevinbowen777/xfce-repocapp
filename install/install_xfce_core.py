#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: install_xfce_core.py
# Purpose: install local Xfce core repositories
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce_core_list = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
             'thunar', 'thunar-volman', 'tumbler',
             'xfce4-appfinder', 'xfce4-dev-tools',
             'xfce4-panel', 'xfce4-power-manager', 'xfce4-session',
             'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']

for item in xfce_core_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
