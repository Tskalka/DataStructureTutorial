# Trees in Python
## What are trees in python?

### Binary tree

![Tree](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Tree.PNG)

### Binary Search tree

![BST](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Binary%20Search%20Tree.PNG)

### Balanced Binary Search tree

![Balanced BST](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Balanced%20Binary%20Tree.PNG)

### Unbalanced Binary Search tree/Linked List

![Linked List](https://github.com/Tskalka/DataStructureTutorial/blob/main/Picture%20Files/Unbalanced%20BST%20Linked%20list.PNG)

### Recursion
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

* contains(value) - Determines if a value is in the tree
* traverse_forward - Iterates through all the objects, small to large
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

* height(node) - Returns height of the 
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
```python
def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+ 1 + size(node.right))
```
* empty() - Returns true if the tree is empty.





## Example Problem

## Test your knowledge problem
