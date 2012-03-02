#!/usr/bin/python3

def sanitize(time_string):
	if '-' in time_string:
		splitter = '-'
	elif ':' in time_string:
		splitter = ':'
	else:
		return(time_string)
	(mins, secs) = time_string.split(splitter)
	return (mins + '.' + secs)

def open_and_split(file):
	try:
		with open(file) as my_file:
			data = my_file.readline()
		return (data.strip().split(','))
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

james = open_and_split('james.txt')
julie = open_and_split('julie.txt')
mikey = open_and_split('julie.txt')
sarah = open_and_split('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
