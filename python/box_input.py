#!/usr/bin/python
import sys
sentence = raw_input("Sentence: ")

screen_width = 80
if len(sentence) > screen_width:
	print "Sorry the text you entered is too long to display"
	#raise SystemExit
	sys.exit()
text_width = len(sentence)
box_width = text_width + 6
left_margin = (screen_width - box_width)//2 # // is interger division

print
print ' ' * left_margin + '+'  + '-' * (box_width-2) +   '+'
print ' ' * left_margin + '|  '+ ' ' * text_width    + '  |'
print ' ' * left_margin + '|  '+       sentence      + '  |'
print ' ' * left_margin + '|  '+ ' ' * text_width    + '  |'
print ' ' * left_margin + '+'  + '-' * (box_width-2) +   '+'
print
