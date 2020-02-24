#!/bin/sh
#this shellscript is just a wrapper to subphctool.sh
#but necessary to run phctool with sudo even from the tray icon
PROGPATH=`dirname "$0"`
cd $PROGPATH
if test -e /usr/bin/gksu
  then gksu  ./subphctool.sh $1
  else sudo ./subphctool.sh $1
fi

