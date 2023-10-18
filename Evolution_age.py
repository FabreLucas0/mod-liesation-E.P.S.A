#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:09:41 2023

@author: t21204574
"""

import numpy as np
import matplotlib.pyplot as plt

#%%
matrice = np.array([[0.6,0.35,0.5,1],[0.4,0,0,0],[0,0.65,0,0],[0,0,0.5,0]])

vector = np.array([10,0,0,0])

def temp (Mat,Vec):
    
    t = Mat
    v = Vec
    
    a0 = [v[0]]
    a1= [v[1]]
    a2= [v[2]]
    a3 =[v[3]]
    
    for i in range(30):
        
        vect = np.dot(t,v)
        print(vect)
        v = vect
        y = 10
        a0.append(v[0])
        a1.append(v[1])
        a2.append(v[2])
        a3.append(v[3])
        
     
        plt.plot(a0,'red')
        plt.plot(a1,'green')
        plt.plot(a2,'blue')
        plt.plot(a3,'yellow')
        
        
        plt.plot(y)
        plt.show()      
        
   

print(temp(matrice,vector))
#%%

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import rc

fig = plt.figure(1)
plt.axis([0,2*np.pi,-1,1])

N = 40                     

x = np.linspace(0,2*np.pi,100)  

liste_images = []           

for i in range(N):
    im = plt.plot(x,np.sin(x-i*(2*np.pi)/N),'b')
    liste_images.append(im)



anim = animation.ArtistAnimation(fig, liste_images, interval=150, repeat_delay=1000)



rc('animation', html='jshtml')
anim
