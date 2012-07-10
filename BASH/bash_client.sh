#!/bin/bash

until [ -p msg_stream ]; do
	sleep 1
done
cat msg_stream
echo "Sending a recieved event message to the stream"
echo "Client: Recieved GO event" > msg_stream	
