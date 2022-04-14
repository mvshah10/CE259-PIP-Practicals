## Aim:- Write a Python script to concatenate following dictionaries to create a new one.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Initializing the Dictionaries.
Dictionary1 = {1:10, 2:20}
Dictionary2 = {3:30, 4:40}
Dictionary3 = {5:50, 6:60}

# Defining new dictionary named 'Concate_Dictionary' which will concatenate above dictionaries.
Concate_Dictionary = {}

# Concatenating the given dictionaries into new one.
for dict in (Dictionary1, Dictionary2, Dictionary3): Concate_Dictionary.update(dict)

# Prints new concatenated dictionary.
print(Concate_Dictionary)