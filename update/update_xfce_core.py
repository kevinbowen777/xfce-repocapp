#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce_core.py
# Purpose: update local Xfce core repositories pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce_core_list = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
                   'thunar', 'thunar-volman', 'tumbler',
                   'xfce4-appfinder', 'xfce4-dev-tools',
                   'xfce4-panel', 'xfce4-power-manager', 'xfce4-session',
                   'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']

os.chdir('../core')

for item in xfce_core_list:
    os.chdir(item)
    print('\n' + item + ':')
    os.system('git pull ')
    os.chdir('../')
