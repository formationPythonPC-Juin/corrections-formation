import matplotlib.pyplot as plt # on importe matplotlib.pyplot sous l'alias plt
from math import pi # on importe pi de la bibliothèque math
import numpy as np # on importe la bibliothèque numpy sous l'alias np

####################################
# question 2 : variables de l'énoncé
####################################

I0 = 3
phi = pi/2
k = pi

#############################################
## question 3 : construction du tableau des x
#############################################
debut = 0
fin = 5
pas  = 0.01
x = np.arange(debut, fin+pas, pas)

###############################################
# question 4 : construction du tableau des I(x)
###############################################

I = I0*np.cos(k*x+phi)


########################################
# question 5 : construction de la courbe
########################################

plt.plot(x,I,'b-', label="signal périodique")

#####################################
# question 6 : noms aux axes et titre
#####################################
plt.xlabel("axe d'espace")
plt.ylabel("Intensité")
plt.title("un signal périodique")

###############################
# question 7 : limites des axes
###############################

plt.xlim(debut, fin)
plt.ylim(-I0,I0)
plt.grid()# on affiche une grille

###################################
# question 8 : légende et affichage
###################################

plt.legend()
plt.show() 
