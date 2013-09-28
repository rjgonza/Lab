#!/usr/bin/python
import sys

def process(string):
	print 'Processing: ', string

try:
	filename = sys.argv[1]
	f = open(filename, 'rw')
except IndexError:
	print "!! ERROR: Must include the file name as te first argument !!"
	sys.exit(1)

for line in f:
	process(line)
f.close()
