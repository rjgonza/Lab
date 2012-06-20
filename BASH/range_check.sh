#!/bin/bash
read -p "Enter a number between ${1:-10} and ${2:-20}: " input
if [[ $input -gt ${1:-10} && $input -lt ${2:-20} ]]; then
	echo "Success! You entered $input"
else
	echo "You did not enter a value between ${1:-10} and ${2:-20}"
	echo "You entered: $input"
	exit 1
fi
