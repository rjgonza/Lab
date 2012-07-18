#!/bin/bash

show_help () {
	cat <<here
	Usage: $0
	$0 [-h | -?] : help information (this message)
	$0 [-v] : send the verbose flag
	$0 [-f] : specify an output file
here
}

output_file=""
verbose=0

while getopts "h?vf:" opt; do
	case "$opt" in
		h|\?)	show_help
			exit 0
			;;
		v)	verbose=1
			;;
		f)	output_file=$OPTARG
	esac
done

shift $((OPTIND-1))

[[ "$1" = "--" ]] && shift

echo "verbose=$verbose, output_file='$output_file', Leftovers: $@"
