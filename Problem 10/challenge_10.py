#Oliver Hamilton
#Challenge 10 - Sieve of Eratosthenes
#20/12/2020

# Find the sum of the primes up to 2,000,000

#Find a list of prime numbers up (and including) to n
def getPrimeNumbers(n):
    #A list of Boolean values, where the third represents 2 and the second to last n
    primeList = [True]*(n+1)

    #Iterate over each number in the list (from 2 to n)
    for i in range(2, n+1):
        #If this number is prime, mark multiples as composite (starting from i^2)
        if primeList[i]:
            for j in range(i**2, n+1, i):
                primeList[j] = False

    return primeList

def addPrimes(primeList):
    #Track the sum of the prime numbers
    sumOfPrimes = 0
    for i in range(2, len(primeList)):
        if primeList[i]:
            #Add to the sum of the primes
            sumOfPrimes += i

    return sumOfPrimes

print(addPrimes(getPrimeNumbers(2000000)))
            
            
