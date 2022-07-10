# Set in Python

## What is a Set?
A set list is a datastructure where order does not matter and no duplicates are allowed, but with these restrictions, comes great benefits. We can determine if something is part of the defined set in O(1) time, which is extremely efficent. 

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
union_set = my_set1 | my_set2
#results:
#{5, 10, 15, 20, 30}

#two different ways to do a set intersection in python
intersection_set = intersection(my_set1, my_set2)
intersection_set = my_set1 & my_set2
#results:
#{10, 20}
```

## Example Problem
You have been given two large sets of data at your new job. You job is to remove all the duplicate items present in both datasets.
Using a set, how would you solve this problem?
```python
#Data given to you
data_set1 = {1, 2, 2, 2, 3, 5, 8, 99, 99, 500, 500, 300, 55, 37, 28}

data_set2 = {1, 1, 1, 1, 5, 8, 9, 11, 350, 980, 300, 341, 55, 27 , 38}

# This problem is quite easy to solve if you understand sets. Remember sets cannot have duplicate numbers.
# So if we create a combined set of data_set1 and data_set2, it will give us all the unique values of each set

#shorthand for creating a union
combined_data = data_set1 | data_set2
print(combined_data)

#The results:
{1, 2, 3, 5, 8, 9, 11, 980, 341, 27, 28, 350, 99, 37, 38, 300, 500, 55}

```

## Test your knowledge problem
You are given 2 new sets of data again at your new job, but now, your boss wants you to only return the duplicate items from the two sets of data.
How would you go about solving this using a set?

```python
#find the repeated values from the two data sets
data_set3 = {1, 8, 17, 15, 27, 40, 38, 94, 100, 567, 394}
data_set4 = {1, 10, 15, 20, 25, 27, 44, 37, 97, 83, 100}
```
[Solution](https://github.com/Tskalka/DataStructureTutorial/edit/main/2-Sets.md)
