#!/bin/bash

read -p "Please enter the name of a file: " file

until [[ -e $file ]]; do
	read -p "$file dose not exist, please try again: " file
done

echo "Finally, you got one, $file exists!"
