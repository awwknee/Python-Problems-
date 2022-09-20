"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) Jane Doe (jdoe1234)
"""

def factors(num):
    factorlist = []
    for i in range(1, num + 1):
        if num % i == 0:
            factorlist.append(i)
    return factorlist

def exists(num, factorlist):
    for i in range(len(factorlist)):
        if factorlist[i] == num:
            return True
    return False

def gcd(num1, num2):
    factorlist1 = []
    factorlist2 = []
    for i in range(1, num1 + 1):
        if num1 % i == 0:
            factorlist1.append(i)
    for i in range(1, num2 + 1):
        if num2 % i == 0:
            factorlist2.append(i)

    same = []
    for i in range(len(factorlist1)):
        for x in range(len(factorlist2)):
            if factorlist1[i] == factorlist2[x]:
                same.append(factorlist1[i])

    return max(same)
