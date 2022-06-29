# Stacks in Python

## What is a stack?
A stack is a data structure that *insertion* and *deletion* happen on the same end (at the back of the stack). A stack is commonly refered to as a "LIFO" order, which means "last in, first out." The operation of insertion or adding data is commonly refered to as a push. The operation of removing/getting data from the stack is called a pop. 

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
* * test
* pop() - Removes/returns the value from the back of the stack
* size() - returns the size of the stack
* empty() - returns true is stack length is 0
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

## Test your knowledge problem
