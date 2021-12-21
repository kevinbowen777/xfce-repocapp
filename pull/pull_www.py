#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: pull_www.py
# Purpose: update local Xfce www repositories pulled from
#           https://gitlab.xfce.org/www
#
# version: 0.7.1
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import cappdata

cappdata.pull_xfce(component='www', comp_list=cappdata.www_list())
