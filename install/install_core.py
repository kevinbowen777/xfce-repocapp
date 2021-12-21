#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_core.py
# Purpose: install local Xfce core repositories
#
# version: 0.7.1
# updated: 20211215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.install_xfce(component='xfce', comp_list=cappdata.core_list())
