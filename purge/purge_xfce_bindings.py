#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_bindings.py
# Purpose: delete the local Xfce bindings repositories originally pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
from repo_arrays import xfce_bindings_list

sys.path.append('./')


confirm = input('Are you sure you want to remove the Xfce bindings '
                'repositories[y|n]? ')
if confirm.lower() == 'y':
    for item in xfce_bindings_list:
        os.system('rm -rf ../bindings/' + item)
        print("The " + item + " Xfce bindings repo has been purged.")
    os.system('rmdir ../bindings/')
    print('The bindings directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
