#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_xfce_thunar_plugins.py
# Purpose: Clones Xfce4 thunar-plugins repositories pulled from
#           https:/lab.xfce.org/thunar-plugins
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce_thunar_plugins_list = ['thunar-archive-plugin',
                             'thunar-media-tags-plugin',
                             'thunar-shares-plugin', 'thunar-vcs-plugin']

os.makedirs('../thunar-plugins', exist_ok=True)
os.chdir('../thunar-plugins')

for item in xfce_thunar_plugins_list:
    os.system('git clone https://gitlab.xfce.org/thunar-plugins/' + item + '.git')
