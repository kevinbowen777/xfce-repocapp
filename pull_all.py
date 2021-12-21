#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_all.py
# Purpose: update oll of the local Xfce repositories pulled from
#           https://gitlab.xfce.org/
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.pull_xfce(component='apps', comp_list=cappdata.apps_list())
cappdata.pull_xfce(component='bindings', comp_list=cappdata.bindings_list())
cappdata.pull_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
cappdata.pull_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
cappdata.pull_xfce(component='www', comp_list=cappdata.www_list())
cappdata.pull_xfce(component='xfce', comp_list=cappdata.core_list())
