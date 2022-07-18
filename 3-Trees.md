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
* remove(value) - Removes value from the tree
* contains(value) - Determines if a value is in the tree
* traverse_forward - Iterates through all the objects, small to large
* traverse_reverse - Iterates through all objects from large to small
* height(node) - Returns height of the 
* size() - Returns size of the tree
* empty() - Returns true if the tree is empty.

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



## Example Problem

## Test your knowledge problem
