def bubblesort(array):
	n = len(array) - 1
	while True:
		# Flag to determine if any values are swapped in
		# this pass.
		swapped = False
		
		# Start swapping.
		for i in range(0, n):
			if array[i] > array[i+1]:
				array[i], array[i+1] = array[i+1], array[i]
				swapped = True
		
		# After each pass index 'n + 1' will have the correct
		# value so we do not need to consider it again.
		n -= 1
		
		# If no values were swapped we are done.
		# Terminate early.
		if swapped == False:
			break