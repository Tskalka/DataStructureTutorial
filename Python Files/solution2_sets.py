data_set3 = {1, 8, 17, 15, 27, 40, 38, 94, 100, 567, 394}
data_set4 = {1, 10, 15, 20, 25, 27, 44, 37, 97, 83, 100}
# the intersection between the 2 sets, finds the points that are repeated
# the shorthand for intersection
repeated_data = data_set3 & data_set4

print(repeated_data)
#output: {1, 27, 100, 15}