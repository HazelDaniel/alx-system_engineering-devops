#!/usr/bin/env bash
#this ia a script that prints some strings at some iterations in a loop
count=0
while [[ "$count" -lt 10 ]];
do
	if [[ "$count" -eq 3 ]];
	then
		echo "bad luck"
	elif [[ "$count" -eq 7 ]];
	then
		echo "good luck"
	else
		echo "Best School"
	fi
	((count++))
done