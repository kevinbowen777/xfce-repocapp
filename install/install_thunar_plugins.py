#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_thunar_plugins.py
# Purpose: Install Xfce4 thunar-plugins into system
#
# version: 0.7.1
# updated: 20211215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.install_xfce(component='thunar-plugins',
                      comp_list=cappdata.thunar_plugins_list())
