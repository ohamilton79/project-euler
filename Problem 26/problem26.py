from cycleLength import getCycle

#Find the decimal with the longest recurring cycle for unit fractions greater than 1/n
def longestRecurringCycle(n):
    #Track the longest cycle so far and the denominator of that fraction
    longestCycle = (None, 0)
    for i in range(2, n):
        #Update the longest cycle
        newCycleLength = getCycle(i)
        if newCycleLength > longestCycle[1]:
            longestCycle = (i, newCycleLength)

    return longestCycle

print(longestRecurringCycle(1000))
