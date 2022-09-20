"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Matt Toivonen (mtoiv4007)
"""

def main():
    print("Write a 4-digit positive integer: ", end="")
    inputnum = int(input())
    print(myReverse(inputnum))

def myReverse(inputnum):
    one_digit = inputnum % 10
    inputnum1 = (inputnum // 10)
    ten_digit = inputnum1 % 10
    inputnum10 = inputnum // 100
    hundred_digit = inputnum10 % 10
    inputnum100 = inputnum // 1000
    thousand_digit = inputnum100 % 10
    return one_digit * 1000 + ten_digit * 100 +hundred_digit * 10 + thousand_digit

main()
