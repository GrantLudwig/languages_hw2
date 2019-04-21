#hw2.py v1.0
#Grant Ludwig
#4/24/19

import sys

class BadFileFormat(Exception): pass
class ImproperDate(Exception): pass

def isLeapYear(year):
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    return False

def maxMonthDay(month, year):
    if month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    return 31

#Throws an ImproperDate exception if date is improper
def properDate(date):
    month, day, year = date
    if year < 1800:
        raise ImproperDate
    elif month < 1 or month > 12:
        raise ImproperDate
    elif day < 1 or day > maxMonthDay(month, year):
        raise ImproperDate

#returns a list in the following format:
#   [(MM, DD, YYYY), (MM, DD, YYYY), ...)]
#Throws a BadFileFormat if file is in an incorrect format
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

def genFinalDates(year):
    list = []
    for month in range(1,13):
        date = (month, maxMonthDay(month, year), year)
        list.append(date)
    return list

#Returns number of days since 1/1/1800
#Helper function for max and sorted
def daysSince(date):
    curMonth, curDay, curYear = date
    numDays = 0
    #Adds up days for years prior to current
    for year in range(1800, curYear):
        if isLeapYear(year):
            numDays += 366
        else:
            numDays += 365
    datesInYear = genFinalDates(curYear)
    #Adds up days prior to current month
    for month in range(1, curMonth):
        numDays += datesInYear[month][1]
    numDays += curDay
    return numDays

fileName = sys.argv[1]
try:
    dateList = createDateList(fileName)
except BadFileFormat:
    print("BadFileFormat exception, exiting program")
    sys.exit()
except ImproperDate:
    print("ImproperDate exception, exiting program")
    sys.exit()
except FileNotFoundError:
    print("FileNotFoundError exception, exiting program")
    sys.exit()
firstYear = dateList[0][2]
numDays = 0
for date in genFinalDates(firstYear):
    numDays += date[1]
    print(date)
print("\n")
print(numDays, "\n")
print(max(dateList, key=daysSince), "\n")
print(sorted(dateList, key=daysSince), "\n")
yearList = [date[2] for date in dateList]
print(yearList, "\n")
monthStr = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
dateStr = [monthStr[date[0] - 1] + " " + str(date[1]) + ", " + str(date[2]) for date in dateList]
print(dateStr, "\n")