#!/usr/bin/python
def flatten(nested):
	try:
		#Don't iterate over string-like objects:
		try: nested + ''
		except TypeError: pass
		else: raise TypeError
		for sublist in nested:
			for element in flatten(sublist):
				yield element
	except TypeError:
		yield nested
