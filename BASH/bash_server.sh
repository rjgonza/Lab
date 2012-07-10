#!/bin/bash
mkfifo msg_stream

while true; do 
	echo "Sending a GO event to the stream"
	echo "Server: GO" > msg_stream
	read < msg_stream
	echo "Received: $REPLY"
done

rm msg_stream
