# bubble_sort

# added print for better understanding


def bubble_sort(arr):

	for i in range(len(arr)-1,0,-1):
		print 'val of I--->',i
		print 'main-array is',arr
		print '---------------'
		for x in range(i):
			print 'val of x',x
			if arr[x] > arr[x+1]:
				temp = arr[x]
				arr[x] = arr[x+1]
				arr[x+1] = temp
			print 'buubled-array is',arr
		print '===inner loop end ==\n'
	print '****outer loop end***'	


arr = [12,1,3,11,2,6]
bubble_sort(arr)
print arr