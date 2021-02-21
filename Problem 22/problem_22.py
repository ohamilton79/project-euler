#ohamilton79
#Problem 22 - Names scores
#14/02/2021

#Read the names from the names.txt file into an array
def readNames():
    with open("p022_names.txt", "r") as fileHandle:
        namesArray = [name[1:-1] for name in fileHandle.read().split(",")]

    return namesArray

totalScore = 0

names = readNames()
names.sort()
#Iterate over each name, and track its index in the array
for index, name in enumerate(names):
    #Calculate the score by calculating the sum of the character codes
    score = sum([ord(char) - 64 for char in name])

    #Multiply by array position, then add to total score
    totalScore += (score * (index + 1))

print(totalScore)

print(ord("A"))
