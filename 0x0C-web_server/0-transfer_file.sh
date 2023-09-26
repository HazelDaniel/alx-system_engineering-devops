#!/usr/bin/env bash
# a script that transfers a file from our client to a server

if [ $# -lt 3 ];
then
	echo "Usage: 0-transfer_file PATH_TO_FILE IP USERNAME PATH_TO_SSH_KEY";
	exit;
fi;

if [ $# == 4 ];
then
	scp -o StrictHostKeyChecking=no -i "$4" "$1" "$3"@"$2":~/
else
	scp -o StrictHostKeyChecking=no "$1" "$3"@"$2":~/
fi;
