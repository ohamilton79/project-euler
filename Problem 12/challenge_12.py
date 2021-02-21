#Oliver Hamilton
#Project Euler - Challenge 12
#21/12/2020

#Test a number for divisbility by numbers less than or equal to it
def getDivisors(n):
    #Counter for the number of divisors
    divisorsCount = 0
    for i in range(1, int(n ** 0.5)+1):
        #Test if the number is divisble by the smaller number
        if n % i == 0:
            if n/i == i:
                divisorsCount += 1

            else:
                divisorsCount += 2

    #Return the number of divisors that the number input has
    return divisorsCount

#Get the nth triangle number
def getTriangleNum(n):
    #Sum of natural numbers up to and including n = n(n+1) / 2
    triangleNum = int(n * (n+1) / 2)

    return triangleNum

#Find the first triangle number to have 500 divisors
targetDivisors = 500

#Number of divisors of current number
nOfDivisors = 0

#Current sequence number of triangle number found
sequenceNum = 0

triangleNum = 0

while nOfDivisors < targetDivisors:
    sequenceNum += 1
    triangleNum = triangleNum + sequenceNum

    nOfDivisors = getDivisors(triangleNum)

print(triangleNum)
