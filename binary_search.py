# binary_search

def binary_search(arr,ele):
	"""
		binary_search works only on sorted array, also it follows divide and conquer fundamentals
	"""

	first = 0
	last = len(arr) - 1 # as indexing starts at 0
	found = False

	while first <= last and not found:

		mid = (first+last)/2 # to get mid point of array

		if arr[mid] == ele:
			found = True
		else:
			if ele < arr[mid]:
				last = mid - 1
			else:
				first = mid + 1

	return found

b = binary_search([1,2,3,4,5],2)
print b