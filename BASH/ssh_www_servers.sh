#!/bin/bash

# The 0 padding will only work in BASH 4 or greater
for i in {000..100}; do
	if [[ $(( $i % 5 )) -ne 0 ]]; then 
		echo "ssh user@www${i} command &"
		echo "ssh user@www$(($i+1)) command &"
		echo "ssh user@www$(($i+2)) command &"
		echo "ssh user@www$(($i+3)) command &"
		echo "ssh user@www$(($i+4)) command &"
	fi
done
