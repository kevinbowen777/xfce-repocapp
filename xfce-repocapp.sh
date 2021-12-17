#!/bin/bash

# {{{ ------------------------------------------------------------------ #
#
# Name: xfce-repocapp.sh
#
# Purpose: Provide a basic menu-driven system that will run scripts from
#           https://gitlab.com/kevinbowen/xfce-repocapp.git
#
#          These scripts, in turn, manage git repositories pulled from
#           https://gitlab.xfce.org
#
# version: 0.7.1
# updated: 20211216
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #
clear

echo "#####################################################"
echo "# xfce-repocapp: local Xfce repository maintenance #"
echo "#####################################################"
echo



options=("Clone" "Build" "Install" "Clean" "Pull" "Purge" "Quit")
optionsprompt='Please enter your choice: '

sub1=("Clone apps" "Clone bindings" "Clone core" "Clone panel-plugins"
      "Clone thunar-plugins" "Clone www" "Clone all repos"
      "Back to Main Menu" "Quit")
sub1prompt='Please enter your choice: '

sub2=("Build apps" "Build bindings" "Build core" "Build panel-plugins"
      "Build thunar-plugins" "Build all repos" "Back to Main Menu" "Quit")
sub2prompt='Please enter your choice: '

sub3=("Install apps" "Install bindings" "Install core" "Install panel-plugins"
      "Install thunar-plugins" "Install all repos" "Back to Main Menu"
      "Quit" )
sub3prompt='Please enter your choice: '

sub4=("Clean apps" "Clean bindings" "Clean core" "Clean panel-plugins"
      "Clean thunar-plugins" "Clean all repos" "Back to Main Menu" "Quit" )
sub4prompt='Please enter your choice: '

sub5=("Pull apps" "Pull bindings" "Pull core" "Pull panel-plugins"
      "Pull thunar-plugins" "Pull www" "Pull all repos" "Back to Main Menu"
      "Quit" )
sub5prompt='Please enter your choice: '

sub6=("Purge apps" "Purge bindings" "Purge core" "Purge panel-plugins"
      "Purge thunar-plugins" "Purge www" "Purge all repos"
      "Back to Main Menu" "Quit" )
sub6prompt='Please enter your choice: '

PS3=$optionsprompt
select opt in "${options[@]}"
do
    case $opt in
        "Clone")
            PS3=$sub1prompt
            select sub1opt in "${sub1[@]}"
            do
                case $sub1opt in
                    "Clone apps")
                        printf "Cloning apps repositories...\n"
                        clone/clone_apps.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone bindings")
                        printf "Cloning bindings repositories...\n"
                        clone/clone_bindings.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone core")
                        printf "Cloning core repositories...\n"
                        clone/clone_core.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone panel-plugins")
                        printf "Cloning panel-plugin repositories...\n"
                        clone/clone_panel_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone thunar-plugins")
                        printf "Cloning thunar-plugin repositories...\n"
                        clone/clone_thunar_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone www")
                        printf "Cloning www repositories...\n"
                        clone/clone_www.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone all repos")
                        printf "Cloning all Xfce repositories...\n"
                        clone/clone_all.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Back to Main Menu")
                        printf "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        printf "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Build")
            PS3=$sub2prompt
            select sub2opt in "${sub2[@]}"
            do
                case $sub2opt in
                    "Build apps")
                        printf "Building apps repositories..."
                        build/build_apps.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build bindings")
                        printf "Building bindings repositories..."
                        build/build_bindings.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build core")
                        printf "Building core repositories..."
                        build/build_core.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build panel-plugins")
                        printf "Building panel-plugin repositories..."
                        build/build_panel_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build thunar-plugins")
                        printf "Building thunar-plugin repositories..."
                        build/build_thunar_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build all repos")
                        printf "Building all Xfce repositories..."
                        build/build_all.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Back to Main Menu")
                        printf "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        printf "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Install")
            PS3=$sub3prompt
            select sub3opt in "${sub3[@]}"
            do
                case $sub3opt in
                    "Install apps")
                        printf "Installing apps repositories...\n"
                        install/install_apps.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install bindings")
                        printf "Installing bindings repositories...\n"
                        install/install_bindings.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install core")
                        printf "Installing core repositories...\n"
                        install/install_core.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install panel-plugins")
                        printf "Installing panel-plugin repositories...\n"
                        install/install_panel_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install thunar-plugins")
                        printf "Installing thunar-plugin repositories...\n"
                        install/install_thunar_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install all repos")
                        printf "Installing all Xfce repositories...\n"
                        install/install_all.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Back to Main Menu")
                        printf "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        printf "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Clean")
            PS3=$sub4prompt
            select sub4opt in "${sub4[@]}"
            do
                case $sub4opt in
                    "Clean apps")
                        printf "Cleaning apps repositories..."
                        clean/clean_apps.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean bindings")
                        printf "Cleaning bindings repositories..."
                        clean/clean_bindings.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean core")
                        printf "Cleaning core repositories..."
                        clean/clean_core.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean panel-plugins")
                        printf "Cleaning panel-plugin repositories..."
                        clean/clean_panel_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean thunar-plugins")
                        printf "Cleaning thunar-plugin repositories..."
                        clean/clean_thunar_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean all repos")
                        printf "Cleaning all Xfce repositories..."
                        clean/clean_all.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Back to Main Menu")
                        printf "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        printf "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Pull")
            PS3=$sub5prompt
            select sub5opt in "${sub5[@]}"
            do
                case $sub5opt in
                    "Pull apps")
                        printf "Pulling apps repositories...\n"
                        pull/pull_apps.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull bindings")
                        printf "Pulling bindings repositories...\n"
                        pull/pull_bindings.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull core")
                        printf "Pulling core repositories...\n"
                        pull/pull_core.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull panel-plugins")
                        printf "Pulling panel-plugin repositories...\n"
                        pull/pull_panel_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull thunar-plugins")
                        printf "Pulling thunar-plugin repositories...\n"
                        pull/pull_thunar_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull www")
                        printf "Pulling www repositories...\n"
                        pull/pull_www.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull all repos")
                        printf "Pulling all Xfce repositories...\n"
                        pull/pull_all.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Back to Main Menu")
                        printf "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        printf "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Purge")
            PS3=$sub6prompt
            select sub6opt in "${sub6[@]}"
            do
                case $sub6opt in
                    "Purge apps")
                        printf "Purging apps repositories...\n"
                        purge/purge_apps.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge bindings")
                        printf "Purging bindings repositories...\n"
                        purge/purge_bindings.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge core")
                        printf "Purging core repositories...\n"
                        purge/purge_core.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge panel-plugins")
                        printf "Purging panel-plugin repositories...\n"
                        purge/purge_panel_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge thunar-plugins")
                        printf "Purging thunar-plugin repositories...\n"
                        purge/purge_thunar_plugins.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge www")
                        printf "Purging www repositories...\n"
                        purge/purge_www.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge all repos")
                        printf "Purging all Xfce repositories...\n"
                        purge/purge_all.py
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Back to Main Menu")
                        printf "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        printf "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Quit")
            break
            ;;
        *) echo invalid option;;
    esac
done
# done
