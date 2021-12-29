#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------ #
#
# Name: xfce-repocapp.py
# Purpose: Clones Xfce repositories pulled from
#           https://gitlab.xfce.org/
#
# source: https://gitlab.com/kevinbowen/xfce-repocapp
# version: 0.8.2
# updated: 20211226
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

import os
import subprocess

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
    os.system('clear')
    main_banner = f"# xfce-repocapp: local Xfce repository maintenance  #"
    border = "#" * len(main_banner)
    print(f"{border}\n{main_banner}\n{border}")
    main_list = list(menus.keys())
    selection = range(1, len(main_list) + 1)
    for x, y in zip(selection, main_list):
        print(f"{x}. {y.title()}")
    question = f"Please enter your choice[1-{len(menus)}]: "
    try:
        choice = int(input(question))
    except ValueError:
        print("Invalid input. Try again.")
        main_menu()
    while choice not in selection:
        print("Enter the correct value, please.")
        try:
            choice = int(input(question))
        except ValueError:
            print("Invalid input. Try again.")
            main_menu()
    else:
        if choice == selection[-1]:
            print("Goodbye!")
            exit()
        else:
            action = main_list[choice - 1]
            sub_menus(action)


def sub_menus(action):
    os.system('clear')
    banner = f"# xfce-repocapp: {action} local Xfce repositories #"
    border = "#" * len(banner)
    print(f"{border}\n{banner}\n{border}")
    selection = list(range(1, len(menus[action]) + 1))
    for x, component in zip(selection, menus[action]):
        print(f"{x}. {action.title()} {component}")
    selection.append(selection[-1] + 1)
    selection.append(selection[-1] + 1)
    print(f"{selection[-2]}. Return to Main Menu")
    print(f"{selection[-1]}. Quit")
    question = f"Please enter your choice[1-{len(selection)}]: "
    try:
        answer = int(input(question))
    except ValueError:
        print("Invalid input. Try again.")
        sub_menus(action)
    while answer not in selection:
        print("Enter the correct value, please.")
        try:
            answer = int(input(question))
        except ValueError:
            print("Invalid input. Try again.")
            sub_menus(action)
    else:
        if answer == selection[-1]:
            print("Goodbye!")
            exit()
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


if __name__ == '__main__':
    main_menu()
