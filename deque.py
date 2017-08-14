# deque implementation

class Deque(object):

	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def addRear(self,item):
		self.items.insert(0,item)

	def addFront(self,item):
		self.items.append(item)

	def removeFront(self):
		self.items.pop()

	def removeRear(self):
		self.items.pop(0)

d = Deque()
print d.items
d.addRear(3)
d.addFront(1)
d.addFront(2)
print d.items
d.removeFront()
print d.items