#!/usr/bin/python
def func(x):
	return x.isalnum()

seq = ["foo", "x41", "?!", "****"]
print
print "Starting list: %r" % seq
print
print "Filtered: %r" % filter(func, seq)
print
print "Using list comprehension: %r" % [ x for x in seq if x.isalnum() ]
print
print "Using lambda expression: %r" % filter(lambda x: x.isalnum(), seq)
print
