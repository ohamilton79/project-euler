#Oliver Hamilton
#Project Euler - Problem 11
#21/12/2020

#Get the greatest product of n adjacent numbers
def greatestAdjacentProduct(anArray, n):
    #Get array size
    width = len(anArray)
    height = len(anArray[0])

    #Stores the maximum product found so far
    maxProduct = 0

    #List of directions to check
    vecsToCheck = [(1, 0), (0, 1), (1, 1), (1, -1)]

    #Check all numbers in array
    for i in range(width):
        for j in range(height):
            for vec in vecsToCheck:
                currentProduct = 1
                for x in range(n):
                    #Calculate new position of number
                    newPos = (i + vec[0]*x, j + vec[1]*x)
                    try:
                        #Update product of numbers in direction specified by vector
                        currentProduct *= anArray[newPos[0]][newPos[1]]
                    except:
                        break

                #If this product is greater than the maximum, update the maximum
                if currentProduct > maxProduct:
                    maxProduct = currentProduct

    #Return the greatest product found
    return maxProduct

myArr = [
    [8, 49, 81, 52, 22, 24, 32, 67, 24, 21, 78, 16, 86, 19, 4, 88, 4, 20, 20, 1],
    [2, 49, 49, 70, 31, 47, 98, 26, 55, 36, 17, 39, 56, 80, 52, 36, 42, 69, 73, 70],
    [22, 99, 31, 95, 16, 32, 81, 20, 58, 23, 53, 5, 0, 81, 8, 68, 16, 36, 35, 54],
    [97, 40, 73, 23, 71, 60, 28, 68, 5, 9, 28, 42, 48, 68, 83, 87, 73, 41, 29, 71],
    [38, 17, 55, 4, 51, 99, 64, 2, 66, 75, 22, 96, 35, 5, 97, 57, 38, 72, 78, 83],
    [15, 81, 79, 60, 67, 3, 23, 62, 73, 00, 75, 35, 71, 94, 35, 62, 25, 30, 31, 51],
    [00, 18, 14, 11, 63, 45, 67, 12, 99, 76, 31, 31, 89, 47, 99, 20, 39, 23, 90, 54],
    [40, 57, 29, 42, 89, 2, 10, 20, 26, 44, 67, 47, 7, 69, 16, 72, 11, 88, 1, 69],
    [00, 60, 93, 69, 41, 44, 26, 95, 97, 20, 15, 55, 5, 28, 7, 3, 24, 34, 74, 16],
    [75, 87, 71, 24, 92, 75, 38, 63, 17, 45, 94, 58, 44, 73, 97, 46, 94, 62, 31, 92],
    [4, 17, 40, 68, 36, 33, 40, 94, 78, 35, 3, 88, 44, 92, 57, 33, 72, 99, 49, 33],
    [5, 40, 67, 56, 54, 53, 67, 39, 78, 14, 80, 24, 37, 13, 32, 67, 18, 69, 71, 48],
    [7, 98, 53, 1, 22, 78, 59, 63, 96, 0, 4, 0, 44, 86, 16, 46, 8, 82, 48, 61],
    [78, 43, 88, 32, 40, 36, 54, 8, 83, 61, 62, 17, 60, 52, 26, 55, 46, 67, 86, 43],
    [52, 69, 30, 56, 40, 84, 70, 40, 14, 33, 16, 54, 21, 17, 26, 12, 29, 59, 81, 52],
    [12, 48, 3, 71, 28, 20, 66, 91, 88, 97, 14, 24, 58, 77, 79, 32, 32, 85, 16, 1],
    [50, 4, 49, 37, 66, 35, 18, 66, 34, 34, 9, 36, 51, 4, 33, 63, 40, 74, 23, 89],
    [77, 56, 13, 2, 33, 17, 38, 49, 89, 31, 53, 29, 54, 89, 29, 93, 52, 4, 57, 19],
    [91, 62, 36, 36, 13, 12, 64, 94, 63, 33, 56, 85, 17, 55, 98, 53, 76, 36, 5, 67],
    [8, 0, 65, 91, 80, 50, 70, 21, 72, 95, 92, 57, 58, 40, 66, 69, 36, 16, 54, 48]
        ]

print(greatestAdjacentProduct(myArr, 4))

