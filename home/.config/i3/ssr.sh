#!/bin/bash

_DMENU_FONT_="JetBrainsMono Nerd Font:style=Regular:size=7"
_LOG_FILE_="$HOME/.ssr-wrapper.log"

function check(){
    rc=$?
    msg=$1

    if [[ $rc -eq 0 ]]; then
        notify-send -u low "SUCCESS : $(echo $msg [ $rc ])"
        logger "SUCCESS : $msg [ $rc ]"
    else
        notify-send -u critical "ERROR : $(echo $msg [ $rc ])"
        logger "ERROR   : $msg [ $rc ]"
        exit 1
    fi
}

logger () {
    date_=$(date "+%d-%b-%Y")
    time_=$(date "+%H:%M:%S")

    echo -e "[ SSR ] [ $date_ ] [ $time_ ] >> $1" >> $_LOG_FILE_
}

function main() {
    dmenu=$(echo -ne " Start (Entire Screen)\n麗 Start (Selection)\n懶 Pause / Resume\n Save\n Cancel / Exit" | \
    dmenu -p "Screen Recording : " -l 6 \
    -fn "$_DMENU_FONT_" \
    -nb "#2F343F" \
    -nf "#CACACA" \
    -sb "#2F343F" \
    -sf "#B9C244" \
    )

    if [[ $dmenu == " Start (Entire Screen)" ]]; then
        /usr/bin/ssrt
        check " Start (Entire Screen)"

    elif [[ $dmenu == "麗 Start (Selection)" ]]; then
        /usr/bin/ssrt -s
        check "Start Recording (Selection)"

    elif [[ $dmenu == "懶 Pause / Resume" ]]; then
        ls=$(tail -n 1 /tmp/ssrt/in); logger "Pause / Resume Status : $ls"
        if [[ $ls == "record-pause" ]]; then
            echo record-start > /tmp/ssrt/in
            check "Resume Recording"
            exit 0
        fi

        /usr/bin/ssrt -p
        check "Pause Recording"

    elif [[ $dmenu == " Save" ]]; then
        echo record-save > /tmp/ssrt/in
        check "Save Recording"

    elif [[ $dmenu == " Cancel / Exit" ]]; then
        echo quit > /tmp/ssrt/in
        check "Cancel / Exit Recording"

    else
        notify-send -u critical "ERROR | Item Not Found"
        logger "ERROR   : Item Not Found [ $dmenu ]"
        exit 1
    fi
}

main
exit 0