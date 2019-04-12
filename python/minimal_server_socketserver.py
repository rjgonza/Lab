#!/usr/bin/python

from SocketServer import TCPServer, StreamRequestHandler

class Handler(streamRequestHandler):

	def handle(self):
		addr = self.request.getpeername()
		print 'Got connection from', addr
		self.wfile.write('Thank you for connection')

server = TCPServer(('', 1234), Handler)
server.serve_forever()
