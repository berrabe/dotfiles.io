#!/bin/bash


if [[ $1 -eq 1 ]]
	then
		clear
		for x in /sys/devices/system/cpu/cpu[$2-7]*/online; do
		  echo $3 >"$x"
		done

elif [[ $1 -eq 2 ]]
	then
		clear
		for value in {0..7}
			do
				haha=$(cat /sys/devices/system/cpu/cpu$value/online)
				echo "CPU $value => $haha"
		done
fi
