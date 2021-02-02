#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce_www.py
# Purpose: delete the local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.5
# updated: 20210131
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import sys
sys.path.append('./')

from repo_arrays import xfce_www_list

confirm = input('Are you sure you want to remove the Xfce www '
                'repositories[y|n]? ')
if confirm.lower() == 'y':
    for item in xfce_www_list:
        os.system('rm -rf ../www/' + item)
        print("The " + item + " Xfce www repositories have been purged.")
    os.system('rmdir ../www/')
    print('The www directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
