#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce_apps.py
# Purpose: update local Xfce apps repositories pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce_apps_list = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
                   'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
                   'xfce4-panel-profiles', 'xfce4-screensaver',
                   'xfce4-screenshooter', 'xfce4-taskmanager',
                   'xfce4-terminal', 'xfce4-volumed-pulse',
                   'xfdashboard', 'xfmpc']

os.chdir('../apps')

for item in xfce_apps_list:
    os.chdir(item)
    print('\n' + item + ':')
    os.system('git pull ')
    os.chdir('../')
