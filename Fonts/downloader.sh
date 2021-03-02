#!/bin/env bash

# =============================================
# Get list font from running this command
# > curl -s https://github.com/ryanoasis/nerd-fonts/releases/tag/v2.1.0 | grep -owE '[a-zA-Z.]{1,20}zip' | uniq | nl | head -n 20

_NF_VERSION_="v2.1.0"
_MY_LOVELY_NF_TYPEFACE_=( "berrabe" "Agave" "Hack" "Iosevka" "JetBrainsMono" "SourceCodePro" "SpaceMono" )

# =============================================


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
    sleep 1
    exit 1
}

function check_ret_code() {
    if [[ $? -eq 0 && ${PIPESTATUS[0]} -eq 0 ]]; then
        echo -e "${Light_Green} [ Success ] ${NoColor}"
    else
        echo -e "${Light_Red} [ Failed ] ${NoColor}"
        # exit 1
    fi
}

function check_dir_file() {
    _file_="$1.zip"
    _dir_="$1"
    if [[ -d "$_dir_" || -f "$_file_" ]]; then
        return 0
    else
        return 1
    fi
}

function downloader() {
    for type_face in "${_MY_LOVELY_NF_TYPEFACE_[@]}"; do
        _file_name_="$type_face.zip"
        _download_url_="https://github.com/ryanoasis/nerd-fonts/releases/download/$_NF_VERSION_/$_file_name_"

        check_dir_file $type_face
        if [[ $? -ne 0 ]]; then
            wget -q $_download_url_ --show-progress --progress=bar:force
            if [[ $? -ne 0 ]]; then echo -e "${Light_Red}   ::! $type_face ${NoColor}Download Error"; fi
        else
            echo -e "${Yellow}   ::! $type_face ${NoColor}Already Exist" ;
        fi
    done
}

function unzip() {
    for type_face in "${_MY_LOVELY_NF_TYPEFACE_[@]}"; do

        check_dir_file "$type_face-$_NF_VERSION_"
        if [[ $? -eq 1 ]]; then
            _file_name_="$type_face.zip"

            printf "***::>*Unzip*%-30s" "$type_face*" | sed 's/ /./g' | sed 's/*/ /g'
            /usr/bin/unzip -qod "$type_face-$_NF_VERSION_" "$_file_name_" > /dev/null 2>&1
            check_ret_code
        else
            echo -e "${Yellow}   ::! $type_face ${NoColor}Dir Already Exist" ;
        fi
    done
}

function main() {
    echo -ne "\n\n\t\t${Light_Purple} Fonts Downloader | berrabe ${NoColor}\n"

    echo -e "\n"
    echo -e "${Light_Cyan}:: Downloading Fonts ${NoColor}" ;
    downloader

    echo -e "\n"
    echo -e "${Light_Cyan}:: Unzip Fonts ${NoColor}" ;
    unzip

}

clear
main