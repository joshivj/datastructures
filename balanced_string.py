# balanced_string

def check_balanced_string(s1):
	
	if len(s1)%2 != 0:
		return False

	opening = set('([{')

	matches = set([ ('{','}'), ('[',']'), ('(',')') ])

	stack = []
	for perm in s1:

		if perm in opening:
			stack.append(perm)
		else:

			if len(stack) == 0 :
				return False
			last_val = stack.pop()

			if (last_val,perm) not in matches:
				return False

	return len(stack) == 0

# '([])'
b = check_balanced_string('[[]()[]]')
print b

