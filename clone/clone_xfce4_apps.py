#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_xfce4_apps.py
# Purpose: Clones Xfce4 apps repositories fromlab.xfce.org/apps
#
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
                   'xfce4-terminal', 'xfce4-volumed-pulse', 'xfdashboard',
                   'xfmpc']

os.makedirs('../apps', exist_ok=True)
os.chdir('../apps')

for item in xfce4_apps_list:
    os.system('clone https:/lab.xfce.org/apps/' + item + '.git')
