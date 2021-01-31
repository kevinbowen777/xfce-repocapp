#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: install_xfce_apps.py
# Purpose: Install Xfce apps into system
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce_apps_list = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
                   'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
                   'xfce4-panel-profiles', 'xfce4-screensaver',
                   'xfce4-screenshooter', 'xfce4-taskmanager',
                   'xfce4-terminal', 'xfce4-volumed-pulse', 'xfdashboard',
                   'xfmpc']

for item in xfce_apps_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
