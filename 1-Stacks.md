# Stacks in Python

## What is a stack?
A stack is a data structure that *insertion* and *deletion* happen on the same end (at the back of the stack). A stack is commonly refered to as a "LIFO" order, which means "last in, first out." The operation of insertion or adding data is commonly called a **push**. The operation of removing/getting data from the stack is called a **pop**. 

## Real world example of a stack
A good example of a stack is a long driveway that has a width of one car. Any car that comes into the driveway, adds itself to the back of the line of cars. Any car that leaves from the driveway, also leaves from the back.

## How to implement a Stack using a list in Python
```python
driveway = []
#List of cars in the order they enter the driveway
driveway.append("red")
driveway.append("blue")
driveway.append("black")
driveway.append("silver")

#The last car in the driveway leaves (silver)
driveway.pop()

for car in driveway:
    print(car)
#Cars in the driveway red, blue, black
```
## Common Stack Operations/ Big O
* push(value) - Adds the value to the back of the stack.
* pop() - Removes/returns the value from the back of the stack
* size() - returns the size of the stack
* empty() - returns true is stack length is 0
**The Big O for ALL the common operators is 0(1)**
```python
stack = []
#push
stack.append(value)
#pop
x = stack.pop()
#size
len = len(stack)
#empty
if len(stack) == 0:
```
## Example Problem
### Reversing the order of a list using a stack
```python
# Reverse the order of the list!
original_list = [1, 2, 3, 4, 5]
reversed_list = []

#iterates through all the items of the list
for item in range(len(original_list)):
    #Removes the value from the end of original_list!
    value = original_list.pop()
    #Adds the last item of original list to the empty reversed list
    reversed_list.append(value)

print(reversed_list)
#Output [5, 4, 3, 2, 1]
```


## Test your knowledge problem