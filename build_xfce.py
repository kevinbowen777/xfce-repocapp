#!/usr/bin/env python3

"""
Name: build_xfce.py
Purpose: Build local Xfce repositories

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.4
updated: 20220101
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import sys
import time
import cappdata

parser = argparse.ArgumentParser(
    description="build groups of Xfce components")
parser.add_argument("-c", "--component", action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'all'],
                    help="specify a component group to build")
parser.add_argument('--version', action='version', version='%(prog)s 0.8.4')
args = parser.parse_args()


def build_xfce(component, comp_list):
    """ Run autogen.sh and make on selected components. """
    print(f"Building the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    os.environ["PKG_CONFIG_PATH"] = "/usr/lib/pkgconfig:/usr"

    if os.path.isdir(repopath):
        os.chdir(repopath)
        for item in comp_list:
            if os.path.isdir(item):
                os.chdir(item)
                print('\nRunning autogen.sh for ' + item + '...\n')
                os.system('./autogen.sh --prefix=/usr')
                print('\nRunning make for ' + item + '...\n')
                time.sleep(1.5)
                os.system('make')
                print('\u2248' * 16)
                os.chdir("..")
            else:
                print('\nNothing to do...\n')
                print(f"The '{item}' repo does not exist.\n\n"
                      "Perhaps you need to clone it first.\n")
                print('\u2248' * 16)

    else:
        print('Nothing to do...\n')
        print(f"The '{component}' repositories do not exist.\n\n"
              "Perhaps you need to clone the directory first.\n")
        print('\u2248' * 16)


def main():
    """ Calls to cappdata for component lists. """
    if args.component == 'apps':
        build_xfce(component='apps',
                   comp_list=cappdata.apps_list())
    elif args.component == 'bindings':
        build_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
    elif args.component == 'xfce':
        build_xfce(component='xfce',
                   comp_list=cappdata.core_list())
    elif args.component == 'panel-plugins':
        build_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
    elif args.component == 'thunar-plugins':
        build_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
    elif args.component == 'all':
        build_xfce(component='apps',
                   comp_list=cappdata.apps_list())
        build_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
        build_xfce(component='xfce',
                   comp_list=cappdata.core_list())
        build_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
        build_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
    else:
        build_xfce(component='apps', comp_list=cappdata.apps_list())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
