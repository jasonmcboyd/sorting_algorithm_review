# Merge sort with optional 'inPlace' parameter (default is False).
# If 'inPlace' is true then the array is sorted in place, otherwise
# a copy of the array is sorted and returned.  This implementation is
# stable, i.e., two objects with the same value appear in the sorted 
# array in the same order as they appear in the original array.
def mergesort(array, inPlace = False):
	def _mergesort(array):
		if len(array) == 1:
			return array
		
		split = len(array) // 2
		left = _mergesort(array[:split])
		right = _mergesort(array[split:])
		
		l = 0
		r = 0
		i = 0
		while i < len(array):
			if l < len(left) and (r >= len(right) or left[l] <= right[r]): 
				array[i] = left[l]
				l += 1
			else:
				array[i] = right[r]
				r += 1
			i += 1
		
		return array
	
	if inPlace == True:
		if len(array) < 2:
			return array
		else:
			return _mergesort(array)
	else:
		if len(array) < 2:
			return array[:]
		else:
			return _mergesort(array[:])
