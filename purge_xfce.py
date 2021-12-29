#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: purge_xfce.py
# Purpose: delete the local Xfce repositories originally pulled from
#           https://gitlab.xfce.org
#
# source: https://gitlab.com/kevinbowen/xfce-repocapp
# version: 0.8.3
# updated: 20211228
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import argparse
import shutil
import os
import cappdata

parser = argparse.ArgumentParser(
    description="purge group directories of Xfce components")
parser.add_argument("-c", "--component", action='store',
                    choices=['apps', 'bindings', 'xfce', 'panel-plugins',
                             'thunar-plugins', 'www', 'all'],
                    help="specify a component group to delete")
parser.add_argument('--version', action='version', version='%(prog)s 0.8.0')
args = parser.parse_args()


def purge_xfce(component, comp_list):
    print(f"Purging the Xfce {component} group...")
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    def get_path(comp_group):
        installpath = os.path.abspath(os.path.join(os.getcwd(),
                                                   os.pardir,
                                                   comp_group))

        return installpath

    repopath = get_path(component)
    success_count = 0

    confirm = cappdata.query_yes_no(f"Are you sure you want to remove the "
                                    f"Xfce '{component}' repositories? ")

    if confirm == 'yes':
        if os.path.isdir(repopath):
            os.chdir(repopath)
            for item in comp_list:
                if os.path.isdir(item):
                    try:
                        shutil.rmtree(item)
                        success_count += 1
                        print(f"\nThe '{item}' directory has been deleted.\n")
                        print(f"{success_count}/{len(comp_list)} "
                              f"'{component}' repositories deleted "
                              f"successfully.")
                        print('=' * 16)
                    except FileNotFoundError:
                        print(f"The directory '{item}' does not exist. "
                              f"Skipping...")
                        print('=' * 16)
            os.chdir('..')
            shutil.rmtree(component)
            print(f"\nThe directory '{component}' has been deleted.\n")
            print('=' * 16)
        else:
            print('Nothing to do...\n')
            print(f"The '{component}' repositories do not exist.\n\n"
                  "Perhaps you need to clone the directory first.\n")
            print('=' * 16)

    else:
        print("No repositories have been deleted. Have a nice day.")


def main():
    if args.component == 'apps':
        purge_xfce(component='apps',
                   comp_list=cappdata.apps_list())
    elif args.component == 'bindings':
        purge_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
    elif args.component == 'xfce':
        purge_xfce(component='xfce',
                   comp_list=cappdata.core_list())
    elif args.component == 'panel-plugins':
        purge_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
    elif args.component == 'thunar-plugins':
        purge_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
    elif args.component == 'www':
        purge_xfce(component='www', comp_list=cappdata.www_list())
    elif args.component == 'all':
        purge_xfce(component='apps',
                   comp_list=cappdata.apps_list())
        purge_xfce(component='bindings',
                   comp_list=cappdata.bindings_list())
        purge_xfce(component='xfce',
                   comp_list=cappdata.core_list())
        purge_xfce(component='panel-plugins',
                   comp_list=cappdata.panel_plugins_list())
        purge_xfce(component='thunar-plugins',
                   comp_list=cappdata.thunar_plugins_list())
        purge_xfce(component='www', comp_list=cappdata.www_list())
    else:
        purge_xfce(component='apps', comp_list=cappdata.apps_list())


if __name__ == '__main__':
    main()
