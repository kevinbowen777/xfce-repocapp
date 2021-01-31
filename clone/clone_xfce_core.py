#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_xfce_core.py
# Purpose: Clones Xfce core repositories pulled from 
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

os.makedirs('../core', exist_ok=True)
os.chdir('../core')

for item in xfce_core_list:
    os.system('git clone https://gitlab.xfce.org/xfce/' + item + '.git')
