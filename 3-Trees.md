# Trees in Python
## What are trees in python?
Trees are a data structure that has nodes that are connected by pointers. It is similar to the structure of a linked list.
In this tutorial, we will talk about a binary tree, a binary search tree, and a balanced binary search tree.

### Binary tree

![Tree](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Tree.PNG)

A binary tree is a tree that only connects up to two nodes (hence the name binary).
The image above goes over all the basic parts of this binary tree structure.
Sometimes the nodes can have pointers that go up and down the binary tree.

### Binary Search tree

![BST](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Binary%20Search%20Tree.PNG)

A binary search tree has certain rules to help organize the data within. Data placecd into the tree will be compared to the parent node, if it is greater than the value of the parent node, then the value will be placed as a child on the right. If the value being placed is less than that of the parent node, then the value will be placed as a child node on the left.
As an example, imagine the number 8 is our parent node (view picture above). If I were to pass in the value 9, it would be greater than the parent node 8, so it will be a child placed on the right.

### Balanced Binary Search tree

![Balanced BST](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Balanced%20Binary%20Tree.PNG)

This is a binary tree where the height of the left and right subtree do not differ more than 1.
By having our binary search tree balanced, we can maintain an O(log n) performance for searching within the tree.

### Unbalanced Binary Search tree/Linked List

![Linked List](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Unbalanced%20BST%20Linked%20list.PNG)

This is an example of an unbalanced binary serach tree, which in actuality, is just a linked list. This means that the searching operation has an O(n) performance, meaning that we would potentially need to go through all the data to find the value we are looking for. Maintaining a balanced binary search tree will save you performance.

### Recursion
Recursion is when a function calls itself, and to prevent this from going on infinitly(or until your editor/environment gets mad), you create what is called a *base case* or logic that will stop the function from calling iteself infinitly.
We will use recurision to perform a lot of the common operators of trees.

### Recursion Example
[Recursion example](https://github.com/Tskalka/DataStructureTutorial/blob/main/3-Trees.md)
Try it a few times :)
## How to implement a Tree in Python

```python
class BST:
    class Node:
        """
        Each node connects to the left/right subtree
        """

        def __init__(self, data):
            """ 
            Node's links are set to none
            """
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        """
        Setting the root node to none, empty tree
        """
        self.root = None

```

## Common Binary Search tree Operations/ Big O
* insert(value) - Inserts value to the tree
* Performance O(log n)
```python
def insert(self, data):
        """
        Insert 'data' into the Binary Search tree.
        """
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)  # Start at the root
            
def _insert(self, data, node):
        """
        This function will look for a place to insert a node
        with 'data' inside of it.  The current sub-tree is
        represented by 'node'.  This function is intended to be
        called the first time by the insert function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        elif data > node.data:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
```
* remove(value) - Removes value from the tree
* Performance O(log n)
```python
def deleteNode(root, data):
 
    # Base Case
    if root is None:
        return root
 
    if data < root.data:
        root.left = deleteNode(root.left, data)
 
    elif(data > root.data):
        root.right = deleteNode(root.right, data)
 
    else:
    
        if root.left is None:
            temp = root.right
            root = None
            return temp
 
        elif root.right is None:
            temp = root.left
            root = None
            return temp
 
        temp = minValueNode(root.right)
 
        root.data = temp.data
 
        root.right = deleteNode(root.right, temp.data)
 
    return root
```

* contains(value) - Determines if a value is in the tree
* Performance O(log n)
```python
   def contains(self, value):
        return self._contains(value, self.root)

    def _contains(self, value, node):
        if node is None or node.value is None:
            return False
        else:
            if value == node.value:
                return True
            elif value < node.value:
                return self._contains(value, node.left)
            else:
                return self._contains(value, node.right)
```

* traverse_forward - Iterates through all the objects, small to large
* Performance O(n)
```python
def __iter__(self):
        """
        Perform a forward traversal (in order traversal) starting from 
	    the root of the BST.

        for value in my_bst:
            print(value)

        """
        yield from self._traverse_forward(self.root)  # Start at the root
        
    def _traverse_forward(self, node):
        """
        Does a forward traversal (in-order traversal) through the 
        BST. 

        for value in my_bst:
            print(value)

        This function is intended to be called the first time by 
        the __iter__ function.
        """
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
```
* traverse_reverse - Iterates through all objects from large to small
* Performance O(n)
```python

 def __reversed__(self):
        """
        for value in reversed(my_bst):
            print(value)
        """        
        yield from self._traverse_backward(self.root)  # Start at the root

 def _traverse_backward(self, node):
        """
        Does a backwards traversal (reverse in-order traversal) through the 
        BST.         
        """
        # Do the opposite of traverse forward
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)
````

* height(node) - Returns height of the tree
* Performance O(n)
```python
    def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

    def _get_height(self, node):
        """
        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0

        right = self._get_height(node.right) + 1
        left = self._get_height(node.left) + 1

        #Decides which sub-tree is taller and returns it
        if right > left:
            return right
        else:
            return left
```


* size() - Returns size of the tree
* Performance O(1)
```python
def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+ 1 + size(node.right))
```
* empty() - Returns true if the tree is empty.
* Performance O(1)
```python
def isempty(self):
    return self.root is None
```

## Example Problem
You have been asked to find the smallest value in a binary search tree. How would you go about doing this?
The answer is actually quite simple, as long as you understand the structure of a binary search tree.
Remember that any number that is less than the parent node will become the child on the left, so by finding the last value on the left hand side of the tree, will be the lowest value. 
```python
class Node:
	def __init__(self, key):
		self.data = key
		self.left = None
		self.right = None
# a basic insert function to add numbers to the tree
def insert(node, data):

	if node is None:
		return (Node(data))

	else:

		if data <= node.data:
			node.left = insert(node.left, data)
		else:
			node.right = insert(node.right, data)
		return node
#this is how we will find the smallest value
def smallValue(node):
	current = node

	# We will want to loop through the left side of the binary search tree
    # because this consists of the values lower than the root node.
	while(current.left is not None):
		current = current.left
	return current.data


root = None
root = insert(root,4)
insert(root,3)
insert(root,1)
insert(root,2)
insert(root,6)
insert(root,5)

print ("The least value in this binary search tree is: %d" %(smallValue(root)))
# this will give us an answer of 1 being the smallest value in the binary search tree.
```
By having our information organized, this problem becomes quite easy to solve.
## Test your knowledge problem
Now that you understand trees, let's test what you have learned. 
How would you find the largest value of this binary search tree?
Fill out the logic for the greatValue() function to return the greatest value in this binary search tree.
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
    #insert logic to find the greatest value in the binary search tree. 
    #if you're lost, think about how a binary search tree is organized.
    return 
    
root = None
root = insert(root,4)
insert(root,3)
insert(root,1)
insert(root,2)
insert(root,6)
insert(root,5)

print ("The greatest value in this binary search tree is: %d" %(greatValue(root)))

```
[Solution](https://github.com/Tskalka/DataStructureTutorial/blob/main/Python%20Files/solution3_trees.md)
