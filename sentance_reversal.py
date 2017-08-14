# sentence reversal
import re

def sentence_reversal(string_val):

	string_val = string_val.strip() # remove whitespaces
	string_val = re.sub(' +',' ',string_val) # remove multiple spaces in between
	# split string on spaces

	string_list = string_val.split(' ')
	

	# reverse the string

	string_list.reverse()

	print ' '.join(string_list)



# sentence_reversal('hi how are you')

sentence_reversal('hi john,   are you ready to go?')