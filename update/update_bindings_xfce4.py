#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_bindings_xfce4.py
# Purpose: Update Xfce4 git bindings repositories from gitlab.xfce.org/bindings
#
#
# version: 0.1
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


bindings_list = ['thunarx-python', 'xfce4-vala']

os.chdir('../../bindings')

for item in bindings_list:
    os.chdir(item)
    os.system('git pull')
    os.chdir('../')
