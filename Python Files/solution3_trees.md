```python

class Node:

	# Constructor to create a new node
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None

def insert(node, data):

	if node is None:
		return (Node(data))

	else:

		if data <= node.data:
			node.left = insert(node.left, data)
		else:
			node.right = insert(node.right, data)
		return node

def greatValue(node):
	current = node

    #By looping throug the right side, all the values that are placed to the right are larger than that of their parents
	while(current.right is not None):
		current = current.right
	return current.data

root = None
root = insert(root,4)
insert(root,3)
insert(root,1)
insert(root,2)
insert(root,6)
insert(root,5)

print ("The greatest value in this binary search tree is: %d" %(greatValue(root)))
# This will give us 6 because that is the greatest value in the BST.




```
