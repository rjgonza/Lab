#!/usr/local/bin/python3
try:
	with open('its.txt', "w" ) as data:
		print("It's...", file=data)
except IOError as err:
	print('File error: ' + str(err))
