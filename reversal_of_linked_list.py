# reversal_of_linked_list

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def reverse(head):

	current = head
	prev = None
	nextnode = None

	while current:
		nextnode = current.nextnode
		current.nextnode = prev
		prev = current
		current = nextnode
		

	return prev

# Create a list of 4 nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

# Set up order a,b,c,d with values 1,2,3,4
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e

print a.nextnode.value
print b.nextnode.value
print c.nextnode.value
print d.nextnode.value
print e.nextnode

reverse(a)

print 'after reverse----'
print e.nextnode.value
print d.nextnode.value
print c.nextnode.value
print b.nextnode.value
print a.value

# a-b-c-d