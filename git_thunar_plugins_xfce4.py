#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: git_thunar_plugins_xfce4.py
# Purpose: Pulls Xfce4 git thunar-plugins code from GitLab repositories
#
#
# version: 0.1
# updated: 20200523
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


panel_list = ['thunar-vcs-plugin', 'thunar-shares-plugin',
              'thunar-media-tags-plugin', 'thunar-archive-plugin']

os.mkdir('../thunar-plugins')
os.chdir('../thunar-plugins')

for item in panel_list:
    os.system('git clone https://gitlab.xfce.org/thunar-plugins/' + item)
