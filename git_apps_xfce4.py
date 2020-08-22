#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: git_apps_xfce4.py
# Purpose: Pulls Xfce4 git apps code from GitLab repositories
#
#
# version: 0.1
# updated: 20200821
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


panel_list = ['xfce4-screensaver', 'xfmpc', 'xfdashboard',
              'xfce4-volumed-pulse', 'xfce4-terminal', 'xfce4-taskmanager',
              'xfce4-screenshooter', 'xfce4-panel-profiles',
              'xfce4-notifyd', 'xfce4-mixer', 'xfce4-dict',
              'xfburn', 'ristretto', 'parole', 'mousepad',
              'gigolo', 'catfish']

os.mkdir('../apps')
os.chdir('../apps')

for item in panel_list:
    os.system('git clone https://gitlab.xfce.org/apps/' + item)
