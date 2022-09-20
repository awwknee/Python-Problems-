"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Thomas Sabu (sabu4338)
"""
def main():
    print("What is your number? ", end="")
    num = int(input())
    print(isPrime(num))
def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num%i == 0:
            return False
    return True
main()
