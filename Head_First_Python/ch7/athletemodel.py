import pickle
from athletelist import AthleteList

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
		return AthleteList(parsed_data.pop(0), parsed_data.pop(0), parsed_data)
	except IOError as ioerr:
		print('File error: ' + str(ioerr))
		return(None)

def put_to_store(files_list):
	all_athletes = {}
	for file in files_list:
		ath = get_coach_data(file)
		all_athletes[ath.name] = ath
	try:
		with open('athletes.pickle', 'wb') as athf:
			pickle.dump(all_athletes, athf)
	except IOError as ioerr:
		print('File error (put_and_store):' + str(ioerr))
	return(all_athletes)

def get_from_store():
	all_athletes = {}
	try:
		with open('athletes.pickle', 'rb') as athf:
			all_athletes = pickle.load(athf)
	except IOError as ioerr:
		print('File error (get_from_store):' + str(ioerr))
	return(all_athletes)
	
def get_names_from_store():
	athlets = get_from_store()
	response = [athletes[each_ath].name for each_ath in athletes]
	return(response)
