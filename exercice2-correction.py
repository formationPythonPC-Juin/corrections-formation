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
debut = 0 # début de l'ensemble des x
fin = 5 # fin de l'ensemble des x
pas  = 0.01
x = np.arange(debut, fin+pas, pas)

###############################################
# question 4 : construction du tableau des I(x)
###############################################
# on construit le tableau I image de x par la fonction qui nous intéresse
I = I0*np.cos(k*x+phi)


########################################
# question 5 : construction de la courbe
########################################

plt.plot(x,I,'b-', label="signal périodique")# on construit la courbe

#####################################
# question 6 : noms aux axes et titre
#####################################
plt.xlabel("axe d'espace")# nom de l'axe selon Ox
plt.ylabel("Intensité")# de même pour l'ordonnée
plt.title("un signal périodique")# mettre un titre


###############################
# question 7 : limites des axes
###############################

plt.xlim(debut, fin)# faire que le graphe ait des valeurs limites selon Ox
plt.ylim(-I0,I0)# faire que le graphe ait des valeurs limites selon Oy
plt.grid()# on affiche une grille

###################################
# question 8 : légende et affichage
###################################

plt.legend()# on place la légende en utilisant le label de la courbe
plt.show() # on affiche 
