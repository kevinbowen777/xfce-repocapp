#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce4_bindings.py
# Purpose: delete Xfce4 bindings repositories from
#           https://gitlab.xfce.org/bindings
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce4_bindings_list = ['thunarx-python', 'xfce4-vala']

confirm = input('Are you sure you want to remove the Xfce bindings '
                'repositories? ')
if confirm.lower() == 'yes':
    for item in xfce4_bindings_list:
        os.system('rm -rf ../bindings/' + item)
        print("The " + item + " Xfce bindings repo has been purged.")
    os.system('rmdir ../bindings/')
    print('The bindings directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
