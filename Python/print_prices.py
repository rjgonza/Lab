#!/usr/bin/python
import sys

width = input("Please enter width: ")
price_width = 10
inventory = { 'Apples' : 0.4 , 
              'Pears' : 0.5 ,
              'Cantaloupes' : 1.92,
              'Dried Apricots (16 oz.)' : 8,
              'Prunes (4 lbs.)' : 12
            }

for item in inventory:
	if width < len(item) + price_width:
		print "Please enter a larger size"
		sys.exit()

item_width = width - price_width
header_format = '%-*s%*s'
format = '%-*s%*.2f'

print '=' * width
print header_format % (item_width, 'Item', price_width, 'Price')
print '-' * width
for item in inventory:
	print format % (item_width, item, price_width, inventory[item])
print '=' * width
