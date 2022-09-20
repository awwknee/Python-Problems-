"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034) and Logan Schorn (scho6370)
"""
def main():
    print("Month:", end="")
    month = int(input())
    print("Date:", end="")
    date = int(input())
    print("Year:", end="")
    year = int(input())
    print(calDayNum(month, date, year))

def leapYear(year):
    if (year%4 == 0 and year%100 != 0) or year%400 == 0:
        return "True"
    else:
        return "False"

def validDate(month, date, year):
    if month == 1 and date <= 31:
        return "True"
    elif month == 2 and leapYear(year) == "True" and date <= 29:
        return "True"
    elif month == 2 and leapYear(year) == "False" and date <= 28:
        return "True"
    elif month == 3 and date <= 31:
        return "True"
    elif month == 4 and date <= 30:
        return "True"
    elif month == 5 and date <= 31:
        return "True"
    elif month == 6 and date <= 30:
        return "True"
    elif month == 7 and date <= 31:
        return "True"
    elif month == 8 and date <= 31:
        return "True"
    elif month == 9 and date <= 30:
        return "True"
    elif month == 10 and date <= 31:
        return "True"
    elif month == 11 and date <= 30:
        return "True"
    elif month == 12 and date <= 31:
        return "True"
    else:
        return "False"

def calDayNum(month, date, year):
    if validDate(month, date, year) == "True" and month <= 2:
        day_num = 31*(month - 1)+date
        return day_num
    elif validDate(month, date, year) == "True" and month > 2 and leapYear(year) == "False":
        day_num = 31*(month-1)+date
        day_num = day_num-(4*month+23)//10
        return day_num
    elif validDate(month, date, year) == "True" and month > 2 and leapYear(year) == "True":
        day_num = (31*(month-1)+date)+1
        day_num = day_num-(4*month+23)//10
        return day_num
    else:
        return -1

main()
