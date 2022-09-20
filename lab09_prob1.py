"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""
def promptInt(mystr):
    mystr2 = input(mystr)
    mystr2 = mystr2.split(" ")
    mystr2 = mystr2[len(mystr2)-1]

    while mystr2.strip('-').isnumeric() is False:
        print("I'm sorry, that is not a valid number")
        mystr2 = input(mystr)
        mystr2 = mystr2.split(" ")
        mystr2 = mystr2[len(mystr2)-1]

    return int(mystr2)
print(promptInt("Enter a number: "))
