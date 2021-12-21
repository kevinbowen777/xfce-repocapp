#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_panel_plugins.py
# Purpose: Install Xfce4 panel-plugins into system
#
# version: 0.7.1
# updated: 20211215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.install_xfce(component='panel-plugins',
                      comp_list=cappdata.panel_plugins_list())
