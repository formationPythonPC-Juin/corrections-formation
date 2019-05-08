###################################################
###################################################
## Exercice 9 : périodicité spatiale et temporelle
###################################################
###################################################

######################################
# importation des bibli et modules utiles
######################################
import matplotlib.pyplot as plt
from math import pi
import numpy as np


######################################
# définition des variables
######################################
I0 = 3 #
phi = pi/2 #
k = pi #
omega  = pi #
T = 2*pi/omega #
######################################
# initialisation des variables d'espace et de temps
######################################
debut = 0 #
fin = 5 #
pas = 0.01 #
x = np.arange(debut, fin+pas, pas) # tous les points entre 0 et 5 séparés de 0,01

t = 0 #
# I = I0*np.cos(omega*t-k*x+phi) # une référence à la courbe (pas utile)


####################################
# initialisation de la courbe
#####################################
(courbe,) = plt.plot([],[],'b-') # une courbe vide (un tuple : objet Python)
plt.xlim(debut, fin) #
plt.ylim(-I0,I0) #
plt.grid() #


####################################
# actualisation de la courbe et affichage
#####################################

dt = T/50 #

while t < 3*T : #
    I = I0*np.cos(omega*t-k*x+phi) # formule de notre onde : t intervient ici
    courbe.set_data(x,I) # on met à jour les valeurs des listes x et surtout I
    print(t) # 
    plt.pause(dt) #
    t = t + dt # on incrémente t ... et on recommence

plt.show() #
