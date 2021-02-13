#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_bindings.py
# Purpose: delete the local Xfce bindings repositories originally pulled from
#           https://gitlab.xfce.org/bindings
#
# version: 0.6
# updated: 20210212
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
import shutil

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from repo_arrays import xfce_bindings_list
from query import query_yes_no

os.chdir(currentdir)


confirm = query_yes_no('Are you sure you want to remove the Xfce bindings repositories? ')
if confirm == 'yes':
    for item in xfce_bindings_list:
        filePath = ('../../bindings/' + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree('../../bindings')
        print('The bindings directory has been deleted.')
    except:
        print("Error while deleting bindings directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
