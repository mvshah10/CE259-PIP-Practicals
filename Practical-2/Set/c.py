## Aim:- Write a Python program to create an intersection, Union, difference of sets.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Creating two sets here.
A = {5, 8, 1}
B = {4, 8, 2}

# Computing intersection between A & B sets using intersection() method.
print("Intersection of A & B sets:", A.intersection(B))

# Computing union between A & B sets using union() method.
print("\nUnion of A & B sets:", A.union(B))

# Computing difference between A & B sets using difference() method.
print("\nA-B:", A.difference(B))
print("B-A:", B.difference(A))