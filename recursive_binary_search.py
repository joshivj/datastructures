# recursive_binary_search

def recursive_binary_search(arr,ele):

	if len(arr) == 0:
		return False

	else:
		mid = len(arr)/2

		if arr[mid] == ele:
			return True
		else:
			if ele < arr[mid]:
				return recursive_binary_search(arr[:mid], ele)
			else:
				return recursive_binary_search(arr[mid+1:], ele)

d = recursive_binary_search([1,2,3,4,5],22)
print d