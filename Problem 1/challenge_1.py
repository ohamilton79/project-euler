#Project Euler Challenge 1
#ohamilton79
#13/05/2020

#Find sum of multiples of 3 below 1000
sumOfMultiples = 0
multipleOf3 = 0
multipleOf5 = 0
multipleOf15 = 0
while multipleOf3 < 997:
    multipleOf3 += 3

    sumOfMultiples += multipleOf3

    print(multipleOf3, sumOfMultiples)

#Find sum of multiples of 5 below 1000
while multipleOf5 < 995:
    multipleOf5 += 5

    sumOfMultiples += multipleOf5

    print(multipleOf5, sumOfMultiples)

#Subtract multiples of 15 below 1000
while multipleOf15 < 985:
    multipleOf15 += 15

    sumOfMultiples -= multipleOf15

    print(multipleOf15, sumOfMultiples)
