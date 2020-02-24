#!/bin/sh
#this shellscript is just a wrapper to phctool.py
#but necessary to run phctool from another directory

PROGPATH=`dirname "$0"`
cd $PROGPATH
USERHOME=`getent passwd $SUDO_USER | cut -d: -f6`
export HOME="$USERHOME"
./phctool.py $1
