#!/bin/bash

# ============================================

_LOCAL_CONF_=( "cava" "dunst" "glava" "gtk-2.0" "gtk-3.0" "i3" "lxterminal" "neofetch" "networkmanager-dmenu" 
                "mpd" "polybar" "ranger" "rofi" "terminator" "Thunar" "tint2" "viewnior"  "picom.conf" 
                "sublime-text-3/Packages/User/Preferences.sublime-settings" )
_HOME_CONF_=( ".fonts" ".Lenovo-Util" ".ncmpcpp" ".resources" ".themes" ".urxvt" ".bashrc" ".fehbg" ".gtkrc-2.0"
				".nvidia-settings-rc" ".profile" ".vimrc" ".xinitrc" ".Xresources" ".Xresources.backup" ".zshrc" "index.php")

# ============================================

Black="\033[0;30m"
Red="\033[0;31m"
Green="\033[0;32m"
Brown_Orange="\033[0;33m"
Blue="\033[0;34m"
Purple="\033[0;35m"
Cyan="\033[0;36m"
Light_Gray="\033[0;37m"
Dark_Gray="\033[1;30m"
Light_Red="\033[1;31m"
Light_Green="\033[1;32m"
Yellow="\033[1;33m"
Light_Blue="\033[1;34m"
Light_Purple="\033[1;35m"
Light_Cyan="\033[1;36m"
White="\033[1;37m"
NoColor="\033[0m"

trap ctrl_c INT

function ctrl_c() {
    echo -ne "  -- Exiting --  "
}

function check_ret_code() {
    if [[ $? -eq 0 && ${PIPESTATUS[0]} -eq 0 ]]; then
        echo -e "${Light_Green} [ Success ] ${NoColor}"
    else
        echo -e "${Light_Red} [ Failed ] ${NoColor}"
        exit 1
    fi
}

function check_dir_file() {
    _full_path_=$1
    if [[ -d "$_full_path_" || -f "$_full_path_" ]]; then
        return 0
    else
        return 1
    fi
}

function backup_conf() {
    _arr_path_=("$@")
    for arr in "${_arr_path_[@]}"; do
        _full_path_="$_BASE_PATH_$arr"
        printf "**|--[+]*Backup*%-60s" "$_full_path_*" | sed 's/ /./g' | sed 's/*/ /g'
        
        check_dir_file "$_full_path_"
        if [[ $? -eq 0 ]]; then
            cp -rf $_full_path_ $_DEST_PATH_
            check_ret_code
        else
            echo -e "${Yellow} [ Not Found ] ${NoColor}"
        fi
    done
    echo -e "${Light_Blue} [+] Backup Stored On $_DEST_PATH_  ${NoColor}"
}

function main() {
	echo -ne "\n\n\t\t${Light_Purple} Automate Backup ./Dotfiles | berrabe ${NoColor}"

	echo -e "\n"
    echo -e "${Light_Cyan} [+] Backup Local Config ${NoColor}" ; _BASE_PATH_="$HOME/.config/" ; _DEST_PATH_="./home/.config/" ; backup_conf "${_LOCAL_CONF_[@]}"

    echo -e "\n"
    echo -e "${Light_Cyan} [+] Backup Home Config ${NoColor}" ; _BASE_PATH_="$HOME/" ; _DEST_PATH_="./home/" ; backup_conf "${_HOME_CONF_[@]}"

}

clear
main