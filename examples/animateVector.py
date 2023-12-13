import matplotlib as matplotlib
import matplotlib.animation as animation


aTest = [0]
aTest1 = [0]
aTest2 = [0]
aTest3 = [0]
aTest4 = [0]

v1 = myVector2
fig = plt.figure(1)
N = 30   
plt.axis([0,N,0,900])
 
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

