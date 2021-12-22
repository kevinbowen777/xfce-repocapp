#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: clean_xfce.py
# Purpose: Clean local Xfce repository directories
#
# source: https://gitlab.com/kevinbowen/xfce-repocapp
# version: 0.8.1
# updated: 20211222
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------- #

import argparse
import os
import time
import cappdata

parser = argparse.ArgumentParser(
    description="clean groups of Xfce components")
parser.add_argument("-c", "--component", action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'all'],
                    help="specify a component group to clean")
parser.add_argument('--version', action='version', version='%(prog)s 0.8.0')
args = parser.parse_args()


def clean_xfce(component, comp_list):
    print(f"Cleaning the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    success_count = 0

    if os.path.isdir(repopath):
        os.chdir(repopath)
        for item in comp_list:
            if os.path.isdir(item):
                os.chdir(item)
                print('\nCleaning ' + item + ' directory...\n')
                time.sleep(1.5)
                os.system('make -s clean')
                success_count += 1
                print(f"{success_count}/{len(comp_list)} "
                      f"'{component}' repositories cleaned.")
                print('\nExiting ' + item + ' directory...\n')
                print('=' * 16)
                os.chdir('..')
            else:
                print('\nNothing to do...\n')
                print(f"The '{item}' repo does not exist.\n\n"
                      "Perhaps you need to clone it first.\n")
                print('=' * 16)

    else:
        print('Nothing to do...\n')
        print(f"The '{component}' repositories do not exist.\n\n"
              "Perhaps you need to clone the directory first.\n")
        print('=' * 16)


def main():
    if args.component == 'apps':
        clean_xfce(component='apps',
                   comp_list=cappdata.apps_list())
    elif args.component == 'bindings':
        clean_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
    elif args.component == 'xfce':
        clean_xfce(component='xfce',
                   comp_list=cappdata.core_list())
    elif args.component == 'panel-plugins':
        clean_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
    elif args.component == 'thunar-plugins':
        clean_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
    elif args.component == 'www':
        clean_xfce(component='www', comp_list=cappdata.www_list())
    elif args.component == 'all':
        clean_xfce(component='apps',
                   comp_list=cappdata.apps_list())
        clean_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
        clean_xfce(component='xfce',
                   comp_list=cappdata.core_list())
        clean_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
        clean_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
        clean_xfce(component='www', comp_list=cappdata.www_list())
    else:
        clean_xfce(component='apps', comp_list=cappdata.apps_list())


if __name__ == '__main__':
    main()
