"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""
def molecularWeight(mydict, mylist):
    weight = 0

    for atom in mylist:
        weight = weight + mydict[atom]

    return weight
