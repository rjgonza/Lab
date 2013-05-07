#!/usr/bin/python

import socket

s = socket.socket()

host = socket.gethostname()
port = 15358

s.connect((host,port))
print s.recv(1024)
