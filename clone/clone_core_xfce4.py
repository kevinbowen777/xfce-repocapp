#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_core_xfce4.py
# Purpose: Clones Xfce4 git core repositories from gitlab.xfce.org/xfce
#
#
# version: 0.2
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

os.mkdir('../../core')
os.chdir('../../core')

for item in core_list:
    os.system('git clone https://gitlab.xfce.org/xfce/' + item)
