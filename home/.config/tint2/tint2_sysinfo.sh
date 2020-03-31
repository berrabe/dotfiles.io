#!/bin/bash

while true
	do

		if [[ $1 == 1 ]]
			then
				# temp=$(sensors | egrep "Core [0-7]" | sed -r 's/.*:\s+[\+-]?(.*C)\s+.*/\1/' | tr '\n' ' ')
				temp=$(sensors | awk '/^Core /{++r; gsub(/[^[:digit:]]+/, "", $3); s+=$3} END {printf("%.0f °C",s/(10*r))}')
				echo " $temp"

		
		elif [[ $1 == 2 ]]
			then
				# cpu=$(cat /proc/cpuinfo | grep -i "cpu MHz" | cut -b 12-15 | tr '\n' ' ')
				freq=$(cat /proc/cpuinfo | grep -i "cpu MHz" | cut -b 12-15 | awk '{total+=$1; count+=1} END {printf("%.0f MHz",total/count)}')
				echo "龍 $freq"

		
		elif [[ $1 == 3 ]]
			then
				memory=$(awk '/^Mem/ {print $3 " MB"}' <(free -m))
				echo " $memory"
		

		fi

	sleep $2

	done

	