# stackstoqueue problem

"""
	use two stacks to create queues
"""

class StackstoQueque(object):

	def __init__(self):
		self.stack1 = []
		self.stack2 = []

	def enqueue(self,item):
		return self.stack1.append(item) # [0,1,2,3,4]
		

	def dequeue(self):

		if not self.stack2:
			while self.stack1:
				self.stack2.append(self.stack1.pop())

		return self.stack2.pop()

q = StackstoQueque()

for i in xrange(5):
	q.enqueue(i)

for i in xrange(5):
	print q.dequeue()

# output 
"""
0
1
2
3
4
"""