# Set in Python

## What is a Set?
A set list is a datastructure where order does not matter and no duplicates are allowed, but with these restrictions, comes great benefits. We can determine if something is part of the defined set in O(1) time, which is extremely efficent. 

## Real world example of a Set


## How to implement a Set in python
A set is written with curly braces
```python
example_set = {1, 2, 3}
````
An empty set is defined a little differently
```python
empty_set = set()
```
## Common Set Operations in python/ Big O
* add(value) - Adds value to the set
* remove(value) - Removes value from the set
* member(value) - Determines if the value is part of a set
* size() - returns the number of items in a set

**The Big O for ALL the common operators is 0(1)**
```python
#add
example_set.add(value)
#remove
example_set.remove(value)
#member
if value in example_set:
#size
length = len(example_set)
```
### Union and Intersection in Sets
* union() - combines two sets together into one
* intersection() - finds the same numbers from two different sets
```python
my_set1= {5, 10, 15, 20}
my_set2 = {10, 20, 30}
#two different ways to unionize two sets in python
union_set = union(my_set1, my_set2)
union_set = my_set1 & my_set2
#results:
#{5, 10, 15, 20, 30}

#two different ways to do a set intersection in python
intersection_set = intersection(my_set1, my_set2)
intersection_set = my_set1 | my_set2
#results:
#{10, 20}
```

## Example Problem

## Test your knowledge problem

