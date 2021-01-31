#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce_www.py
# Purpose: update local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.3
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


xfce_www_list = ['archive.xfce.org', 'blog.xfce.org',
                  'cdn.xfce.org', 'forum.xfce.org', 'moka',
                  'wiki.xfce.org', 'www.xfce.org']

os.chdir('../www')

for item in xfce_www_list:
    os.chdir(item)
    print('\n' + item + ':')
    os.system('git pull')
    os.chdir('../')
