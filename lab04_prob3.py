"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Thomas Sabu (sabu4338)
"""
def main():
    print("What is your number? ", end="")
    number = int(input())
    print("How many times do you want to run? ", end="")
    time = int(input())
    print(naturalLog(number, time))

def naturalLog(number, time):
    z = 1
    sumsofar = 0
    for _i in range(time):
        log = ((1/z)*((number-1)/(number+1))**z)
        z = z + 2
        sumsofar = sumsofar + log
    return sumsofar*2
main()
