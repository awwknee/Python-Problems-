"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""

def prettyPrint(mylist, indentlvl):

    start = 4 * indentlvl * " " + "["
    print(start)

    spaces = (4*(indentlvl+1)) * " "

    for i in range(len(mylist)):
        if isinstance((mylist[i]), list) is True:
            prettyPrint(mylist[i], indentlvl+1)
            if i == len(mylist) - 1:
                print(spaces + "]")
            else:
                print(spaces + "],")

        if isinstance((mylist[i]), str) is True:
            if mylist[i] != mylist[len(mylist)-1]:
                print(spaces + '"{}",'.format(mylist[i]))
            else:
                print(spaces + '"{}"'.format(mylist[i]))

        if isinstance((mylist[i]), (int, float)) is True:
            if mylist[i] != mylist[len(mylist)-1]:
                print(spaces + str(mylist[i]) + ",")
            else:
                print(spaces + str(mylist[i]))

    if indentlvl == 0:
        print(4 * indentlvl * " " + "]")
