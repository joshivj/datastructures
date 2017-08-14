# selection_sort

def selection_sort(arr):

	
	for fillspot in range(len(arr)-1,0,-1):
		print 'array is ',arr
		positionMax = 0

		for location in range(1,fillspot+1):
			if arr[location] > arr[positionMax]:
				positionMax = location
		temp = arr[fillspot]
		arr[fillspot] = arr[positionMax]
		arr[positionMax] = temp
		

arr = [3,5,2,7,6,8,12,40,21]
selection_sort(arr)
