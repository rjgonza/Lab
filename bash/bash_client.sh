#!/bin/bash
until [ -p msg_stream ]; do
	sleep 1
	echo "Insert bash spinner here"
done
echo "The message stream is ready!"
cat <<here
	1 ) Read a message and disconnect
	2 ) Read a message and then send a termination event to the server
here
read -r -p "Choose an operation to perform?: "
case $REPLY in
	1) 	read < msg_stream
		echo "Reading from message stream: $REPLY"
		echo "Sending a received event message to the stream"
		echo "Client: Recieved GO event" > msg_stream
		;;
	2)	read < msg_stream
		echo "Reading from message stream: $REPLY"
		echo "Sending termination event to the server"
		echo "TERM" > msg_stream
		read < msg_stream; echo "$REPLY"
		;;
esac
