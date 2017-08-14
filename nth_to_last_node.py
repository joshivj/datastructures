# nth_to_last_node
"""
Write a function that takes a head node and an integer value n and then returns the nth to last node in the linked list.
"""

class Node:

    def __init__(self, value):
        self.value = value
        self.nextnode  = None

def nth_to_last_node(n, head):

	node = head

	nodes = []
	while node != None:
		nodes.append(node)
		node = node.nextnode

	return nodes[-n]

"""
RUN THIS CELL TO TEST YOUR SOLUTION AGAINST A TEST CASE 

PLEASE NOTE THIS IS JUST ONE CASE
"""

from nose.tools import assert_equal

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)
f = Node(6)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
e.nextnode = f

####

class TestNLast(object):
    
    def test(self,sol):
        
        assert_equal(sol(4,a),c)
        print 'ALL TEST CASES PASSED'
        
# Run tests
t = TestNLast()
t.test(nth_to_last_node)
