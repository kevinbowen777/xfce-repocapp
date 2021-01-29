#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce4_thunar_plugins.py
# Purpose: update local Xfce4 thunar-plugin repositories pulled from
#           https://gitlab.xfce.org/thunar-plugins
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce4_thunar_plugins_list = ['thunar-archive-plugin',
                             'thunar-media-tags-plugin',
                             'thunar-shares-plugin',
                             'thunar-vcs-plugin']

os.chdir('../thunar-plugins')

for item in xfce4_thunar_plugins_list:
    os.chdir(item)
    print('\n' + item + ':')
    os.system('git pull ')
    os.chdir('../')
