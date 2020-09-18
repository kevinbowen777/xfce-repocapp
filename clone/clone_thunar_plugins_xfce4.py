#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_thunar_plugins_xfce4.py
# Purpose: Clones Xfce4 git thunar-plugins repositoriies from gitlab.xfce.org
#
#
# version: 0.2
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


thunar_plugin_list = ['thunar-archive-plugin', 'thunar-media-tags-plugin',
                      'thunar-shares-plugin', 'thunar-vcs-plugin']

os.mkdir('../../thunar-plugins')
os.chdir('../../thunar-plugins')

for item in thunar_plugin_list:
    os.system('git clone https://gitlab.xfce.org/thunar-plugins/' + item)
