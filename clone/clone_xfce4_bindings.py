#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_xfce4_bindings.py
# Purpose: Clone Xfce4 git bindings repositories from gitlab.xfce.org/bindings
#
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce4_bindings_list = ['thunarx-python', 'xfce4-vala']

os.makedirs('../bindings', exist_ok=True)
os.chdir('../bindings')

for item in xfce4_bindings_list:
    os.system('git clone https://gitlab.xfce.org/bindings/' + item + '.git')
