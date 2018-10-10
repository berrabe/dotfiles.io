#!/bin/bash

#count=0
while true
	do
		# temp0=$(sensors | grep -i 'core' | head -n1 | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/')
		# temp1=$(sensors | grep -i 'core 1' | head -n1 | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/')
		# temp3=$(sensors | grep -i 'core 2' | head -n1 | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/')
		# temp4=$(sensors | grep -i 'core 3' | head -n1 | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1

		temp=$(sensors | egrep "Core [0-3]" | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/' | tr '\n' ' ')

		# echo "$temp0 $temp1 $temp3 $temp4"
		echo "$temp"
		sleep $1
		#echo " [ $count ]	$temp0 == $temp1"
		#count=$(printf "%0${digits}d\n" "$((10#$count + 1))")
	done

