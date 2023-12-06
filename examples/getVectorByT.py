import numpy as np

myMatrix = [[0.6, 0.35, 0.5, 1],
          [0.4, 0, 0, 0],
          [0, 0.65, 0, 0],
          [0, 0, 0.5, 0]]

myVector = [10, 0, 0, 0]

myMatrix = np.array(myMatrix)
myVector = np.array(myVector)

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

def getVectorByTdoingLoop(myMatrix, myVector, t):
    v1 = myVector
    for i in range(t):
        v2 = np.matmul(myMatrix, v1)
        v1 = v2
    return v2

def getVectorByT(myMatrix, myVector, t):
    updatedMatrix = np.linalg.matrix_power(myMatrix, t)
    resultVector = np.matmul(updatedMatrix, myVector)
    return resultVector

def getEigenvalue(myMatrix, tol=0.0001):
    myVector = np.random.normal(size=myMatrix.shape[1])
    myVector = myVector / np.linalg.norm(myVector)
    previous = np.empty(shape=myMatrix.shape[1])
    while True:
        previous[:] = myVector
        myVector = myMatrix @ myVector
        myVector = myVector / np.linalg.norm(myVector)
        if np.allclose(myVector, previous, atol=tol):
            break
    return myVector

print(getEigenvalue(myMatrix))
# v1 = myVector
# for i in range(1,4):
#     v2= np.matmul(myMatrix, v1)
#     vUpdate = getVectorByT(myMatrix, myVector, i)
#     print(v2)
#     print(vUpdate)
#     print()
#     v1 = v2

