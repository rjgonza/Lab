def print_range(limit):
	i = 0
	numbers = []
	while i < limit:
		print "At the topi is %d" %i
		numbers.append(i)
		i = i + 1
		print "Numbers now: ", numbers
		print "At the bottom i is %d:" % i
	print "The numbers: "

	for num in numbers:
		print num

print_range(10)
