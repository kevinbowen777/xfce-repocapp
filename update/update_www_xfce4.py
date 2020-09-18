#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: update_www_xfce4.py
# Purpose: Updates Xfce4 www repositories from gitlab.xfce.org/www
#
#
# version: 0.1
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


www_list = ['archive.xfce.org', 'blog.xfce.org', 'bugzilla.xfce.org',
            'cdn.xfce.org', 'forum.xfce.org', 'moka',
            'wiki.xfce.org', 'www.xfce.org']

os.chdir('../../www')

for item in www_list:
    os.chdir(item)
    os.system('git pull')
    os.chdir('../')
