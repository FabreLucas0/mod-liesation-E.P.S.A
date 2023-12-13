import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

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




# v1 = myVector2

# aVector = []
# for i in range (5):
#     aVector.append([v1[i]])
# x = [0]
# count = [sumVector(v1)]
# for i in range(15):
#     v2 = multiplyMatrixVector(myMatrix2, v1)

    # for j in range (5):
    #     aVector[j].append(v2[j])
    
#     x.append(i+1)
#     count.append(sumVector(v2))
#     v1 = v2

# for i in range(5):
#     plt.plot(x, aVector[i], label="a"+str(i))

# plt.plot(x, count, label="somme des populations")
# leg = plt.legend(loc='upper center')
# plt.show()

aTest = [0]
aTest1 = [0]
aTest2 = [0]
aTest3 = [0]
aTest4 = [0]

v1 = myVector2
fig = plt.figure(1)
N = 45 
plt.axis([0,N,0,100000])
 
x = [0]

liste_images = [] 
liste_images1 = [] 
liste_images2 = [] 
liste_images3 = [] 
liste_images4 = [] 

for i in range(N):
    v2 = multiplyMatrixVector(myMatrix2, v1)
    im = plt.plot(x,aTest,'b')
    im1 = plt.plot(x, aTest1,'c')
    im2 = plt.plot(x, aTest2,'y')
    im3 = plt.plot(x, aTest3,'r')
    im4 = plt.plot(x, aTest4,'g')
    aTest.append(v2[0])
    aTest1.append(v2[1])
    aTest2.append(v2[2])
    aTest3.append(v2[3])
    aTest4.append(v2[4])
    x.append(i)
    liste_images.append(im)
    liste_images1.append(im1)
    liste_images2.append(im2)
    liste_images3.append(im3)
    liste_images4.append(im4)
    v1 = v2

anim = animation.ArtistAnimation(fig, liste_images, interval=150, repeat_delay=1000)
anim1 = animation.ArtistAnimation(fig, liste_images1,interval=150, repeat_delay=1000)
anim2 = animation.ArtistAnimation(fig, liste_images2,interval=150, repeat_delay=1000)
anim3 = animation.ArtistAnimation(fig, liste_images3,interval=150, repeat_delay=1000)
anim4 = animation.ArtistAnimation(fig, liste_images4,interval=150, repeat_delay=1000)

rc('animation', html='jshtml')
#anim
plt.show()