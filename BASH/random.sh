#!/bin/bash

INCORRECT_VARIABLE_AMOUNT=58

function usage {
	cat <<here
	Must specify home many random numbers you want to see
	ex: $(basename $0) 4
	$ 1988.2365 
	$ 13798.14178 
	$ 10081.134
	$ 3816.15098
here

exit $INCORRECT_VARIABLE_AMOUNT
}

[[ $# -ne 1 ]] && usage
count=0
while [[ $count -lt $1 ]]; do
	printf "%5d.%-5d\n" $RANDOM $RANDOM
	count=$(($count+1))
done
