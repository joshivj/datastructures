# queue implementation

class Queue(object):

	def __init__(self):
		self.items = []

	def enQueue(self,item):
		return self.items.insert(0,item)

	def deQueue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

q = Queue()
q.enQueue(5)
q.enQueue(4)
print q.size()
print q.items
q.deQueue()
print q.items