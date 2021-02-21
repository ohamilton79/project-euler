#Oliver Hamilton
#Project Euler Challenge 67 - Dynamic Programming
#01/01/2021
from copy import copy

#Read tree from text file
tree = []
with open("C:\\Users\\olive\\Documents\\Programming/Project Euler\\p067_triangle.txt", "r") as fileHandle:
    line = fileHandle.readline()
    while not line == "":
        stringsList = line.split()
        numsList = [int(numString) for numString in stringsList]
        tree.append(numsList)
        line = fileHandle.readline()

#Store previous max routes
maxRoutes = {}

#Get the score for a given route through the tree
def getScore(route):
    #print(len(route))
    totalScore = 0
    for index, node in enumerate(route):
        #print(index, node)
        score = tree[index][node]
        totalScore += score
    
    return totalScore


#Find maximum route as an array of node positions at a given level (n)
def getMaxRoute(m, n):
    global maxRoutes
    #BASE CASE
    if m == 0:
        return [0]

    elif (m, n) in maxRoutes:
        return maxRoutes[(m, n)]

    else:
        #Get the previous maximum routes
        leftRoute = None
        rightRoute = None
        if n-1 >= 0:
            leftRoute = copy(getMaxRoute(m-1, n-1))
    
        if n < m:
            rightRoute = copy(getMaxRoute(m-1, n))

        #Initialise scores for different routes
        leftScore = 0
        rightScore = 0

        #The optimal route is either to the node to the left or to the right than this
        if leftRoute:
            leftNode = leftRoute[m-1]
            if leftNode >= 0:
                leftRoute.append(n)
                leftScore = getScore(leftRoute)

        if rightRoute:
            rightNode = rightRoute[m-1]
            if rightNode <= m:
                rightRoute.append(n)
                rightScore = getScore(rightRoute)

        #If the left score is greater than the right score, return the left path
        if leftScore > rightScore:
            #Add the maximum route to the dictionary
            maxRoutes[(m, n)] = leftRoute
            return leftRoute
        #If the right score is greater than or equal to the left score, return the right path
        if rightScore >= leftScore:
            #Add the maximum route to the dictionary
            maxRoutes[(m, n)] = rightRoute
            return rightRoute

        #print(maxRoutes)

scores = []
for i in range(99):
    maxRoute = getMaxRoute(len(tree)-1, i)
    #print(len(maxRoute))
    maxScore = getScore(maxRoute)
    scores.append(maxScore)

print(max(scores))