#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: git_core_xfce4.py
# Purpose: Pulls Xfce4 git core code from GitLab repositories
#
#
# version: 0.1
# updated: 20200523
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


panel_list = ['xfwm4', 'xfdesktop', 'xfconf', 'xfce4-settings',
              'xfce4-session', 'xfce4-power-manager', 'xfce4-panel',
              'xfce4-dev-tools', 'xfce4-appfinder',
              'tumbler', 'thunar-volman', 'thunar', 'libxfce4util',
              'libxfce4ui', 'garcon', 'exo']

os.mkdir('../core')
os.chdir('../core')

for item in panel_list:
    os.system('git clone https://gitlab.xfce.org/xfce/' + item)
