#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce4_bindings.py
# Purpose: update local Xfce4 binding repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce4_bindings_list = ['thunarx-python', 'xfce4-vala']

os.chdir('../bindings')

for item in xfce4_bindings_list:
    os.chdir(item)
    os.system('git pull')
    os.chdir('../')
