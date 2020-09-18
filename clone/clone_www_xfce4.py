#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_www_xfce4.py
# Purpose: Clones Xfce4 www repositories from gitlab.xfce.org/www
#
#
# version: 0.2
# updated: 20200917
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


www_list = ['archive.xfce.org', 'blog.xfce.org', 'bugzilla.xfce.org',
            'cdn.xfce.org', 'forum.xfce.org', 'moka',
            'wiki.xfce.org', 'www.xfce.org']

os.mkdir('../../www')
os.chdir('../../www')

for item in www_list:
    os.system('git clone https://gitlab.xfce.org/www/' + item)
