#ohamilton79
#Challenge 21 - amicable numbers
#09/02/2021
import math

#Get the integers that divide a number
def getProperDivisors(n):
    divisors = []
    for i in range(1, math.ceil(math.sqrt(n))):
        #If the number divides n, it and the other factor are both proper divisors
        if n % i == 0:
            divisors.append(i)
            if i != 1:
                divisors.append(n // i)

    #Return all the proper divisors of n
    return divisors

print(sum(getProperDivisors(5)))

#Get the amicable pairs less than n
def getAmicableNumbers(n):
    amicableNumbers = []
    for a in range(1, n):
        #Look for an amicable pair
        firstInPair = sum(getProperDivisors(a))
        secondInPair = sum(getProperDivisors(firstInPair))

        if a == secondInPair and a != firstInPair and a not in amicableNumbers:
            #Each number in the amicable pair is an amicable number
            amicableNumbers.append(a)
            if firstInPair < n:
                amicableNumbers.append(firstInPair)

    print(amicableNumbers)

    #Return the list of amicable numbers
    return amicableNumbers

#Get the sum of all amicable numbers under 10000
print(sum(getAmicableNumbers(10000)))

print(sum(getProperDivisors(284)))
            

