"""
CISC 131 Problem 2 - Ani Lamichhane (lami5034) and Vivian Ikeri (iker1395)
"""

def main():
    print("What is your phrase: ", end="")
    phrase = input()
    print(acronym(phrase))

def acronym(phrase):
    acro = ""
    for i in range(0, len(phrase)):
        if phrase[i] != " " and ((phrase[i-1] == " " and phrase[i] != " ") or i == 0 ):
            acro = acro + phrase[i].upper()
    return acro

main()
   