#string compression

def string_compression(s1):
	s1 = s1.strip()

	dict1 = {}
	end_string = ''

	for s in s1:
		if s in dict1:
			dict1[s] += 1

		else:
			dict1[s] = 1

	for data in dict1:
		end_string += '{0}{1}'.format(data,dict1[data])
	print end_string

string_compression('AAAABBBBCCCCCaaab')