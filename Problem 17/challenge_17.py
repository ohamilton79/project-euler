#Oliver Hamilton
#Challenge 17 - Number letter counts
#27/12/2020

#CONSTANTS

#Mapping from numbers less than 20 to character counts
unitsMapping = {'1': 'one',
                '2': 'two',
                '3': 'three',
                '4': 'four',
                '5': 'five',
                '6': 'six',
                '7': 'seven',
                '8': 'eight',
                '9': 'nine',
                '10': 'ten',
                '11': 'eleven',
                '12': 'twelve',
                '13': 'thirteen',
                '14': 'fourteen',
                '15': 'fifteen',
                '16': 'sixteen',
                '17': 'seventeen',
                '18': 'eighteen',
                '19': 'nineteen'
                }
#Mapping from tens (20, 30, 40, ...) to character counts
tensMapping = {'2': 'twenty',
               '3': 'thirty',
               '4': 'forty',
               '5': 'fifty',
               '6': 'sixty',
               '7': 'seventy',
               '8': 'eighty',
               '9': 'ninety'
               }

def getCharCount(num):
    global unitsMapping
    global tensMapping

    if int(num) == 0:
        return ""

    #For thousands
    if len(num) >= 4:
        thousandsDigit = num[0]
        hundredsDigit = num[1]
        tensDigit = num[2]
        unitsDigit = num[3]

        #If the hundreds are non-zero, the 'and' doesn't need to be included
        if hundredsDigit != '0':
            return getCharCount(thousandsDigit) + 'thousand' + getCharCount(hundredsDigit + tensDigit + unitsDigit)

        #If one of the units and tens digits are non-zero, the 'and' must be included
        elif tensDigit != '0' or unitsDigit != '0':
            return getCharCount(thousandsDigit) + 'thousand' + 'and' + getCharCount(tensDigit + unitsDigit)

        #If the hundreds, tens, and units are all zero, the 'and' doesn't need to be included to be included
        else:
            return getCharCount(thousandsDigit) + 'thousand'

    #For hundreds
    elif len(num) >= 3:
        hundredsDigit = num[0]
        tensDigit = num[1]
        unitsDigit = num[2]

        #If both tens digit and units digit are 0, don't include the 'and'
        if tensDigit == '0' and unitsDigit == '0':
            return getCharCount(hundredsDigit) + 'hundred'

        else:
            return getCharCount(hundredsDigit) + 'hundred' + 'and' + getCharCount(tensDigit + unitsDigit)

    #For tens
    elif int(num) >= 20:
        tensDigit = num[0]
        unitsDigit = num[1]

        return tensMapping[tensDigit] + getCharCount(unitsDigit)

    #For units / teens              
    elif int(num) < 20:

        #If the tens digit is 0, return only the value of the units digit
        if num[0] == '0':
            return unitsMapping[num[1]]

        else:
            return unitsMapping[num]



#Number of letters used in sequence of numbers
letterCount = 0

#Iterate over integers from 1 to 1000 (inclusive)
for i in range(1, 1001):
    #Convert number to string
    currentNum = str(i)
    print(getCharCount(currentNum))
    letterCount += len(getCharCount(currentNum))

print(letterCount)

