#Project Euler Challenge 3 Improved
#ohamilton79
#13/09/2020
import math

def isPrime(num):
    #Check if it's divisble by common numbers first, like 2, 4, 6, 8... and 3, 6, 9, 12...
    if num % 2 == 0:
        return False

    elif num % 3 == 0:
        return False

    elif num % 5 == 0:
        return False

    elif num % 7 == 0:
        return False

    #Otherwise it isn't a common number, so use brute force
    for x in range(11, int(num**0.5)+2):
        if num % x == 0:
            return False

    #Otherwise the number is prime
    return True


bigNum = 600851475143
largestPrime = 0

for i in range(2, int(bigNum**0.5)+2):
    if isPrime(i) and bigNum % i == 0 and i > largestPrime:
        largestPrime = i

print(largestPrime)
    
