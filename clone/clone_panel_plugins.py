#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: clone_panel_plugins.py
# Purpose: Clones Xfce4 panel-plugins repositories pulled  from
#           https://gitlab.xfce.org/panel-plugins
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.clone_xfce(component='panel-plugins',
                    comp_list=cappdata.panel_plugins_list())
