# problem1. check for balanced string.
# problem2. use two stacks to create queue


def check_for_balanced_string(s1):
	# '{[]}'

	if len(s1)%2 != 0:
		return False

	s1 = s1.strip()

	opening = set('{([')

	matches = set([ ('{','}'), ('(',')'), ('[',']') ])

	stack = []
	for elem in s1:
		if elem in opening:
			stack.append(elem)
		else:
			if len(stack) == 0:
				return False

			last_pop_item = stack.pop()

			if (last_pop_item,elem) in matches:
				return True
			else:
				return False

	if len(stack) == 0:
		return True

# c = check_for_balanced_string('{[]{}}')
# print c

# now use two stacks to create queue

class StackstoQueue(object):

	def __init__(self):
		self.instack = []
		self.outstack = []

	def enqueue(self,item):
		self.instack.append(item)

	def dequeue(self):
		if self.outstack == []:
			while len(self.instack) > 0 :
				self.outstack.append(self.instack.pop())

		return self.outstack.pop()


q = StackstoQueue()

for i in xrange(5):
	q.enqueue(i)

for i in xrange(5):
	print q.dequeue()

