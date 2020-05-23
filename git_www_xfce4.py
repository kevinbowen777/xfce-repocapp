#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: git_www_xfce4.py
# Purpose: Pulls Xfce4 www code from GitLab repositories
#
#
# version: 0.1
# updated: 20200523
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os


panel_list = ['www.xfce.org', 'wiki.xfce.org', 'moka', 'forum.xfce.org',
              'cdn.xfce.org', 'bugzilla.xfce.org', 'blog.xfce.org',
              'archive.xfce.org']

os.mkdir('../www')
os.chdir('../www')

for item in panel_list:
    os.system('git clone https://gitlab.xfce.org/www/' + item)
