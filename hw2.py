#hw2.py v1.0
#Grant Ludwig
#4/24/19

import sys

class BadFileFormat(Exception): pass

#TODO
def isLeapYear(year):
    return none

#TODO
def properDate(date):
    return none

def createDateList(fileName):
    list = []
    for line in open(fileName):
        line = line.rstrip()
        dateLine = line.split()
        #checks if 3 things on line
        if len(dateLine) != 3:
            raise BadFileFormat
        #int check
        try:
            date = (int(dateLine[0]), int(dateLine[1]), int(dateLine[2]))
            #ImproperDate
            list.append(date)
        except ValueError:
            raise BadFileFormat
    if list == []:
        raise BadFileFormat
    return list

fileName = sys.argv[1]
try:
    list = createDateList(fileName)
    print(list)
except BadFileFormat:
    print("BadFileFormat")