#Oliver Hamilton
#10/01/2021
#Problem 20 - Factorial digit sum
import time

#Calculate sum of the digits of the factorial of a number
def sumOfFactorialDigits(n):
    #Store the part of the factorial calculated so far
    factorial = 1
    #Iterate over values from 1 up to (and including) n
    for i in range(1, n+1):
        #Multiply the current factorial by this number
        factorial *= i

    #Add the digits of the factorial
    digitSum = 0
    for digit in str(factorial):
        digitSum += int(digit)

    return digitSum

begin = time.perf_counter()

print(sumOfFactorialDigits(100))

end = time.perf_counter()
print("Time taken: {}".format(end - begin))