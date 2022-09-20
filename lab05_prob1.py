"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Vivian Ikeri (iker1395)
"""
def main():
    print("What is your word?", end="")
    word = input()
    print(isPalindrome(word))

def isPalindrome(word):
    rev = word[::-1]
    if word == rev:
        return True
    else:
        return False

main()
