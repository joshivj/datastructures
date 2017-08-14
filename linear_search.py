# linear_search

def ordered_list_search(arr,ele):

	pos = 0
	found = False
	stopped = False

	while pos < len(arr) and not found and not stopped:

		if arr[pos] == ele:
			found = True
		else:
			if arr[pos] > ele:
				stopped = True
			else:
				pos += 1
	return found


o= ordered_list_search([1,2,3,4,5,6,7,8],15)
print o