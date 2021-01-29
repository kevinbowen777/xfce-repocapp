#!/bin/bash

#{{{ ======================================================================= #
# Author: Kevin Bowen <kevin.bowen@gmail.com>
# Script Name: basic_bash_header.template
# Description:
#		  Create executable files with templates
#
#			This script creates a skeleton file for bash scripts
#
# Source : http://www.github.com/kevinbowen777/dotfiles.git
# Last modified: 20191003
# Dependencies:
#	None
#     
#}}} ======================================================================= #

PS3='Do you want to clone, build, purge, or update Xfce sources?'
menu=("Clone" "Build" "Purge" "Update" "Quit")
select options in "${menu[@]}"; do
    case $options in
        "Clone")
            echo "We are cloning the Xfce sources"
	    # optionally call a function or run some code here
            ;;
        "Build")
            echo "We are building some Xfce shit."
	    # optionally call a function or run some code here
            ;;
        "Purge")
            echo "We are purging some Xfce shit."
	    # optionally call a function or run some code here
            ;;
        "Update")
            echo "We are updating some Xfce shit."
	    # optionally call a function or run some code here
	    break
            ;;
	    "Quit")
	    echo "User requested exit"
	    exit
	    ;;
        *) echo "invalid option $REPLY";;
    esac

done
