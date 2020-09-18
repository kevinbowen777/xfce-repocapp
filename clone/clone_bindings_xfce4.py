#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_bindings_xfce4.py
# Purpose: Clone Xfce4 git bindings repositories from gitlab.xfce.org/bindings
#
#
# version: 0.2
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


bindings_list = ['thunarx-python', 'xfce4-vala']

os.mkdir('../../bindings')
os.chdir('../../bindings')

for item in bindings_list:
    os.system('git clone https://gitlab.xfce.org/bindings/' + item)
