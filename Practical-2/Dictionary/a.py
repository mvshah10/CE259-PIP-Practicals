## Aim:- Write a Python script to check whether a given key already exists in a dictionary.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Initializing the Dictionary here.
Dictionary = {1: 20, 2: 40, 3: 60, 4: 10, 5: 30, 6: 50}

# Defining 'check_key' to check whether a key is present or not in the given dictionary.
check_key = 4

# Condition to check whether that particular key is present or not in the given dictionary.
if check_key in Dictionary:
    print('\nThe key is present in the given dictionary.\n')
else:
    print('\nThe key is not present in the given dictionary.\n')
