## Aim:- Write a Python program to find the most common elements and their counts from list, tuple, dictionary.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Imports Counter here.
from collections import Counter

# Defining List, Tuple & Dictionary here.
List = ['Python', 'C++', 'JavaScript', 'Ruby', 'Swift', 'JavaScript', 'Ruby', 'Swift', 'Python', 'C++', 'JavaScript', 'Ruby', 'Swift', 'Python', 'C++', 'Swift']
Tuple = (1, "Hello", 3.4, 1, 3.4, "Hello", "Hello", 3.4, 1, 3.4)
Dictionary = {1: 'Apple', 2: 'Ball', 3: 'Book', 4: 'Knife', 4: 'Knife'}

# Prints the most common elements and their counts respectively using most_common() method.
print(Counter(List).most_common(1))
print(Counter(Tuple).most_common(1))
print(Counter(Dictionary).most_common(1))