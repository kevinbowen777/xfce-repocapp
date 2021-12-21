#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_bindings.py
# Purpose: Install Xfce bindings into system
#
# version: 0.7.1
# updated: 20211215
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.install_xfce(component='bindings',
                      comp_list=cappdata.bindings_list())
