# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:53:52 2015

@author: Laïta
"""

"Tic tac toc"

# Fonction pour grille
def grille():
    import matplotlib.pyplot as plt
    a=[0,3]
    for i in range (4):
        b=[i,i]
        plt.plot(a,b)
        plt.plot(b,a)

grille()

# Fonction check gagnant
def a_gagne(i,T):
    res=False
    for k in range(3):
        if T[k][0]==i and T[k][1]==i and T[k][2]==i:
            res=True
        if T[0][k]==i and T[1][k]==i and T[2][k]==i:
            res=True
    if T[0][0]==i and T[1][1]==i and T[2][2]==i:
        res=True
    if T[2][0]==i and T[1][1]==i and T[0][2]==i:
        res=True
    return res

# Definition coordonnées
def coord(k,l):
    if (k,l)==(0,0):
        (x,y)=(0,2)
    if (k,l)==(0,1):
        (x,y)=(1,2)
    if (k,l)==(0,2):
        (x,y)=(2,2)
    if (k,l)==(1,0):
        (x,y)=(0,1)
    if (k,l)==(1,1):
        (x,y)=(1,1)
    if (k,l)==(1,2):
        (x,y)=(2,1)
    if (k,l)==(2,0):
        (x,y)=(0,0)
    if (k,l)==(2,1):
        (x,y)=(1,0)
    if (k,l)==(2,2):
        (x,y)=(2,0)
    return (x,y)
   
# Definition pions joueur 1 
def croix(k,l):
    import matplotlib.pyplot as plt
    (x,y)=coord(k,l)
    a=[x+(1/4),x+(3/4)]
    b=[y+(1/4),y+(3/4)]
    d=[y+(3/4),y+(1/4)]
    plt.plot(a,b)
    plt.plot(a,d)
    
croix(0,1) 
 

#Je n'arrrive pas à faire fonctionner la fonction croix et je ne trouve pas mon erreur#

# Definition pionts joueur 2
def rond(k,l):
    import matplotlib.pyplot as plt
    import numpy as np
    (x,y)=coord(k,l)
    t=np.linspace(0,2*np.pi,200)
    plt.plot(x+0.5+0.25*np.cos(t),y+0.5+0.25*np.sin(t))
    
rond(0,1)

# Jeu final
def tic_tac_toc():
    import numpy as np
    import matplotlib.pyplot as plt
    grille()
    T=np.zeros((3,3))
    for n in range (9):
        print (T)
        i=n%2+1
        k=input("rentrez la ligne")
        l=input("rentrez la colonne")
        T[k][l]=i
        if i==1:
            rond(k,l)
        if i==2:
            croix(k,l)
        if a_gagne(i,T)==True:
            print (T)
            return'le joueur '+str(i)+' a gagne : Felicitation'
    return'match nul il faut retenter sa chance'
    
tic_tac_toc()




 

    
