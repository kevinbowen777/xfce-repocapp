#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_apps.py
# Purpose: Build local Xfce apps repositories
#
# version: 0.1
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os

xfce_apps_list = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
             'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
             'xfce4-panel-profiles', 'xfce4-screensaver',
             'xfce4-screenshooter', 'xfce4-taskmanager', 'xfce4-terminal',
             'xfce4-volumed-pulse', 'xfdashboard', 'xfmpc']

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"
print(os.environ["PKG_CONFIG_PATH"])
for item in xfce_apps_list:
    os.chdir(item)
    os.system('./autogen.sh --prefix=/usr && make >> ../logs/xfce_build.log')
    os.chdir("..")
