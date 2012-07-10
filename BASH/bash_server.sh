#!/bin/bash
mkfifo msg_stream

while true; do {
	echo "Server: GO" > msg_stream
	read < msg_stream
	echo "Received: $REPLY"
done

rm msg_stream
