"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""
def reverseString(mystr):
    if len(mystr) == 1:
        return mystr
    else:
        return reverseString(mystr[1:]) + mystr[0]
