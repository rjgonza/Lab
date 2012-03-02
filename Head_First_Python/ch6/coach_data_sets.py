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

def get_coach_data(file):
	try:
		with open(file) as my_file:
			data = my_file.readline()
		parsed_data = data.strip().split(',')
		coach_data = {'Name': parsed_data.pop(0), 'DoB': parsed_data.pop(0),
			'Times': str(sorted(set([sanitize(t) for t in parsed_data]))[0:3])}
		return coach_data
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)


james = get_coach_data('james2.txt')
julie = get_coach_data('julie2.txt')
mikey = get_coach_data('mikey2.txt')
sarah = get_coach_data('sarah2.txt')

print (james['Name'] + "'s fastest times are: " + james['Times'])
print (julie['Name'] + "'s fastest times are: " + julie['Times'])
print (mikey['Name'] + "'s fastest times are: " + mikey['Times'])
print (sarah['Name'] + "'s fastest times are: " + sarah['Times'])
