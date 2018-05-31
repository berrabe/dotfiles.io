#!/bin/bash

#count=0
while true
	do
		temp0=$(sensors | grep -i 'core 0' | head -n1 | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/')
		temp1=$(sensors | grep -i 'core 1' | head -n1 | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/')

		echo "$temp0 $temp1"
		sleep $1
		#echo " [ $count ]	$temp0 == $temp1"
		#count=$(printf "%0${digits}d\n" "$((10#$count + 1))")
	done

