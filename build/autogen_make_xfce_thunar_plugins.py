#!/usr/bin/env python3

# {{{ --------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_thunar_plugins.py
# Purpose: Build local Xfce4 core repositories
#
# version: 0.1
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# }}} --------------------------------------------------------------------- #

import os

xfce_thunar_plugins_list = ['thunar-archive-plugin', 'thunar-media-tags-plugin',
                      'thunar-shares-plugin', 'thunar-vcs-plugin']

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"
print(os.environ["PKG_CONFIG_PATH"])
for item in xfce_thunar_plugins_list:
    os.chdir(item)
    os.system('./autogen.sh --prefix=/usr && make >> ../logs/xfce_build.log')
    os.chdir("..")
