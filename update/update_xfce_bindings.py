#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce_bindings.py
# Purpose: update local Xfce binding repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce_bindings_list = ['thunarx-python', 'xfce4-vala']

os.chdir('../bindings')

for item in xfce_bindings_list:
    os.chdir(item)
    print('\n' + item + ':')
    os.system('git pull')
    os.chdir('../')
