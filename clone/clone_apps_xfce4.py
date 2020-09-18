#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_apps_xfce4.py
# Purpose: Clones Xfce4 git apps repositories from gitlab.xfce.org/apps
#
#
# version: 0.2
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

os.mkdir('../../apps')
os.chdir('../../apps')

for item in apps_list:
    os.system('git clone https://gitlab.xfce.org/apps/' + item)
