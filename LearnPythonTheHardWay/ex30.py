people = 30
cars = 40
buses = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
<<<<<<< HEAD
	print "We should not take the cars."
=======
	print "We should not tka ethe cars."
>>>>>>> 90633362cf19e3f07eacd96a41dbdd737ef9a7d2
else:
	print "We can't decide."

if buses > cars:
<<<<<<< HEAD
	print "That's too many buses."
=======
	print "Thats too many buses."
>>>>>>> 90633362cf19e3f07eacd96a41dbdd737ef9a7d2
elif buses < cars:
	print "Maybe we could take the buses."
else:
	print "We still can't decide."

if people > buses:
	print "Alright, let's just take the buses."
else:
	print "Fine, let's stay home then."
