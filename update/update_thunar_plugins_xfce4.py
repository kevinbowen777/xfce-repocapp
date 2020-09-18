#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_thunar_plugins_xfce4.py
# Purpose: Updatess Xfce4 git thunar-plugins repositoriies from gitlab.xfce.org
#
#
# version: 0.1
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


thunar_plugin_list = ['thunar-archive-plugin', 'thunar-media-tags-plugin',
                      'thunar-shares-plugin', 'thunar-vcs-plugin']

os.chdir('../../thunar-plugins')

for item in thunar_plugin_list:
    os.chdir(item)
    os.system('git pull ')
    os.chdir('../')
