# Stacks in Python

## What is a stack?
A stack is a data structure that *insertion* and *deletion* happen on the same end (at the end of the stack). These are commonly called push() and pop().

## Real world example of a stack
A good example of a stack is a long driveway that has a width of one car. Any car that comes into the driveway, adds itself to the end of the line. Any car that leaves from the driveway, also leaves from the end.

## How to implement a Stack in Python
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
#Cars in driveway red, blue, black
```
## Common Stack Operations/ Big O

## Example Problem
## Test your knowledge problem
