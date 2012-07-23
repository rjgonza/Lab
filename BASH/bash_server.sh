#!/bin/bash

if [[ -e msg_stream ]]; then 
	read -r -p "The message stream file already exists, use it? (y/n): "
	if [[ $REPLY =~ 'y'|'Y' ]]; then
		if [[ ! -p msg_stream ]]; then
			echo "This file is not a FIFO!"
			exit 1
		fi
	elif [[	$REPLY =~ 'n'|'N' ]]; then
		echo "User does not want to use the existing FIFO"
		exit 1
	fi
else
	mkfifo msg_stream
fi

while true; do 
	echo "Sending a GO event to the stream"
	echo "Server: GO" > msg_stream
	read < msg_stream
	echo "Received: $REPLY"
	if [[ $REPLY =~ 'TERM' ]]; then
		echo "Received: TERM event on the stream, shuttdown server"
		echo "Server: SHUTTING DOWN NOW" > msg_stream
		rm msg_stream
		exit 0
	fi
done
