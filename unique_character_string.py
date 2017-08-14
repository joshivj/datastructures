#unique_character_string

"""
if string is 'abcd' return true
else if string is 'aabcd' return false
"""

def unique_char(s1):
	s1 = s1.strip()

	if len(s1) == 1 :
		return True
	else:
		chars = set()

		for s in s1:
			if s in chars:
				return False
			else:
				chars.add(s)
		return True

a = unique_char('cdfd')
print a
