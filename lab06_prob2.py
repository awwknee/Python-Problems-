"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Christina Bolcer (bolc6545)
"""
def main():
    list1 = [75, 82, 85, 92, 84]
    high = 90
    low = 80
    list3 = [85, 82, 98, 40, 68, 72, 99]
    list4 = [85, 82, 90, 99, 83, 67, 25, 33]
    print(countScoresInRange(list1, low, high))
    print("")
    print(scoresToGrades(list3))
    print("")
    printGradeGraph(list4)
    print("")
    print(countScoresInRange(list1, 60, 61))

def countScoresInRange(list1, low, high):
    length = 0
    for i in range(len(list1)):
        if list1[i] => low and list1[i] < high:
            length = length + 1
    return length

def scoresToGrades(list3):
    listgrade = []
    for i in range(len(list3)):
        if list3[i] >= 90:
            listgrade.append("A")
        elif list3[i] >= 80:
            listgrade.append("B")
        elif list3[i] >= 70:
            listgrade.append("C")
        elif list3[i] >= 60:
            listgrade.append("D")
        elif list3[i] < 60:
            listgrade.append("F")
    return listgrade

def printGradeGraph(list4):
    listgrade = []
    for i in range(len(list4)):
        if list4[i] >= 90:
            listgrade.append("A")
        elif list4[i] >= 80:
            listgrade.append("B")
        elif list4[i] >= 70:
            listgrade.append("C")
        elif list4[i] >= 60:
            listgrade.append("D")
        elif list4[i] < 60:
            listgrade.append("F")

    print("A: ", end="")
    for i in range(listgrade.count("A")):
        print("*", end="")
    print("")
    print("B: ", end="")
    for i in range(listgrade.count("B")):
        print("*", end="")
    print("")
    print("C: ", end="")
    for i in range(listgrade.count("C")):
        print("*", end="")
    print("")
    print("D: ", end="")
    for i in range(listgrade.count("D")):
        print("*", end="")
    print("")
    print("F: ", end="")
    for i in range(listgrade.count("F")):
        print("*", end="")

main()
