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

def unique(time_list):
	unique_list = []
	for t in time_list:
		if t not in unique_list:
			unique_list.append(t)
	return(unique_list)

with open('james.txt') as jaf:
	data = jaf.readline()
james = data.strip().split(',')

with open('julie.txt') as juf:
	data = juf.readline()
julie = data.strip().split(',')

with open('mikey.txt') as mif:
	data = mif.readline()
mikey = data.strip().split(',')

with open('sarah.txt') as saf:
	data = saf.readline()
sarah = data.strip().split(',')

james = sorted([sanitize(t) for t in james])
julie = sorted([sanitize(t) for t in julie])
mikey = sorted([sanitize(t) for t in mikey])
sarah = sorted([sanitize(t) for t in sarah])

print(unique(james)[0:3])
print(unique(julie)[0:3])
print(unique(mikey)[0:3])
print(unique(sarah)[0:3])
