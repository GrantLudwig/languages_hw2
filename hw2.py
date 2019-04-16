#hw2.py v1.0
#Grant Ludwig
#4/24/19

import sys

class BadFileFormat(Exception): pass
class ImproperDate(Exception): pass

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 4 != 0:
        return true
    return False

#TODO
def properDate(date):
    month, day, year = date
    if year < 1800:
        raise ImproperDate
    elif month < 1 or month > 12:
        raise ImproperDate
    elif day < 1 or day > 31:
        raise ImproperDate
    elif day > 30:
        if month == 4 or month == 6 or month == 9 or month == 11:
            raise ImproperDate
    elif month == 2:
        if isLeapYear(year):
            if day > 29:
                raise ImproperDate
        else:
            if day > 28:
                raise ImproperDate

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
            properDate(date)
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
except ImproperDate:
    print("ImproperDate")