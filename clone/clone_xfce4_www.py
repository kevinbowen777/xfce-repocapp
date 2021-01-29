#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: clone_xfce4_www.py
# Purpose: Clones Xfce4 www repositories from
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

os.makedirs('../www', exist_ok=True)
os.chdir('../www')

for item in xfce4_www_list:
    os.system('git clone https:/lab.xfce.org/www/' + item + '.git')
