#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 14:09:41 2023

@author: t21204574
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import gen_matrice as k

#on défini notre matrice et notre vecteur
matrix1 = np.array([[0.6,0.35,0.5,1],
                    [0.4,0,0,0],
                    [0,0.65,0,0],
                    [0,0,0.5,0]])



matrix2 = np.array([[0.73, 1.25, 1.25, 1.25, 0],
             [0.39, 0, 0, 0, 0],
             [0, 0.67, 0, 0, 0],
             [0, 0, 0.67, 0, 0],
             [0, 0, 0, 0.64, 0]])

vector = np.array([5,3,3,2])


def grap_without_animation(Mat,Vec):
    
    t = Mat
    v = Vec
    
    a0 = [v[0]]
    a1= [v[1]]
    a2= [v[2]]
    a3 =[v[3]]
    
    for i in range(30):
        #on multiplie la matrice par le vecteur pour obtenir la multiplication de la matrice fois le vecteur
        vect = np.dot(t,v)
        v = vect
        y = 10
        #chaque a correspondent respectivement à l'indice du vecteur obtenur
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
        

def graph_with_animation1(matrix,vector):
        
        mat = np.array(matrix)
        print(mat)

    
        #on défini notre graphe ou chaque ligne correspond à un vecteur pour l'instant vide
        fig, ax = plt.subplots()
        ligne, = ax.plot([], [], '-', label='a0')
        ligne1, = ax.plot([], [], '-', label='a1')
        ligne2, = ax.plot([], [], '-', label='a2')
        ligne3, = ax.plot([], [], '-', label='a3')
        

        def init():
            #on limite notre graphe
            ax.set_xlim(0, 30)
            ax.set_ylim(0, 30)
            ax.legend()
            return ligne, ligne1, ligne2, ligne3

        def update(frame):
            
            global vector
            #On va multiplier la matrice par le cecteur tant que update et appeler
            vect = np.dot(mat, vector)
            vector = vect
            print(round(np.sum(vect),2))
            a0.append(vect[0])
            a1.append(vect[1])
            a2.append(vect[2])
            a3.append(vect[3])
            #on met a jour els ligne qui coresspondent respectivement a a0,a1,a2,a3
            ligne.set_data(range(frame + 2), a0[:frame + 2])
            ligne1.set_data(range(frame + 2), a1[:frame + 2])
            ligne2.set_data(range(frame + 2), a2[:frame + 2])
            ligne3.set_data(range(frame + 2), a3[:frame + 2])
            return ligne, ligne1, ligne2, ligne3

        #on donne le point de départ de nos vecteur
        a0 = [vector[0]]
        a1 = [vector[1]]
        a2 = [vector[2]]
        a3 = [vector[3]]


        #on lance l'animation en appelant update 20 fois
        ani = FuncAnimation(fig, update, frames=20, init_func=init, blit=True)
        

        plt.title("évolution d'une population modéle académique")
        plt.show()

   

graph_with_animation1(k.genMatricColEqual(4,1.2),vector)
#graph_with_animation1(k.genMatricLineEqual(4,2),vector)
# graph_with_animation1(k.genMatricDiagEqual(4,2,0),vector)
#grap_without_animation(matrice,vector)


