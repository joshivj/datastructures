#Anagram problem

# input1 = 'public relations'
# output1 = 'crap built on lies'

input = 'client eastwood'
output = 'old west action'


def check_for_anagram(input1,output1):

	"""
		checks for Anagram
	"""
	input1 = input1.lower()
	output1 = output1.lower()
	len_of_input1 = len(input1)
	len_of_output1 = len(output1)

	input_1_dict = {}
	output_1_dict = {}

	if len_of_input1 == len_of_output1:
		striped_input1 = ''.join(input1.split(' '))
		striped_output1 = ''.join(input1.split(' '))

		for i in range(len(striped_input1)+1):
			if i in input_1_dict:
				input_1_dict[i] += 1
			else:
				input_1_dict[i] = 1

		for i in range(len(striped_output1)+1):
			if i in output_1_dict:
				output_1_dict[i] += 1
			else:
				output_1_dict[i] = 1

		if output_1_dict == input_1_dict:
			print True
		else:
			print False

		
	else:
		print False

check_for_anagram(input,output)