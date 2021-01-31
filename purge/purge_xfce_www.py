#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: purge_xfce_www.py
# Purpose: delete the local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.3
# updated: 20210128
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce4_www_list = ['archive.xfce.org', 'blog.xfce.org',
                  'cdn.xfce.org', 'forum.xfce.org', 'moka',
                  'wiki.xfce.org', 'www.xfce.org']

confirm = input('Are you sure you want to remove the Xfce www repositories? ')
if confirm.lower() == 'yes':
    for item in xfce4_www_list:
        os.system('rm -rf ../www/' + item)
        print("The " + item + " Xfce www repositories have been purged.")
    os.system('rmdir ../www/')
    print('The www directory has been deleted.')
else:
    print("No repositories have been deleted. Have a nice day.")
