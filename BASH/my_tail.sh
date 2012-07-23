#!/bin/bash

# DO TO: need to support flags

# DO TO: need to check operand
file=$1

end=$(wc -l $1 | awk '{print $1}')
length=10
[[ $end -lt 10 ]] && start=1 || start=$(($end-$length))
count=1
while IFS= read -r line; do 
	((count++))
	[[ $count -ge $start ]] && printf "%s\n" "$line"
done < $file
