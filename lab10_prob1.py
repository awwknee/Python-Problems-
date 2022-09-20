"""
CISC 131 Problem 1 - Ani Lamichhane (lami5034)
"""

def readCsv(filename):
    file_ref = open(filename, 'r')
    dataname = file_ref.readline()
    dataname = dataname.strip()
    dataname = dataname.split(",")

    nextline = file_ref.readline()

    listmydict = []

    while nextline != "":
        mydict = {}
        nextline = nextline.strip()
        nextline = nextline.split(",")

        for i in range(len(dataname)):
            mydict[dataname[i]] = nextline[i]

        nextline = file_ref.readline()
        listmydict.append(mydict)

    file_ref.close()

    return listmydict

def filterOverallGpa(applicants, top_n):
    for i in range(len(applicants) - 1):
        for j in range(i + 1, len(applicants)):
            if applicants[j]['overall_gpa'] > applicants[i]['overall_gpa']:
                tmp = applicants[i]
                applicants[i] = applicants[j]
                applicants[j] = tmp

    overallgpalist = []
    for i in range(top_n):
        overallgpalist.append(applicants[i])

    return overallgpalist

def filterMajorGpa(applicants, top_n):
    for i in range(len(applicants) - 1):
        for j in range(i + 1, len(applicants)):
            if applicants[j]['major_gpa'] > applicants[i]['major_gpa']:
                tmp = applicants[i]
                applicants[i] = applicants[j]
                applicants[j] = tmp

    majorgpalist = []
    for i in range(top_n):
        majorgpalist.append(applicants[i])

    return majorgpalist

def filterCustomScore(applicants, top_n):
    for i in range(len(applicants)):
        cusscore = (10 * float(applicants[i]['advanced_gpa'])) + \
            (8 * float(applicants[i]['intermediate_gpa'])) + \
            (6 * float(applicants[i]['intro_gpa'])) + \
            (4 * float(applicants[i]['overall_gpa'])) + \
            (0.25 * float(applicants[i]['years_experience']))
        applicants[i]['score'] = cusscore

    for i in range(len(applicants) - 1):
        for j in range(i + 1, len(applicants)):
            if applicants[j]['score'] > applicants[i]['score']:
                tmp = applicants[i]
                applicants[i] = applicants[j]
                applicants[j] = tmp

    customscorelist = []
    for i in range(top_n):
        customscorelist.append(applicants[i])

    return customscorelist

def main():
    applicants = readCsv("applicants.csv")

    myfilter = input("What filter: ")

    if myfilter == "1":
        overallgpalist = filterOverallGpa(applicants, 10)
        for i in range(len(overallgpalist)):
            print("{} {} ({}, {}): Overall GPA = {}, Major GPA = {}, {} Years Experience"\
                .format(overallgpalist[i]['fname'], \
                overallgpalist[i]['lname'], overallgpalist[i]['gender'], \
                overallgpalist[i]['age'], overallgpalist[i]['overall_gpa'], \
                overallgpalist[i]['major_gpa'], overallgpalist[i]['years_experience']))
    elif myfilter == "2":
        majorgpalist = filterMajorGpa(applicants, 10)
        for i in range(len(majorgpalist)):
            print("{} {} ({}, {}): Overall GPA = {}, Major GPA = {}, {} Years Experience"\
                .format(majorgpalist[i]['fname'], majorgpalist[i]['lname'],\
                     majorgpalist[i]['gender'], majorgpalist[i]['age'], \
                         majorgpalist[i]['overall_gpa'], majorgpalist[i]['major_gpa'], \
                             majorgpalist[i]['years_experience']))
    elif myfilter == "3":
        customscorelist = filterCustomScore(applicants, 10)
        for i in range(len(customscorelist)):
            print("{} {} ({}, {}): Overall GPA = {}, Major GPA = {}, {} Years Experience\
                 (Score = {:.1f})".format(customscorelist[i]['fname'], \
                customscorelist[i]['lname'], customscorelist[i]['gender'], \
                customscorelist[i]['age'], \
                customscorelist[i]['overall_gpa'], customscorelist[i]['major_gpa'], \
                customscorelist[i]['years_experience'], customscorelist[i]['score']))

main()
