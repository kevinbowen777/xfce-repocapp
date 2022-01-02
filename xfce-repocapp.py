#!/usr/bin/env python3

"""
Name: xfce-repocapp.py
Purpose: Clones Xfce repositories pulled from
           https://gitlab.xfce.org/

source: https://gitlab.com/kevinbowen/xfce-repocapp
version: 0.8.4
updated: 20220101
@author: kevin.bowen@gmail.com
"""

import os
import subprocess
import sys

menus = {'clone': ['apps', 'bindings', 'xfce', 'panel-plugins',
                   'thunar-plugins', 'www', 'all'],
         'build': ['apps', 'bindings', 'xfce', 'panel-plugins',
                   'thunar-plugins', 'all'],
         'install': ['apps', 'bindings', 'xfce', 'panel-plugins',
                     'thunar-plugins', 'all'],
         'clean':  ['apps', 'bindings', 'xfce', 'panel-plugins',
                    'thunar-plugins', 'all'],
         'pull':  ['apps', 'bindings', 'xfce', 'panel-plugins',
                   'thunar-plugins', 'www', 'all'],
         'purge': ['apps', 'bindings', 'xfce', 'panel-plugins',
                   'thunar-plugins', 'www', 'all'],
         'quit': 'quit',
         }

currentdir = os.path.dirname(os.path.realpath(__file__))
os.chdir(currentdir)


def main_menu():
    """ Display selection of available actions to take with repositories. """
    os.system('clear')
    main_banner = "\u2248: xfce-repocapp: local " \
                  "Xfce repository maintenance :\u2248"
    border = '\u2248' * len(main_banner)
    print(f"{border}\n{main_banner}\n{border}")
    main_list = list(menus.keys())
    selection = range(1, len(main_list) + 1)
    for select, m_list in zip(selection, main_list):
        print(f"{select}. {m_list.title()}")
    print(f"{border}")
    question = f"Please enter your choice[1-{len(menus)}]: "
    try:
        choice = int(input(question))
        if choice not in selection:
            # print("Enter the correct value, please.")
            # try:
            #    choice = int(input(question))
            # except ValueError:
            print("Invalid input. Try again.")
            main_menu()
        else:
            if choice == selection[-1]:
                print("Goodbye!")
                sys.exit()
            else:
                action = main_list[choice - 1]
                sub_menus(action)
    except (ValueError, EOFError):
        print("Invalid input. Try again.")
        main_menu()


def sub_menus(action):
    """ Display actions to take upon a specific repository. """
    os.system('clear')
    banner = f"\u2248: xfce-repocapp: {action} " \
             f"local Xfce repositories :\u2248"
    border = '\u2248' * len(banner)
    print(f"{border}\n{banner}\n{border}")
    selection = list(range(1, len(menus[action]) + 1))
    for select, component in zip(selection, menus[action]):
        print(f"{select}. {action.title()} {component}")
    selection.append(selection[-1] + 1)
    selection.append(selection[-1] + 1)
    print(f"{selection[-2]}. Return to Main Menu")
    print(f"{selection[-1]}. Quit")
    print(f"{border}")
    question = f"Please enter your choice[1-{len(selection)}]: "
    try:
        answer = int(input(question))
        if answer not in selection:
            # print("Enter the correct value, please.")
            # try:
            #     answer = int(input(question))
            # except ValueError:
            print("Invalid input. Try again.")
            sub_menus(action)
        else:
            if answer == selection[-1]:
                print("Goodbye!")
                sys.exit()
            elif answer == selection[-2]:
                main_menu()
            else:
                component_list = list(menus[action])
                component = component_list[answer - 1]
                script = action + '_xfce.py'
                command = f"{currentdir}/{script} -c {component}"
                subprocess.run([command], shell=True)
                input("Press Enter to continue...")
                main_menu()
    except (ValueError, EOFError):
        print("Invalid input. Try again.")
        sub_menus(action)


if __name__ == '__main__':
    try:
        main_menu()
    except KeyboardInterrupt:
        print()
        print('Stopped xfce-repocapp. Exiting...')
        sys.exit()
