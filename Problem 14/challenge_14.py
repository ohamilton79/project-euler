#Oliver Hamilton
#Challenge 14
#23/12/2020
import numpy as np

#Stores already found chain lengths for numbers
chainLengths = {}

#test = np.array([0, 0, 5, 0])
#print(np.nonzero(test))
nums = np.array(range(1, 1000000), dtype=np.longlong)
collatzNums = np.array(range(1, 1000000), dtype=np.longlong)
count = 1
while len(np.nonzero(newCollatzNums - 1)[0]) != 1:
    collatzNums = newCollatzNums
    oddMask = (collatzNums != 1) & (collatzNums % 2 != 0)
    evenMask = (collatzNums != 1) & (collatzNums % 2 == 0)
    newLength = len(np.nonzero(oddMask[0])) + len(np.nonzero(evenMask[0]))
    newCollatzNums = np.array(range(newLength))
    newCollatzNums[oddMask] = (collatzNums[oddMask] * 3) + 1
    newCollatzNums[evenMask] = (collatzNums[evenMask]) / 2
    count += 1

#Get the final remaining number (with the longest chain length)
startingNum = nums[np.nonzero(collatzNums - 1)[0][0]]

#Continue to get final chain length
while len(np.nonzero(collatzNums - 1)[0]) != 0:
    oddMask = (collatzNums != 1) & (collatzNums % 2 != 0)
    evenMask = (collatzNums != 1) & (collatzNums % 2 == 0)
    collatzNums[oddMask] = (collatzNums[oddMask] * 3) + 1
    collatzNums[evenMask] = (collatzNums[evenMask]) / 2
    count += 1

print("{} has a Collatz chain length of {}".format(startingNum, count))
