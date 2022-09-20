"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""

def sortBinary(mylist):
    sliced = mylist[:2]
    rest = mylist[2:]

    if len(sliced) <= 1:
        return sliced
    else:
        if sliced[0] == sliced[1]:
            if sliced[0] == 0:
                rest = sortBinary(rest)
                rest.insert(0, sliced[0])
                rest.insert(0, sliced[1])
                return rest
            elif sliced[0] == 1:
                rest = sortBinary(rest)
                rest.append(sliced[0])
                rest.append(sliced[1])
                return rest
        elif (sliced[0] == 0 and sliced[1] == 1):
            rest = sortBinary(rest)
            rest.insert(0, sliced[0])
            rest.append(sliced[1])
            return rest
        else:
            rest = sortBinary(rest)
            rest.insert(0, sliced[1])
            rest.append(sliced[0])
            return rest
