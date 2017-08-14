# double_linked_list implementation

class DoublyLinkedList(object):

	def __init__(self,val):

		self.value = val
		self.next_node = None
		self.prev_node = None

a = DoublyLinkedList(1)
b = DoublyLinkedList(2)
c = DoublyLinkedList(3)

a.next_node = b
b.prev_node = a

b.next_node = c
c.prev_node = b

# if you want to make circularlinked list then point c.next_node = a

