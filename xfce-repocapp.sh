#!/bin/bash

# {{{ ------------------------------------------------------------------ #
#
# Name: xfce-repocapp.sh
#
# Purpose: Provide a basic menu-driven system that will run scripts from
#           https://gitlab.com/kevinbowen/xfce-repocapp.git
#          These scripts, in turn, manage git repositories pulled from
#           https://gitlab.xfce.org
#
# source: https://gitlab.com/kevinbowen/xfce-repocapp
# version: 0.8.3
# updated: 20211228
# @author: kevin.bowen@gmail.com
#
# }}} ------------------------------------------------------------------ #
clear

echo "#####################################################"
echo "# xfce-repocapp: local Xfce repository maintenance  #"
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
                        clone_xfce.py -c apps
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone bindings")
                        clone_xfce.py -c bindings
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone core")
                        clone_xfce.py -c xfce
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone panel-plugins")
                        clone_xfce.py -c panel-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone thunar-plugins")
                        clone_xfce.py -c thunar-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone www")
                        clone_xfce.py -c www
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clone all repos")
                        printf "Cloning all Xfce repositories...\n"
                        clone_xfce.py -c all
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
                        build_xfce.py -c apps
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build bindings")
                        build_xfce.py -c bindings
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build core")
                        build_xfce.py -c xfce
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build panel-plugins")
                        build_xfce.py -c panel-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build thunar-plugins")
                        build_xfce.py -c thunar-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Build all repos")
                        printf "Building all Xfce repositories...\n"
                        build_xfce.py -c all
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
                        install_xfce.py -c apps
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install bindings")
                        install_xfce.py -c bindings
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install core")
                        install_xfce.py -c xfce
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install panel-plugins")
                        install_xfce.py -c panel-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install thunar-plugins")
                        install_xfce.py -c thunar-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Install all repos")
                        printf "Installing all Xfce repositories...\n"
                        install_xfce.py -c all
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
                        clean_xfce.py -c apps
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean bindings")
                        clean_xfce.py -c bindings
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean core")
                        clean_xfce.py -c xfce
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean panel-plugins")
                        clean_xfce.py -c panel-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean thunar-plugins")
                        clean_xfce.py -c thunar-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Clean all repos")
                        printf "Cleaning all Xfce repositories...\n"
                        clean_xfce.py -c all
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
                        pull_xfce.py -c apps
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull bindings")
                        pull_xfce.py -c bindings
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull core")
                        pull_xfce.py -c xfce
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull panel-plugins")
                        pull_xfce.py -c panel-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull thunar-plugins")
                        pull_xfce.py -c thunar-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull www")
                        pull_xfce.py -c www
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Pull all repos")
                        printf "Pulling all Xfce repositories...\n"
                        pull_xfce.py -c all
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
                        purge_xfce.py -c apps
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge bindings")
                        purge_xfce.py -c bindings
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge core")
                        purge_xfce.py -c xfce
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge panel-plugins")
                        purge_xfce.py -c panel-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge thunar-plugins")
                        purge_xfce.py -c thunar-plugins
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge www")
                        purge_xfce.py -c www
                        read -p "Press any key to continue... " -r -n1 -s
                        exec "$0"
                        ;;
                    "Purge all repos")
                        printf "Purging all Xfce repositories...\n"
                        purge_xfce.py -c all
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
