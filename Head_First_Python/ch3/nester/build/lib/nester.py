"""This is the "nester.py" module, and it provides one function called print_lol() which prints lists that may or may not include nested lists."""

import sys

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
	"""This function takes a positional argument called "the_list", which is any Python list (of, posibly, nested lists). Each data item in the prvided list is (recursively) printed ot the screen on its own line."""
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item, indent, level+1, fh)
		else:	
			if indent:
				for tab_stop in range(level):
					print("\t", end='', file=fh)
			print (each_item, file=fh)
