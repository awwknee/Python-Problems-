"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Christina Bolcer (bolc6545)
"""
def main():
    my_list = [12.5, -36.375, 100, 0.0]
    x = listStats(my_list)
    printStats(x)

def listStats(my_list):
    listmin = my_list[:]
    listmax = my_list[:]
    listaver = my_list[:]

    listmin.sort()
    listmax.sort()

    min1 = listmin[0]
    max1 = listmax[-1]

    average1 = 0
    mysum = 0
    for i in range(len(listaver)):
        mysum = mysum + my_list[i]
    average1 = mysum/(len(listaver))

    mma = [min1, max1, average1]

    return mma

def printStats(mma):
    print("The minimum is {:.3f}, the maximum is {:.3f}, the average is {:.3f}"\
        .format(mma[0], mma[1], mma[2]))

main()
