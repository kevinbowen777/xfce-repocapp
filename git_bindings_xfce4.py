#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: git_bindings_xfce4.py
# Purpose: Pulls Xfce4 git bindings code from GitLab repositories
#
#
# version: 0.1
# updated: 20200523
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


panel_list = ['xfce4-vala', 'thunarx-python']

os.mkdir('../bindings')
os.chdir('../bindings')

for item in panel_list:
    os.system('git clone https://gitlab.xfce.org/bindings/' + item)
