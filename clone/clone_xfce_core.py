#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_core.py
# Purpose: Clones Xfce core repositories pulled from
#           https://gitlab.xfce.org/xfce
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
from repo_arrays import xfce_core_list

sys.path.append('./')


os.makedirs('../core', exist_ok=True)
os.chdir('../core')

for item in xfce_core_list:
    os.system('git clone https://gitlab.xfce.org/xfce/' + item + '.git')
