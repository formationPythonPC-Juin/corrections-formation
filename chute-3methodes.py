import matplotlib.pyplot as plt

# constantes
m = 80
f = 0.17
g = 9.81

# initialisation
t = 0
dt = 1
v0 = 0
v = v0
y0 = 0
y = y0

# les forces
frott = -f*v**2
P = m*g

# somme des forces
F = frott+P

##################
# Euler explicite
#####################

# initialisation des listes
Y1=[]; V1 = []; T1 =[]

# calcul au cours du mouvement
while t < 30 :
    V1.append(v); T1.append(t) ; Y1.append(y)
    frott = -f*v**2
    P = m*g
    F = frott+P
    y = y+v*dt
    v = v +F*(dt/m)
    t+=dt


##################
# Euler implicite
##################
from math import sqrt

t = 0
v = v0
y0 = 0
y = y0

# initialisation des listes
Y2=[]; V2 = []; T2 =[]

# calcul au cours du mouvement
while t < 30 :
    V2.append(v); T2.append(t)
    v = (-1+sqrt(1+4*(f*dt/m)*(v+dt*g)))/(2*f*dt/m)
    t+=dt


#######################
# méthode odeint
########################
from scipy.integrate import odeint
from numpy import linspace
import numpy as np

t = 0
v = v0
y0 = 0
y = y0

# initialisation des listes
Y3=[]; V3 = []; T3 =[]

# calcul au cours du mouvement
def derivee(v,t) :# 2 paramètres qui seront donnés en dessous
    frott = -f*v**2
    P = m*g
    F = frott+P
    return F/m

T3 = np.arange(0,30,dt)# meme contrainte pour le pas de temps qu'euler explicite pour comparer
V3 = odeint(derivee, v0, T3)# 2 paramètres pour derivee ; valeur initiale et tableau de temps



################################################
# tracé des 3 courbes d'évolution de la vitesse
################################################
plt.plot(T1, V1, 'b--', label = "Euler explicite")
plt.plot(T2, V2, 'g--', label = "Euler implicite")
plt.plot(T3, V3, 'r--', label = "méthode odeint")




plt.xlabel("temps en s")
plt.ylabel("vitesse du corps")
plt.title("comparaison des 3 méthodes")
plt.legend()
plt.show()
