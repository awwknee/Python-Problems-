"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Thomas Sabu (sabu4338)
"""
def main():
    print("Integer:", end="")
    integer = int(input())
    print("Symbol:", end="")
    symbol = input()
    print("Second symbol:", end="")
    symbol2 = input()
    print("Width:", end="")
    width = int(input())
    print("Height:", end="")
    height = int(input())
    print("Number:", end="")
    num = int(input())

    printLine(integer, symbol)
    print("")
    (printRect(width, height, symbol))
    print("")
    (printUpTriangle(width, symbol))
    print("")
    (printDownTriangle(width, symbol))
    print("")
    (printHills(num, symbol, symbol2))

def printLine(integer, symbol):
    symsum = ""
    for _i in range(integer):
        symsum = symbol + symsum
    return print(symsum)

def printRect(width, height, symbol):
    symsum = ""
    for _i in range(width):
        symsum = symbol + symsum
    for _i in range(height):
        print(symsum)

def printUpTriangle(width, symbol):
    symsum = ""
    for _i in range(width):
        symsum = symbol + symsum
        tri = print(symsum)
    return tri

def printDownTriangle(width, symbol):
    symsum = symbol
    for o in range(width, 0, -1):
        for _i in range(1, o):
            symsum = symbol + symsum
        print(symsum)
        symsum = symbol

def printHills(num, symbol, symbol2):
    for _o in range(1, 0, -1):
        for x in range(1, num+1):
            num = x
            printUpTriangle(num, symbol)
            printDownTriangle(num, symbol2)
main()
