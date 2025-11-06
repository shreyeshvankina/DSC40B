def mode(numbers):
	occurences = {}
	for num in numbers:
		if num in occurences:
			occurences[num] += 1
		else:
			occurences[num] = 1

	maximum = (None, 0)
	for key, value in occurences.items():
		if (value > maximum[1]):
			maximum = (key, value)
	return maximum[0]