"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Matt Toivonen (mtoiv4007)
"""

import math

def main():
    print("Values you want to represent: ", end="")
    valueofnumbits = int(input())
    print(numBits(valueofnumbits))
def numBits(valueofnumbits):
    exponent = math.log2(valueofnumbits)
    exponent_floor = math.ceil(exponent)
    return exponent_floor

main()
