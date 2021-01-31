#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce_apps.py
# Purpose: delete the local Xfce apps repositories originally pulled from
#           https://gitlab.xfce.org/apps
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce_apps_list = ['catfish', 'gigolo', 'mousepad', 'parole', 'ristretto',
                   'xfburn', 'xfce4-dict', 'xfce4-mixer', 'xfce4-notifyd',
                   'xfce4-panel-profiles', 'xfce4-screensaver',
                   'xfce4-screenshooter', 'xfce4-taskmanager',
                   'xfce4-terminal', 'xfce4-volumed-pulse',
                   'xfdashboard', 'xfmpc']

confirm = input('Are you sure you want to remove the Xfce app repos? ')
if confirm.lower() == 'yes':
    for item in xfce_apps_list:
        os.system('rm -rf ../apps/' + item)
        print("The " + item + " Xfce app repo has been purged.")
    os.system('rmdir ../apps/')
    print('The apps directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
