#!/usr/bin/env python3

# ---------------------------------------------------------------------- #
#
# Name: autogen_make_xfce_bindings.py
# Purpose: Build local Xfce bindings repositories
#
# version: 0.1
# updated: 20210130
# @author: kevin.bowen@gmail.com
#
# ---------------------------------------------------------------------- #

import os

xfce_bindings_list = ['thunarx-python', 'xfce4-vala']

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"
print(os.environ["PKG_CONFIG_PATH"])
for item in xfce_bindings_list:
    os.chdir(item)
    os.system('./autogen.sh --prefix=/usr && make >> ../logs/xfce4_build.log')
    os.chdir("..")
