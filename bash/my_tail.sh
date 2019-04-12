#!/bin/bash
show_help() {
	cat <<here
	echo "Pass a file"
here
exit 1
}

count=10

while getopts "?hl:" opt; do
	case "$opt" in
		h|\?)   show_help
			;;
		l)	count=$OPTARG
	esac
done
file=$(eval echo '$'"$#")
[[ -e $file ]] || show_help
end_of_file=$(wc -l $file | awk '{print $1}')

[[ $end_of_file -lt 10 ]] && start=1 || start=$(($end_of_file-$count))
counter=1
while IFS= read -r line; do 
	[[ $counter -gt $start ]] && printf "%s\n" "$line"
	((counter++))
done < $file
