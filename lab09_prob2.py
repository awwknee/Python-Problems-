"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""
def syracuse(num):
    numstr = str(num) + ", "

    while num != 1:
        if num % 2 == 0:
            num = num//2
            numstr = numstr + str(num) + ", "

        elif num % 2 == 1:
            num = 3*(num)+1
            numstr = numstr + str(num) + ", "

    numstr = numstr.strip()
    numstr = numstr.strip(',')

    return numstr
