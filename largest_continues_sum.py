
# given an array of integers(positive and neg), find the largest continuoes sum



def large_cont_sum(arr):
	if len(arr) < 1 :
		return 0
	max_sum = current_sum = arr[0]

	for num in arr[1:]:

		current_sum = max(num,current_sum+num)
		max_sum = max(current_sum,max_sum)

	print max_sum

large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) #29