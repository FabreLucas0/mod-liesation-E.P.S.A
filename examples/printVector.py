myMatrix = [[0.6, 0.35, 0.5, 1],
          [0.4, 0, 0, 0],
          [0, 0.65, 0, 0],
          [0, 0, 0.5, 0]]

# myMatrix2 = [[0.73, 1.25, 1.25, 1.25, 0],
#              [0.39, 0, 0, 0, 0],
#              [0, 0.67, 0, 0, 0],
#              [0, 0, 0.67, 0, 0],
#              [0, 0, 0, 0.64, 0]]

myMatrix1_1 = [[0.25, 0.4, 0.2, 1],
               [0.25, 0.025, 0.1, 0],
               [0.25, 0.375, 0, 0],
               [0.25, 0.2, 0.7, 0]]

myMatrix1_2 = [[0.25, 0.25, 0.25, 0.25],
               [0.4, 0.025, 0.375, 0.2],
               [0.2, 0.1, 0.7, 0],
               [1, 0, 0, 0]]

myMatrix1_3 = [[0.25, 0.25, 0.25, 0.25],
               [0.25, 0.25, 0.25, 0.25],
               [0.25, 0.25, 0.25, 0.25],
               [0.25, 0.25, 0.25, 0.25]]

myMatrix1_4 = [[1, 0, 0, 0],
               [0, 1, 0, 0],
               [0, 0, 1, 0],
               [0, 0, 0, 1]]

myVector = [10, 0, 0, 0]
# myVector2 = [10, 0, 0, 0, 0]

def multiplyMatrixVector(myMatrix, myVector):
    resultVector = [0]*len(myVector)
    for i in range(len(myMatrix)):
        result = 0
        for j in range(len(myMatrix[i])):
            result += myMatrix[i][j] * myVector[j]
        resultVector[i] = result
    return resultVector

def sumVector(myVector):
    result = 0
    for i in range(len(myVector)):
        result += myVector[i]
    return result

v1 = myVector
for i in range(10):
    v2 = multiplyMatrixVector(myMatrix1_4, v1)
    print(v2)
    print(sumVector(v2))
    v1 = v2