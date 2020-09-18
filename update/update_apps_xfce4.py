#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_apps_xfce4.py
# Purpose: Updates Xfce4 git apps repositories from GitLab repositories
#
#
# version: 0.1
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


apps_list = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
             'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
             'xfce4-panel-profiles', 'xfce4-screensaver',
             'xfce4-screenshooter', 'xfce4-taskmanager', 'xfce4-terminal',
             'xfce4-volumed-pulse', 'xfdashboard', 'xfmpc']

os.chdir('../../apps')

for item in apps_list:
    os.chdir(item)
    os.system('git pull ')
    os.chdir('../')
