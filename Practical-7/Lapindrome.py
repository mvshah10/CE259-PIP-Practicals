## Aim:- Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency. Also, abccab, rotor and xyzxy are a few examples of lapindromes. Note that abbaab is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match. Your task is simple. Given a string, you need to tell if it is a lapindrome.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Prompting the user to enter the no. of words here.
number = int(input())

for i in range(number):
    # Prompting user to enter words here.
    word = input()
    # Checking length of word here.
    length = len(word)
    # Condition if length of word is even.
    if length % 2 == 0:
        b, c = word[:length//2], word[length//2:]
    # Condition if length of word is odd.
    else:
        b, c = word[:length//2], word[length//2+1:]
    # Condition to display final result here.
    if sorted(b) == sorted(c):
        print("YES")
    else:
        print("NO")
