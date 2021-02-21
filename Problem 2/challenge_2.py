#Project Euler Challenge 2
#ohamilton79
#13/09/2020

#Every third term of the Fibonacci sequence is even

previousNum = 1
num = 1
sumOfNums = 0
count = 0

while num < 4000000:
    if (count - 1) % 3 == 0:
        sumOfNums += num

    temp = num
    num += previousNum
    previousNum = temp
    count += 1

print(sumOfNums)
