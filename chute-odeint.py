##################################
## résolution "exacte" avec odeint
##################################


import matplotlib.pyplot as plt
from scipy.integrate import odeint
from numpy import linspace
import numpy as np


# constantes
m = 80
f = 0.17
g = 9.81

# les CI
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

# on entre l'équation différentielle
def derivee(v,t) :# 2 paramètres qui seront donnés en dessous
    frott = -f*v**2
    P = m*g
    F = frott+P
    return F/m

# définition de l'espace des temps de résolution
T3 = np.arange(0, 30, dt)# meme contrainte pour le pas de temps qu'euler explicite pour comparer

# on résout l'équa diff
solution = odeint(derivee, v0, T3)# 2 paramètres pour derivee ; valeur initiale et tableau de temps
V3 = solution

# on trace la vitesse en fonction du temps
plt.plot(T3, V3, "r-", lw=0.5, label = 'solution par odeint de l équa diff')
plt.legend()
plt.title("chute libre, frottements quadratiques, méthode odeint")
plt.show()
