#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce_core.py
# Purpose: install local Xfce core repositories
#
# version: 0.1
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')
from repo_arrays import xfce_core_list


os.chdir('../core')

for item in xfce_core_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
