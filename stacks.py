# stacks implementation

class Stacks(object):

	def __init__(self):

		self.items = []

	def isEmpty(self):
		return self.items == []

	def size(self):
		return len(self.items)

	def push(self,item):
		return self.items.append(item)

	def pop(self):
		return self.items.pop()


s = Stacks()
s.size()
s.push(1)
s.push(22)
print s.size()
print s.isEmpty()
print s.pop()
print s.size()
s.push(44)
print s.items
