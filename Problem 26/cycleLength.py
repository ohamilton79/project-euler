#Get the length of the recurring cycle when 1 is divided by n
def getCycle(n):
    #Stores the positions at which different remainder occur
    remainders = {}
    currentPos = 0
    cycleFound = False
    cycleLength = -1
    newRemainder = 1

    while not cycleFound and currentPos < n:
        previousRemainder = newRemainder
        newRemainder = (10 * previousRemainder) % n

        #If remainder occurred previously
        if newRemainder in remainders:
            #Cycle has been found
            cycleFound = True

        #If remainder hasn't been seen before, store for future reference
        else:
            remainders[newRemainder] = currentPos
            cycleLength = currentPos + 1

        #Calculate next digit in decimal expansion
        currentPos += 1

    #Return the length of the cycle, or -1 if there isn't one
    return cycleLength
