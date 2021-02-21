import math
#from itertools import combinations

abundantNumsDict = {}

#Return a list of the proper divisors of n
def getProperDivisors(n):
    divisors = []
    for i in range(1, int(math.floor(n ** 0.5))+1):
        #Add any numbers that have remainder 0 when divided into n
        if not i in divisors and n % i == 0:
            divisors.append(i)
            
            #The other factor is also a divisor (if it isn't equal to n)
            if not (n // i) in divisors and i != 1 and n % i == 0:
                divisors.append(n // i)

    return divisors


            
#Check if the number is abundant
"""def getAbundantNums(n):
    abundantNums = []
    for i in range(1, n+1):
        if i in abundantNumsDict and abundantNumsDict[i] == True:
            abundantNums.append(i)
            
        #If the sum of i's proper divisors is more than i, it is abundant
        elif sum(getProperDivisors(i)) > i:
            abundantNums.append(i)

            #Add to dictionary for future reference
            abundantNumsDict[i] = True

    return abundantNums"""

def isAbundant(n):
    if sum(getProperDivisors(n)) > n:
        return True

    else:
        return False

#print(isAbundant(13))
#print(isAbundant(124))

#Return a list of the numbers less than or equal to n that cannot be written as the sum of two abundant numbers
def notSumOfAbundants(n):
    abundantsList = [False]*(n+1)
    results = []
    testSum = 0
    #print(i)

    for i in range(1, n+1):
        if isAbundant(i):
            abundantsList[i] = True

        #else:
            #abundantsList[i] = False

    for i in range(1, n+1):
        #print("Current number: {}".format(i))
        #print("Not sum of abundants: {}".format(results))
        
        sumOfAbundants = False
        for index in range(i):
            #print(i - index)
            #print(index)
            if i >= index and abundantsList[index] == True and abundantsList[i - index] == True:
                #print("{} and {} sum to give {}".format(i - index, index, i))
                #print(i)
                sumOfAbundants = True
                break

        if not sumOfAbundants:
            results.append(i)
            #print(i)
            testSum += i
            #print(results)

    #print(max(results))

    return testSum
    


#print(getProperDivisors(28))
#print(getAbundantNums(24))
#print(abundantNumsDict)

print(notSumOfAbundants(30000))
        
