#!/usr/bin/python3
import nester

man=[]
other=[]
try:
	data=open('sketch.txt')
	for each_line in data:
		try:	
			(role, line_spoken) = each_line.split(':', 1)
			line_spoken=line_spoken.strip()
			if role == 'Man':
				man.append(line_spoken)
			elif role == 'Other Man':
				other.append(line_spoken)
			#print(role, end='')
			#print(' said: ', end='')
			#print(line_spoken, end='')
		except ValueError:
			pass
	data.close()
except IOError:
	print('The data file is missing!')

try:
	with open('man_data.txt', 'w') as man_file, open('other_data.txt', 'w') as other_file:
		nester.print_lol(man, fh=man_file)
		nester.print_lol(other, fh=other_file)
except IOError as err:
	print('File error: ' + str(err))
