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

#graphique intéressant pour adapter à l'évolution du vecteur a des temps différent

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 2), ylim=(0, 10))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    x = np.linspace(0, 2, 1000)
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    line.set_data(x, y)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=200, interval=20, blit=True)


anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()