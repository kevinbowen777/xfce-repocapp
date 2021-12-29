#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: install_xfce.py
# Purpose: Install Xfce components into system
#
# source: https://gitlab.com/kevinbowen/xfce-repocapp
# version: 0.8.3
# updated: 20211228
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import argparse
import os
import cappdata

parser = argparse.ArgumentParser(
    description="install groups of Xfce components")
parser.add_argument("-c", "--component", action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'all'],
                    help="specify a component group to install")
parser.add_argument('--version', action='version', version='%(prog)s 0.8.0')
args = parser.parse_args()


def install_xfce(component, comp_list):
    print(f"Installing the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)

    if os.path.isdir(repopath):
        os.chdir(repopath)
        for item in comp_list:
            if os.path.isdir(item):
                os.chdir(item)
                confirm = cappdata.query_yes_no(
                    f"Do you want to install '{item}' to the system? "
                    f"Answer 'No' to install locally. ")
                if confirm == 'yes':
                    print('Installing ' + item + ' to the system...')
                    os.system('sudo make install')
                    print('=' * 16)
                    os.chdir("..")
                else:
                    print('Installing ' + item + ' locally...')
                    os.system('make install')
                    print('=' * 16)
                    os.chdir("..")
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
        install_xfce(component='apps',
                     comp_list=cappdata.apps_list())
    elif args.component == 'bindings':
        install_xfce(component='bindings',
                     comp_list=cappdata.bindings_list())
    elif args.component == 'xfce':
        install_xfce(component='xfce',
                     comp_list=cappdata.core_list())
    elif args.component == 'panel-plugins':
        install_xfce(component='panel-plugins',
                     comp_list=cappdata.panel_plugins_list())
    elif args.component == 'thunar-plugins':
        install_xfce(component='thunar-plugins',
                     comp_list=cappdata.thunar_plugins_list())
    elif args.component == 'all':
        install_xfce(component='apps',
                     comp_list=cappdata.apps_list())
        install_xfce(component='bindings',
                     comp_list=cappdata.bindings_list())
        install_xfce(component='xfce',
                     comp_list=cappdata.core_list())
        install_xfce(component='panel-plugins',
                     comp_list=cappdata.panel_plugins_list())
        install_xfce(component='thunar-plugins',
                     comp_list=cappdata.thunar_plugins_list())
    else:
        install_xfce(component='apps', comp_list=cappdata.apps_list())


if __name__ == '__main__':
    main()
