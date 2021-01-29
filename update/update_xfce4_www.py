#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_xfce4_www.py
# Purpose: update local Xfce4 www repositories pulled from
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

os.chdir('../www')

for item in xfce4_www_list:
    os.chdir(item)
    os.system('git pull')
    os.chdir('../')
