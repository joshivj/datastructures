# Unique pairs
"""
input : pair_sum([1,3,2,2],4)

output : 2 pairs
i.e (1,3) and (2,2)
"""

def get_unique_pair(list_of_elems,k):
	if len(list_of_elems) < 2:
		print "Please increase data"
	else:
		seen = set()
		output = set()

		for num in list_of_elems:

			target = k - num

			if target not in seen:
				seen.add(num)
			else:
				output.add(((min(num,target)),max(num,target)))

	print output

get_unique_pair([1,3,2,2],4)