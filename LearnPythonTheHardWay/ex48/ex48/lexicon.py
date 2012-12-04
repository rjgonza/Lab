#!/usr/bin/python

mappings = {
	'north' : 'direction',
	'south' : 'direction',
	'east' : 'direction',
	'go' : 'verb',
	'kill' : 'verb',
	'eat' : 'verb',
	'the' : 'stop',
	'in' : 'stop',
	'of' : 'stop',
	'bear' : 'noun',
	'princess' : 'noun'
}

def scan(x):
	pieces = x.split(' ')
	ret_val = []
	for piece in pieces:
		if piece in mappings:
			ret_val.append((mappings[piece], piece))
		else:
			try:
				parsed = int(piece)
				ret_val.append(('number', parsed))
			except ValueError:
				ret_val.append(('error', piece))
	return ret_val
