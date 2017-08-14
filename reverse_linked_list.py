# reverse_linked_list

"""
Problem
Write a function to reverse a Linked List in place. The function will take in the head of the list as input and return the new head of the list.
"""

class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None


# def reverse(head): # bad apporoach
    
#     head_node = head
#     running_node = head
#     stacks = []
#     while running_node != None:
#     	stacks.append((running_node,running_node.nextnode))
#     	running_node = running_node.nextnode

#     for (firstnode,secondnode) in stacks:
#     	if secondnode != None:
# 	    	secondnode.nextnode = firstnode
# 	    	if firstnode == head_node:
# 	    		firstnode.nextnode = None

def reverse(head):
    
    # Set up current,previous, and next nodes
    current = head
    previous = None
    nextnode = None

    # until we have gone through to the end of the list
    while current:
        
        # Make sure to copy the current nodes next node to a variable next_node
        # Before overwriting as the previous node for reversal
        nextnode = current.nextnode

        # Reverse the pointer ot the next_node
        current.nextnode = previous

        # Go one forward in the list
        previous = current
        current = nextnode

    return previous

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
print a.nextnode
    	
