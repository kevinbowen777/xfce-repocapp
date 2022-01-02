#!/usr/bin/env python3

"""
Name: clone_xfce.py
Purpose: Clones Xfce repositories pulled from
           https://gitlab.xfce.org/

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.4
updated: 20220101
@author: kevin.bowen@gmail.com
"""

import argparse
import os
import sys
import cappdata

parser = argparse.ArgumentParser(
    description="clone groups of Xfce components")
parser.add_argument("-c", "--component", action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'www', 'all'],
                    help="specify a component group to clone")
parser.add_argument('--version', action='version', version='%(prog)s 0.8.4')
args = parser.parse_args()


def clone_xfce(component, comp_list):
    """ Run 'git clone' for selected components. """
    print(f"Cloning the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    success_count = 0

    os.makedirs(repopath, exist_ok=True)
    os.chdir(repopath)

    for item in comp_list:
        if os.path.isdir(item):
            print(f"\nThe '{item}' directory already exists. Skipping...\n")
            print('\u2248' * 16)
        else:
            os.system('git clone https://gitlab.xfce.org/' + component + '/'
                      + item + '.git')
            success_count += 1
            print('\u2248' * 16)
            print(f"{item} repository cloned successfully.")
            print(f"{success_count}/{len(comp_list)} "
                  f"'{component}' repositories cloned successfully.")
            print('\u2248' * 16)


def main():
    """ Calls to cappdata for component lists. """
    if args.component == 'apps':
        clone_xfce(component='apps',
                   comp_list=cappdata.apps_list())
    elif args.component == 'bindings':
        clone_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
    elif args.component == 'xfce':
        clone_xfce(component='xfce',
                   comp_list=cappdata.core_list())
    elif args.component == 'panel-plugins':
        clone_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
    elif args.component == 'thunar-plugins':
        clone_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
    elif args.component == 'www':
        clone_xfce(component='www', comp_list=cappdata.www_list())
    elif args.component == 'all':
        clone_xfce(component='apps',
                   comp_list=cappdata.apps_list())
        clone_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
        clone_xfce(component='xfce',
                   comp_list=cappdata.core_list())
        clone_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
        clone_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
        clone_xfce(component='www', comp_list=cappdata.www_list())
    else:
        clone_xfce(component='apps', comp_list=cappdata.apps_list())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
