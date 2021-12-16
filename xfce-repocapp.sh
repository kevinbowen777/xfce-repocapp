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
# version: 0.7
# updated: 20210217
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #
clear

# while true
# do
# clear

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
            echo "you chose choice 1"
            PS3=$sub1prompt
            select sub1opt in "${sub1[@]}"
            do
                case $sub1opt in
                    "Clone apps")
                        echo
                        echo "Cloning apps repositories..."
                        clone/clone_apps.py
                        exit
                        ;;
                    "Clone bindings")
                        echo
                        echo "Cloning bindings repositories..."
                        clone/clone_bindings.py
                        exit
                        ;;
                    "Clone core")
                        echo
                        echo "Cloning core repositories..."
                        clone/clone_core.py
                        exit
                        ;;
                    "Clone panel-plugins")
                        echo
                        echo "Cloning panel-plugin repositories..."
                        clone/clone_panel_plugins.py
                        exit
                        ;;
                    "Clone thunar-plugins")
                        echo
                        echo "Cloning thunar-plugin repositories..."
                        clone/clone_thunar_plugins.py
                        exit
                        ;;
                    "Clone www")
                        echo
                        echo "Cloning www repositories..."
                        clone/clone_www.py
                        exit
                        ;;
                    "Clone all repos")
                        echo
                        echo "Cloning all Xfce repositories..."
                        clone/clone_all.py
                        exit
                        ;;
                    "Back to Main Menu")
                        echo
                        echo "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        echo "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Build")
            echo "you chose choice 2"
            PS3=$sub2prompt
            select sub2opt in "${sub2[@]}"
            do
                case $sub2opt in
                    "Build apps")
                        echo
                        echo "Building apps repositories..."
                        build/build_apps.py
                        exit
                        ;;
                    "Build bindings")
                        echo
                        echo "Building bindings repositories..."
                        build/build_bindings.py
                        exit
                        ;;
                    "Build core")
                        echo
                        echo "Building core repositories..."
                        build/build_core.py
                        exit
                        ;;
                    "Build panel-plugins")
                        echo
                        echo "Building panel-plugin repositories..."
                        build/build_panel_plugins.py
                        exit
                        ;;
                    "Build thunar-plugins")
                        echo
                        echo "Building thunar-plugin repositories..."
                        build/build_thunar_plugins.py
                        exit
                        ;;
                    "Build all repos")
                        echo
                        echo "Building all Xfce repositories..."
                        build/build_all.py
                        exit
                        ;;
                    "Back to Main Menu")
                        echo
                        echo "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        echo "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Install")
            echo "you chose choice 3"
            PS3=$sub3prompt
            select sub3opt in "${sub3[@]}"
            do
                case $sub3opt in
                    "Install apps")
                        echo
                        echo "Installing apps repositories..."
                        install/install_apps.py
                        exit
                        ;;
                    "Install bindings")
                        echo
                        echo "Installing bindings repositories..."
                        install/install_bindings.py
                        exit
                        ;;
                    "Install core")
                        echo
                        echo "Installing core repositories..."
                        install/install_core.py
                        exit
                        ;;
                    "Install panel-plugins")
                        echo
                        echo "Installing panel-plugin repositories..."
                        install/install_panel_plugins.py
                        exit
                        ;;
                    "Install thunar-plugins")
                        echo
                        echo "Installing thunar-plugin repositories..."
                        install/install_thunar_plugins.py
                        exit
                        ;;
                    "Install all repos")
                        echo
                        echo "Installing all Xfce repositories..."
                        install/install_all.py
                        exit
                        ;;
                    "Back to Main Menu")
                        echo
                        echo "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        echo "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Clean")
            echo "you chose choice 4"
            PS3=$sub4prompt
            select sub4opt in "${sub4[@]}"
            do
                case $sub4opt in
                    "Clean apps")
                        echo
                        echo "Cleaning apps repositories..."
                        clean/clean_apps.py
                        exit
                        ;;
                    "Clean bindings")
                        echo
                        echo "Cleaning bindings repositories..."
                        clean/clean_bindings.py
                        exit
                        ;;
                    "Clean core")
                        echo
                        echo "Cleaning core repositories..."
                        clean/clean_core.py
                        exit
                        ;;
                    "Clean panel-plugins")
                        echo
                        echo "Cleaning panel-plugin repositories..."
                        clean/clean_panel_plugins.py
                        exit
                        ;;
                    "Clean thunar-plugins")
                        echo
                        echo "Cleaning thunar-plugin repositories..."
                        clean/clean_thunar_plugins.py
                        exit
                        ;;
                    "Clean all repos")
                        echo
                        echo "Cleaning all Xfce repositories..."
                        clean/clean_all.py
                        exit
                        ;;
                    "Back to Main Menu")
                        echo
                        echo "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        echo "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Pull")
            echo "you chose choice 5"
            PS3=$sub5prompt
            select sub5opt in "${sub5[@]}"
            do
                case $sub5opt in
                    "Pull apps")
                        printf "Pulling apps repositories...\n"
                        pull/pull_apps.py
                        exit
                        ;;
                    "Pull bindings")
                        printf "Pulling bindings repositories...\n"
                        pull/pull_bindings.py
                        exit
                        ;;
                    "Pull core")
                        printf "Pulling core repositories...\n"
                        pull/pull_core.py
                        exit
                        ;;
                    "Pull panel-plugins")
                        printf "Pulling panel-plugin repositories...\n"
                        pull/pull_panel_plugins.py
                        exit
                        ;;
                    "Pull thunar-plugins")
                        printf "Pulling thunar-plugin repositories...\n"
                        pull/pull_thunar_plugins.py
                        exit
                        ;;
                    "Pull www")
                        printf "Pulling www repositories...\n"
                        pull/pull_www.py
                        exit
                        ;;
                    "Pull all repos")
                        printf "Pulling all Xfce repositories...\n"
                        pull/pull_all.py
                        exit
                        ;;
                    "Back to Main Menu")
                        echo "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        echo "Goodbye..."
                        exit
                        ;;
                    *) echo invalid option;;
                 esac
            done
            ;;
        "Purge")
            echo "you chose choice 6"
            PS3=$sub6prompt
            select sub6opt in "${sub6[@]}"
            do
                case $sub6opt in
                    "Purge apps")
                        echo
                        echo "Purging apps repositories..."
                        purge/purge_apps.py
                        exit
                        ;;
                    "Purge bindings")
                        echo
                        echo "Purging bindings repositories..."
                        purge/purge_bindings.py
                        exit
                        ;;
                    "Purge core")
                        echo
                        echo "Purging core repositories..."
                        purge/purge_core.py
                        exit
                        ;;
                    "Purge panel-plugins")
                        echo
                        echo "Purging panel-plugin repositories..."
                        purge/purge_panel_plugins.py
                        exit
                        ;;
                    "Purge thunar-plugins")
                        echo
                        echo "Purging thunar-plugin repositories..."
                        purge/purge_thunar_plugins.py
                        exit
                        ;;
                    "Purge www")
                        echo
                        echo "Purging www repositories..."
                        purge/purge_www.py
                        exit
                        ;;
                    "Purge all repos")
                        echo
                        echo "Purging all Xfce repositories..."
                        purge/purge_all.py
                        exit
                        ;;
                    "Back to Main Menu")
                        echo
                        echo "Returning to Main Menu..."
                        exec "$0"
                        ;;
                    "Quit")
                        echo "Goodbye..."
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
