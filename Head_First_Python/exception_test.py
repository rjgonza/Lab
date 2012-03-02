#!/usr/local/bin/python3
try:
	data=open('missing.txt')
	print(data.readling(), end='')
except IOError as err:
	print('File error: ' + str(err))
finally:
	if 'data' in locals():
		data.close()
