#!/bin/bash

until [ -p msg_stream ]; do
	sleep 1
	cat msg_stream
	echo "Client: Recieved GO event" > msg_stream
done
	
