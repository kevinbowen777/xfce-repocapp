#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_xfce_bindings.py
# Purpose: Clone Xfce bindings repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}}} ------------------------------------------------------------------ #

import os
import sys
from repo_arrays import xfce_bindings_list

sys.path.append('./')


os.makedirs('../bindings', exist_ok=True)
os.chdir('../bindings')

for item in xfce_bindings_list:
    os.system('git clone https://gitlab.xfce.org/bindings/' + item + '.git')
