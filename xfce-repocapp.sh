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
# version: 0.2
# updated: 20210212
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #

options=("Clone" "Build" "Install" "Clean" "Pull" "Purge" "Quit")
optionsprompt='Please enter your choice: '

sub1=("Clone apps" "Clone bindings" "Clone core" "Clone panel-plugins" "Clone thunar-plugins" "Clone www" "Clone all repos" "Quit")
sub1prompt='Please enter your choice: '

sub2=("Build apps" "Build bindings" "Build core" "Build panel-plugins" "Build thunar-plugins" "Build all repos" "Quit")
sub2prompt='Please enter your choice: '

sub3=("Install apps" "Install bindings" "Install core" "Install panel-plugins" "Install thunar-plugins" "Install all repos" "Quit" )
sub3prompt='Please enter your choice: '

sub4=("Clean apps" "Clean bindings" "Clean core" "Clean panel-plugins" "Clean thunar-plugins" "Clean all repos" "Quit" )
sub4prompt='Please enter your choice: '

sub5=("Pull apps" "Pull bindings" "Pull core" "Pull panel-plugins" "Pull thunar-plugins" "Pull www" "Pull all repos" "Quit" )
sub5prompt='Please enter your choice: '

sub6=("Purge apps" "Purge bindings" "Purge core" "Purge panel-plugins" "Purge thunar-plugins" "Purge www" "Purge all repos" "Quit" )
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
                        echo "you chose choice 1"
                        clone/clone_xfce_apps.py
                        exit
                        ;;
                    "Clone bindings")
                        echo "you chose choice 2"
                        clone/clone_xfce_bindings.py
                        exit
                        ;;
                    "Clone core")
                        echo "you chose choice 3"
                        clone/clone_xfce_core.py
                        exit
                        ;;
                    "Clone panel-plugins")
                        echo "you chose choice 4"
                        clone/clone_xfce_panel_plugins.py
                        exit
                        ;;
                    "Clone thunar-plugins")
                        echo "you chose choice 5"
                        clone/clone_xfce_thunar_plugins.py
                        exit
                        ;;
                    "Clone www")
                        echo "you chose choice 6"
                        clone/clone_xfce_www.py
                        exit
                        ;;
                    "Clone all repos")
                        echo "you chose choice 7"
                        clone/clone_xfce_all.py
                        exit
                        ;;
                    "Quit")
                        break
                        ;;
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
                        echo "you chose choice 1"
                        build/build_xfce_apps.py
                        exit
                        ;;
                    "Build bindings")
                        echo "you chose choice 2"
                        build/build_xfce_bindings.py
                        exit
                        ;;
                    "Build core")
                        echo "you chose choice 3"
                        build/build_xfce_core.py
                        exit
                        ;;
                    "Build panel-plugins")
                        echo "you chose choice 4"
                        build/build_xfce_panel_plugins.py
                        exit
                        ;;
                    "Build thunar-plugins")
                        echo "you chose choice 5"
                        build/build_xfce_thunar_plugins.py
                        exit
                        ;;
                    "Build all repos")
                        echo "you chose choice 6"
                        build/build_xfce_all.py
                        exit
                        ;;
                    "Quit")
                        break
                        ;;
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
                        echo "you chose choice 1"
                        install/install_xfce_apps.py
                        exit
                        ;;
                    "Install bindings")
                        echo "you chose choice 2"
                        install/install_xfce_bindings.py
                        exit
                        ;;
                    "Install core")
                        echo "you chose choice 3"
                        install/install_xfce_core.py
                        exit
                        ;;
                    "Install panel-plugins")
                        echo "you chose choice 4"
                        install/install_xfce_panel_plugins.py
                        exit
                        ;;
                    "Install thunar-plugins")
                        echo "you chose choice 5"
                        install/install_xfce_thunar_plugins.py
                        exit
                        ;;
                    "Install all repos")
                        echo "you chose choice 6"
                        install/install_xfce_all.py
                        exit
                        ;;
                    "Quit")
                        break
                        ;;
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
                        echo "you chose choice 1"
                        clean/clean_xfce_apps.py
                        exit
                        ;;
                    "Clean bindings")
                        echo "you chose choice 2"
                        clean/clean_xfce_bindings.py
                        exit
                        ;;
                    "Clean core")
                        echo "you chose choice 3"
                        clean/clean_xfce_core.py
                        exit
                        ;;
                    "Clean panel-plugins")
                        echo "you chose choice 4"
                        clean/clean_xfce_panel_plugins.py
                        exit
                        ;;
                    "Clean thunar-plugins")
                        echo "you chose choice 5"
                        clean/clean_xfce_thunar_plugins.py
                        exit
                        ;;
                    "Clean all repos")
                        echo "you chose choice 6"
                        clean/clean_xfce_all.py
                        exit
                        ;;
                    "Quit")
                        break
                        ;;
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
                        echo "you chose choice 1"
                        pull/pull_xfce_apps.py
                        exit
                        ;;
                    "Pull bindings")
                        echo "you chose choice 2"
                        pull/pull_xfce_bindings.py
                        exit
                        ;;
                    "Pull core")
                        echo "you chose choice 3"
                        pull/pull_xfce_core.py
                        exit
                        ;;
                    "Pull panel-plugins")
                        echo "you chose choice 4"
                        pull/pull_xfce_panel_plugins.py
                        exit
                        ;;
                    "Pull thunar-plugins")
                        echo "you chose choice 5"
                        pull/pull_xfce_thunar_plugins.py
                        exit
                        ;;
                    "Pull www")
                        echo "you chose choice 6"
                        pull/pull_xfce_www.py
                        exit
                        ;;
                    "Pull all repos")
                        echo "you chose choice 7"
                        pull/pull_xfce_all.py
                        exit
                        ;;
                    "Quit")
                        break
                        ;;
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
                        echo "you chose choice 1"
                        purge/purge_xfce_apps.py
                        exit
                        ;;
                    "Purge bindings")
                        echo "you chose choice 2"
                        purge/purge_xfce_bindings.py
                        exit
                        ;;
                    "Purge core")
                        echo "you chose choice 3"
                        purge/purge_xfce_core.py
                        exit
                        ;;
                    "Purge panel-plugins")
                        echo "you chose choice 4"
                        purge/purge_xfce_panel_plugins.py
                        exit
                        ;;
                    "Purge thunar-plugins")
                        echo "you chose choice 5"
                        purge/purge_xfce_thunar_plugins.py
                        exit
                        ;;
                    "Purge www")
                        echo "you chose choice 6"
                        purge/purge_xfce_www.py
                        exit
                        ;;
                    "Purge all repos")
                        echo "you chose choice 7"
                        purge/purge_xfce_all.py
                        exit
                        ;;
                    "Quit")
                        break
                        ;;
                 esac
            done
            ;;
        "Quit")
            break
            ;;
        *) echo invalid option;;
    esac
done
