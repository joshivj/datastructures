# find missing element
import collections

# finder([1,2,3,4,5,6,7],[3,7,1,4,6])

def find_missing_elem(arr1,arr2):
	arr1.sort()
	arr2.sort()
	# # first approach
	# missing_ele = []
	# if arr1 == arr2:
	# 	print 'every element present in second array'
	# else:
	# 	for ele in arr1:
	# 		if not ele in arr2:
	# 			missing_ele.append(ele)

	# print missing_ele

	# second approach

	d = collections.defaultdict(int)

	for num in arr2:
		d[num] += 1

	for num in arr1:
		if d[num] == 0:
			print num
		else:
			d[num] -= 1

#find_missing_elem([1,2,3,4,5,6,7],[3,7,1,4,6])
find_missing_elem([5,5,7,7],[5,7,7])
