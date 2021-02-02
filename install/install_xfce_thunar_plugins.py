#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_thunar_plugins.py
# Purpose: Install Xfce4 thunar-plugins into system
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os


xfce_thunar_plugins_list = ['thunar-archive-plugin',
                             'thunar-media-tags-plugin',
                             'thunar-shares-plugin', 'thunar-vcs-plugin']

for item in xfce_thunar_plugins_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
