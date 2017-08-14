# implementation of singly_linked_list

class Node(object):

	def __init__(self,val):

		self.value = val
		self.nextNode = Node

a = Node(1)
b = Node(2)
c = Node(3)
a.nextNode = b
b.nextNode = c
print a.nextNode.value