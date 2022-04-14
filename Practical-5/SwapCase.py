## Aim:- You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
## Student_Name:- Meghal Shah
## Student_ID:- 20CS085

# Defining a function called 'swapCase' here.
def swapCase(sc):
    # For output string here
    char_swap = ''
    for character in sc:
        # Condition to check if a character is in uppercase then swap it to lowercase.
        if(character.isupper() == True):
            char_swap += (character.lower())
        # Condition to check if a character is in lowercase then swap it to uppercase.
        elif(character.islower() == True):
            char_swap += (character.upper())
        # Condition to print special characters as it is in the final result too.
        else:
            char_swap += character
        # Returning 'char_swap' here
    return char_swap

if __name__ == '__main__':
    # Prompting user to enter the string here.
    sc = input()
    finalresult = swapCase(sc)
    # Displaying final result here.
    print(finalresult)
