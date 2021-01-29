#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce4_apps.py
# Purpose: update local Xfce4 apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce4_apps_list = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
                   'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
                   'xfce4-panel-profiles', 'xfce4-screensaver',
                   'xfce4-screenshooter', 'xfce4-taskmanager',
                   'xfce4-terminal', 'xfce4-volumed-pulse',
                   'xfdashboard', 'xfmpc']

os.chdir('../apps')

for item in xfce4_apps_list:
    os.chdir(item)
    os.system('git pull ')
    os.chdir('../')
