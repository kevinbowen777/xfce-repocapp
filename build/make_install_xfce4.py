#!/usr/bin/env python3
# Delete all Xfce4 repositories
# created: 20190519
# version: 0.1
# @author: kevin.bowen@gmail.com

import os

build_list = ['libxfce4util', 'xfconf', 'libxfce4ui', 'garcon', 'exo',
              'xfce4-panel', 'thunar', 'xfce4-settings',
              'xfce4-session', 'xfdesktop', 'xfwm4', 'xfce4-appfinder']

os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"
print(os.environ["PKG_CONFIG_PATH"])
for item in build_list:
    os.chdir(item)
    os.system('sudo make install')
    os.chdir("..")
