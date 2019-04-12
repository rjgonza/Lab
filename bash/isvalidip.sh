#!/bin/bash
isvalidip() #@ USAGE: isvalidip DOTTED-QUAD
{
	case $1 in
		#reject the following:
		#empty string
		#anything other than digits and dots anything not ending in a digit
		"" | *[!0-9.]* | *[!0-9]) return 1 ;;
	esac
	
	## Change IFS to a dot, but only in this function
	#local IFS=.
	
	## Place the IP address into the positional parameters; ## after word splitting each element becomes a parameter 
	#set -- $1
	echo ${1//./ }
	
	[ $# -eq 4 ] && ## must be four parameters
			## each must be less than 256
	## A default of 666 (which is invalid) is used if a parameter is empty ## All four parameters must pass the test
	[ ${1:-666} -le 255 ] && [ ${2:-666} -le 255 ] &&
	[ ${3:-666} -le 255 ] && [ ${4:-666} -le 255 ]
}
