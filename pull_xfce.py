#!/usr/bin/env python3

"""
Name: pull_xfce.py
Purpose: update local Xfce repositories pulled from
           https://gitlab.xfce.org

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
    description="pull/update groups of Xfce components")
parser.add_argument('-c', '--component', action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'www', 'all'],
                    help='specify a component group to pull/update')
parser.add_argument('--version', action='version', version='%(prog)s 0.8.4')
args = parser.parse_args()


def pull_xfce(component, comp_list):
    """ Run 'git pull' on selected components to update repositories. """
    print(f"Updating the Xfce {component} group...")
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
                print('Updating ' + item + '...')
                os.system('git pull')
                success_count += 1
                print(f"\n{success_count}/{len(comp_list)} "
                      f"'{component}' repositories updated successfully.")
                print('\u2248' * 16)
                os.chdir('..')
            else:
                print('\nNothing to do...\n')
                print(f"The '{item}' repository does not exist.\n\n"
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
        pull_xfce(component='apps',
                  comp_list=cappdata.apps_list())
    elif args.component == 'bindings':
        pull_xfce(component='bindings',
                  comp_list=cappdata.bindings_list())
    elif args.component == 'xfce':
        pull_xfce(component='xfce',
                  comp_list=cappdata.core_list())
    elif args.component == 'panel-plugins':
        pull_xfce(component='panel-plugins',
                  comp_list=cappdata.panel_plugins_list())
    elif args.component == 'thunar-plugins':
        pull_xfce(component='thunar-plugins',
                  comp_list=cappdata.thunar_plugins_list())
    elif args.component == 'www':
        pull_xfce(component='www', comp_list=cappdata.www_list())
    elif args.component == 'all':
        pull_xfce(component='apps',
                  comp_list=cappdata.apps_list())
        pull_xfce(component='bindings',
                  comp_list=cappdata.bindings_list())
        pull_xfce(component='xfce',
                  comp_list=cappdata.core_list())
        pull_xfce(component='panel-plugins',
                  comp_list=cappdata.panel_plugins_list())
        pull_xfce(component='thunar-plugins',
                  comp_list=cappdata.thunar_plugins_list())
        pull_xfce(component='www', comp_list=cappdata.www_list())
    else:
        pull_xfce(component='apps', comp_list=cappdata.apps_list())


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
