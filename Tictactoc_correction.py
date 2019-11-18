# -*- coding: utf-8 -*-
"""
Created on Fri May 01 18:03:46 2015

@author: Laïta
"""

import numpy as np
import matplotlib.pyplot as plt

# Creation de la grille
def creer_grille():
    for i in range (4):
        a=[0,3]
        b=[i,i]
        plt.plot(a,b)
        plt.plot(b,a)
    
        
        
def croix (i,j):
    a=[i+(1/4),i+(3/4)]
    b=[j+(1/4),j+(3/4)]
    c=[j+(3/4),j+(1/4)]
    plt.plot(a,b)
    plt.plot(a,c)
    

def rond (i,j):
    t=np.linspace(0,2*np.pi,200)
    x=(i/2)+(1/4)*np.cos(t)
    y=(i/2)+(1/4)*np.sin(t)
    plt.plot(x,y)
    
    
def a_gagne (i,T):
    res=False
    for k in range (3):
        if T[k,0]==i and T[k,1]==i and T[k,2]==i:
            res=True
        elif T[0,k]==i and T[1,k]==i and T[2,k]==i:
            res=True
        elif T[0,0]==i and T[1,1]==i and T[2,2]==i:
            res=True
        elif T[0,2]==i and T[1,1]==i and T[2,0]==i:
            res=True
    return res
    
    
def jeu_duo():
    import numpy as np
    import matplotlib.pyplot as plt
    creer_grille()
    plt.title("TIC TAC TOE")
    J=np.zeros((3,3))
    for k in range(9):
        a=k%2 +1
        if a==1:
            print ("joueur 1")
        if a==2:
            print ("joueur 2")
        print (J)
        l=input("ligne ")
        c=input("colonne ")
        J[l-1][c-1]=a
        if a==1:
            croix(l,c)
        if a==2:
            rond(l,c)
        if a_gagne(J,a)==True:
            print (J)
            return "Bravo au joueur "+str(a)+" qui remporte la partie"
    return "match nul"        


