#Oliver Hamilton
#Project Euler Challenge 18 - Dynamic Programming
#29/12/2020
from copy import copy

#Store tree as 2D array
tree = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]

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
    #BASE CASE
    if m == 0:
        return [0]

    else:
        #Get the previous maximum routes
        leftRoute = None
        rightRoute = None
        if n-1 >= 0:
            leftRoute = getMaxRoute(m-1, n-1)
    
        if n < m:
            rightRoute = getMaxRoute(m-1, n)

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
            return leftRoute
        #If the right score is greater than the left score, return the right path
        if rightScore > leftScore:
            return rightRoute

scores = []
for i in range(15):
    maxRoute = getMaxRoute(len(tree)-1, i)
    maxScore = getScore(maxRoute)
    scores.append(maxScore)

print(max(scores))