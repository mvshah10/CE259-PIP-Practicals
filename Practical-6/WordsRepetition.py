## Aim:- You are given n words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Importing dictionary subclass 'OrderedDict' from 'collections' here.
from collections import OrderedDict;

# Prompting user to enter no. of words she/he wishes for.
number = int(input())
dict = OrderedDict()

for i in range(number):
    # Prompting user to enter word here.
    word = input()
    # Condition to check for word appearing more than one time.
    if word in dict:
        dict[word] += 1
    # Condition for a word appearing only once.
    else:
        dict[word] = 1

# To print distinct no. of words 
print(len(dict))

# Displaying result here.
for key, value in dict.items():
    print(value, end = " ")
