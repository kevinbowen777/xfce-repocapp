#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce4_thunar_plugins.py
# Purpose: delete Xfce4 local thunar-plugin repositories pulled from
#           https://gitlab.xfce.org/thunar-plugins
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce4_thunar_plugins_list = ['thunar-archive-plugin',
                             'thunar-media-tags-plugin',
                             'thunar-shares-plugin', 'thunar-vcs-plugin']

confirm = input('Are you sure you want to remove the Xfce thunar-plugins'
                ' repositories? ')
if confirm.lower() == 'yes':
    for item in xfce4_thunar_plugins_list:
        os.system('rm -rf ../thunar-plugins/' + item)
        print("The " + item + " Xfce thunar-plugin repo has been purged.")
    os.system('rmdir ../thunar-plugins/')
    print('The thunar-plugins directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
