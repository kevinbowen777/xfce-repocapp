#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_www.py
# Purpose: delete the local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
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


from repo_arrays import xfce_www_list
from query import query_yes_no
from repodir import repodir

repopath = repodir('www')
os.chdir(currentdir)

confirm = query_yes_no('Are you sure you want to remove the Xfce www '
                       'repositories? ')
if confirm == 'yes':
    for item in xfce_www_list:
        filePath = (repopath + item)
        try:
            shutil.rmtree(filePath)
            print(item + ' directory has been deleted.')
        except ValueError:
            print("Error while deleting", item + " directory.")
    try:
        shutil.rmtree(repopath)
        print('The www directory has been deleted.')
    except ValueError:
        print("Error while deleting www directory.")
else:
    print("No repositories have been deleted. Have a nice day.")
