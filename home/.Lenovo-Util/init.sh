#!/bin/bash

xrandr --output eDP-1 --brightness 0.6
sleep 1

sudo su -c "echo 11936 >/sys/class/backlight/intel_backlight/brightness" 
sleep 1

util 2 1000000