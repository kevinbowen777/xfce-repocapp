#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: autogen_make_xfce4_template.py
# Purpose: Build local Xfce4 core repositories
#
# version: 0.1
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce4_core_list = ['exo', 'garcon', 'libxfce4ui', 'libxfce4util',
             'thunar', 'thunar-volman', 'tumbler',
             'xfce4-appfinder', 'xfce4-dev-tools',
             'xfce4-panel', 'xfce4-power-manager', 'xfce4-session',
             'xfce4-settings', 'xfconf', 'xfdesktop', 'xfwm4']

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"
print(os.environ["PKG_CONFIG_PATH"])
for item in build_xfce_core_list:
    os.chdir(item)
    os.system('./autogen.sh --prefix=/usr && make >> ../logs/xfce4_build.log')
    os.chdir("..")
