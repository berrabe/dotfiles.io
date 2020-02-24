#!/bin/sh
#this shellscript is just a wrapper to phctray.py
#but necessary to run phctray from another directory

PROGPATH=`dirname "$0"`
cd $PROGPATH
./phctray.py
