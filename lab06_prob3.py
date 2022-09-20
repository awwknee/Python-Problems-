"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Christina Bolcer (bolc6545)
"""
def main():
    mylist = [5, 2, 3, 5, 5, 3]
    print(hasDuplicates(mylist))
    print(removeDuplicates(mylist))
    removeDuplicatesInPlace(mylist)

def hasDuplicates(mylist):
    list1 = mylist[:]
    list1.sort()
    for i in range(len(list1)-1):
        if list1[i] == list1[i+1]:
            return True
    return False

def removeDuplicates(mylist):
    list2 = mylist[:]
    list2.sort()
    #[2,3,3,5,5,5]
    listremove = []
    for i in range(len(list2)):
        if list2[i] != list2[i-1]:
            listremove.append(list2[i])
    return listremove

def removeDuplicatesInPlace(mylist):
    listremove2 = mylist[:]
    listremove2.sort()
    mylist.sort()
    for i in range(len(listremove2)):
        if listremove2[i] == listremove2[i-1]:
            mylist.remove(listremove2[i])
main()
