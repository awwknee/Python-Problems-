"""
CISC 131 Problem 3 - Ani Lamichhane (lami5034) and Vivian Ikeri (iker1395)
"""

def main():
    print("What is your word?", end="")
    word = input()
    print("What is your key?", end="")
    key = int(input())
    print(swapEnc(key, word))

def swapEnc(key, word):
    enc = ""
    for i in range(len(word)):
        enc = enc + word[(key-i)%len(word)]
    return enc

def swapDec(key, word):
    dec = ""
    for i in range(len(word)):
        dec = dec + word[(key-i)%len(word)]
    return dec

main()
