#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_bindings.py
# Purpose: Clean local Xfce bindings repository directories
#
# version: 0.7
# updated: 20211207
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import os
import sys
import time

import cappdata

component = 'bindings'

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

repopath = cappdata.repodir(component)
os.chdir(currentdir)

clean_success_count = 0

if os.path.isdir(repopath):
    os.chdir(cappdata.repodir(component))
    for item in cappdata.bindings_list():
        if os.path.isdir('../' + component + '/' + item):
            os.chdir(item)
            print('\nCleaning ' + item + ' directory...\n')
            time.sleep(1.5)
            os.system('make -s clean')
            clean_success_count += 1
            print(f"{clean_success_count}/{len(cappdata.bindings_list())} "
                  f"'{component}' repositories cleaned.")
            print('\nExiting ' + item + ' directory...\n')
            print('=' * 16)
            os.chdir('..')
        else:
            print(f"\nThe '{item}' repo does not exist. "
                  "Perhaps you need to clone & build it first.\n")
            print('=' * 16)
