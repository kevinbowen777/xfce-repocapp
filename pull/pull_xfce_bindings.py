#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce_bindings.py
# Purpose: update local Xfce binding repositories pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_bindings_list

os.chdir('../bindings')

for item in xfce_bindings_list:
    os.chdir(item)
    print('Updating ' + item + ':')
    os.system('git pull')
    os.chdir('../')
