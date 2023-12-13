import matplotlib.pyplot as plt

myMatrix = [[0.6, 0.35, 0.5, 1],
          [0.4, 0, 0, 0],
          [0, 0.65, 0, 0],
          [0, 0, 0.5, 0]]

myMatrix2 = [[0.73, 1.25, 1.25, 1.25, 0],
             [0.39, 0, 0, 0, 0],
             [0, 0.67, 0, 0, 0],
             [0, 0, 0.67, 0, 0],
             [0, 0, 0, 0.64, 0]]

myVector = [10, 0, 0, 0]

myVector2 = [10, 0, 0, 0, 0]

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




v1 = myVector2

a0 = [v1[0]]
a1 = [v1[1]]
a2 = [v1[2]]
a3 = [v1[3]]
a4 = [v1[4]]
x = [0]
count = [sumVector(v1)]
for i in range(15):
    v2 = multiplyMatrixVector(myMatrix, v1)

    a0.append(v2[0])
    a1.append(v2[1])
    a2.append(v2[2])
    a3.append(v2[3])
    a4.append(v2[4])
    
    x.append(i+1)
    count.append(sumVector(v2))
    v1 = v2

plt.plot(x, a0, label="a0")
plt.plot(x, a1, label="a1")
plt.plot(x, a2, label="a2")
plt.plot(x, a3, label="a3")
plt.plot(x, a4, label="a4")

plt.plot(x, count, label="somme des populations")
leg = plt.legend(loc='upper center')
plt.show()