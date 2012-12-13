#!/usr/bin/python
#tests = [NOT, OR, AND, 'NOT OR', 'NOT AND', '!=', '=']
evulate = [False, True]
print "Testing: NOT"
for i in evulate:
	value = evulate[i]
	if ( value != True ):
		print "not %r\tTrue" % value
	else:
		print "not %r\tFalse"% value

print "\nTesting: OR"
for i in evulate:
	value = evulate[i]
	if ( value or False ):
		print "%r or False\tTrue" % value
	else:
		print "%r or False\tFalse" % value
	
	if ( value or True ):
		print "%r or True\tTrue" % value
	else:
		print "%r or True\tFalse" % value

print "\nTesting: AND"
for i in evulate:
	value = evulate[i]
	if ( value and False ):
		print "%r and False\tTrue" % value
	else:
		print "%r and False\tFalse" % value
	
	if ( value and True ):
		print "%r and True\tTrue" % value
	else:
		print "%r and True\tFalse" % value

print "\nTesting: NOT OR"
for i in evulate:
	value = evulate[i]
	if not ( value or False ):
		print "not %d or False\tTrue" % value
	else:
		print "not %d or False\tFalse" % value
	
	if not ( value or True ):
		print "not %d or True\tTrue" % value
	else:
		print "not %d or True\tFalse" % value

print "\nTesting: NOT AND"
for i in evulate:
	value = evulate[i]
	if ( not (value and False) ):
		print "not %r and False\tTrue" % value
	else:
		print "not %r and False\tFalse" % value
	
	if ( not (value and True) ):
		print "not %r and True\tTrue" % value
	else:
		print "not %r and True\tFalse" % value

evulate = [1, 0]

print "\nTesting: !="
for i in evulate:
	value = evulate[i]
	if ( value != 0 ):
		print "%d != 0\tTrue" % value
	else:
		print "%d != 0\tFalse" % value
	
	if ( value != 1 ):
		print "%d != 1\tTrue" % value
	else:
		print "%d != 1\tFale" % value

print "\nTesting: =="
for i in evulate:
	value = evulate[i]
	if ( value == 0 ):
		print "%d == 0\tTrue" % value
	else:
		print "%d == 0\tFalse" % value
	
	if ( value == 1 ):
		print "%d == 1\tTrue" % value
	else:
		print "%d == 1\tFale" % value
