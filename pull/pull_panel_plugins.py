#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_panel-plugins.py
# Purpose: update local Xfce panel-plugin repositories pulled from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.pull_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
