#Oliver Hamilton
#10/01/2021
#Challenge 19 - counting Sundays

#Check if a year is a leap year
def isLeapYear(year):
    #If this year is a century
    if year % 100 == 0:
        #The year must be divisible by 400
        if year % 400 == 0:
            return True

        else:
            return False

    #If not a century, the year must just be divisible by 4
    else:
        if year % 4 == 0:
            return True

        else:
            return False


#Get the number of days in a month
def getDaysInMonth(month, year):
    #30 days has September, April, June and November
    if month == 9 or month == 4 or month == 6 or month == 11:
        return 30

    #Feburary has 29 if a leap year...
    elif month == 2 and isLeapYear(year):
        return 29

    #...Otherwise it has 28
    elif month == 2 and not isLeapYear(year):
        return 28

    #Any other month has 31
    else:
        return 31

#Get the date given the number of days after 1st Jan 1900
def getDate(days):
    #Days remaining to be accounted for
    daysRemaining = days
    #Count the year, month, and day
    year = 1900
    month = 1
    day = 1

    #1900 is not a leap year
    daysInYear = 365

    #While there are more years to count
    while daysInYear <= daysRemaining:
        #Subtract the days and increment the year
        daysRemaining -= daysInYear
        year += 1

        #If a leap year, days in year are 366 instead of 365
        if isLeapYear(year):
            daysInYear = 366
        else:
            daysInYear = 365

    #January has 31 days
    daysInMonth = 31
    #While there are more months to count
    while daysInMonth <= daysRemaining:
        #Subtract the days and increment the month
        daysRemaining -= daysInMonth
        month += 1

        #Calculate the number of days in this next month
        daysInMonth = getDaysInMonth(month, year)

    #Add any remaining days to the day counter
    day += daysRemaining

    #Return the date as a tuple
    return (year, month, day)

#Count the number of Sundays that fall of the first of the month
sundays = 0

#The first Sunday after 1 Jan 1900 is 7th Jan 1900
days = 6

date = getDate(days)

#Keep adding 7 to get successive Sundays whilst the year 2001 hasn't been reached
while date[0] < 2001:
    days += 7
    date = getDate(days)

    print(date)

    #If the date is the first of the month and the year is greater than (or equal to) 1901, increment the counter
    if date[2] == 1 and date[0] >= 1901:
        sundays += 1


print(sundays)


