#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_core_xfce4.py
# Purpose: Pulls Xfce4 git core code from GitLab repositories
#
#
# version: 0.1
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


core_list = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
             'thunar', 'thunar-volman', 'tumbler',
             'xfce4-appfinder', 'xfce4-dev-tools',
             'xfce4-panel', 'xfce4-power-manager', 'xfce4-session',
             'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']

os.chdir('../../core')

for item in core_list:
    os.chdir(item)
    os.system('git pull ')
    os.chdir('../')
