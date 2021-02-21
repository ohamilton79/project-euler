#Project Euler Challenge 3
#ohamilton79
#13/09/2020

#Find the prime factors of the number 600851475143
targetNum = 600851475143

searchList = list(range(1, 775147))

counter = 1
#Stores the largest prime factor found so far
largestPrime = 0

while(counter < len(searchList)):
    currentNum = searchList[counter]
    #print(currentNum)

    #Set this as the largest prime if it divides the number
    if (targetNum % currentNum == 0 and currentNum > largestPrime):
        largestPrime = currentNum

    #Remove all multiples of this from the search list
    multiplier = 2
    result = currentNum * multiplier

    while result <= searchList[len(searchList)-1]:
        if result in searchList:
            searchList.remove(result)
        multiplier += 1
        result = currentNum * multiplier
        print(result)

    #Increment the counter
    counter += 1

    #print(counter)


print(largestPrime)
        
    
    


    
