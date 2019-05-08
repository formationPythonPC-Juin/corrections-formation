#######################################################
#######################################################
# Exercice 6
#######################################################
#######################################################

import matplotlib.pyplot as plt
import numpy as np
from math import radians, exp, cos, sin

################
# question 1
################
m = 0.4
g = 9.8
k = 5e-2

alpha = 55
alpha = radians(alpha)

tau = m/k
v0 = 10

################
# question 2
################
t0 = 0
tf = 1.7
dt = 0.1
T = np.arange(t0, tf+dt, dt)

################
# question 3
################
X = v0*cos(alpha)*tau*(1-np.exp(-T/tau))
Y = v0*sin(alpha)*tau*(1-np.exp(-T/tau))-tau*g*T + (tau**2)*g*(1-np.exp(-T/tau))
VX = v0*cos(alpha)*np.exp(-T/tau)
VY = v0*sin(alpha)*np.exp(-T/tau)-tau*g*(1-np.exp(-T/tau))


##############
# question 4
##############
plt.plot(X,Y,"b+--", lw = 0.5, label = "trajectoire du solide")


plt.legend()
plt.show()




#######################################################
#######################################################
# Exercice 8
#######################################################
#######################################################

##############
# question 1
##############
Ep = m*g*Y
Ec = 0.5*m*(VX**2+VY**2)
E = Ec+Ep

##############
# question 2
##############

# construction de Ep en fonction du temps
plt.plot(T, Ep, "b-",label="énergie potentielle")

# construction de Ec en fonction du temps
plt.plot(T, Ec, "g-",label="énergie cinétique")

# construction de E en fonction du temps
plt.plot(T, E, "r-",label="énergie mécanique")

# un titre au graphe
plt.title("Étude énergétique")


# affichage des valeurs des 4 tableaux T, Ep, Ec, E
for i in range(len(T)) : 
    print("temps : ",T[i], "   Ep : ",Ep[i], "   Ec : ",Ec[i], "   E : ", E[i])


plt.legend()
plt.show()


##############
# question 3
##############
# initialisation de la liste Xarrondie
Xarrondie = []

# implémentation de Xarrondie
for i in X : # pour chaque élément de X
    i = round(i, 1) # on l'arrondit au 1er chiffre après la virgule
    Xarrondie.append(i) # on l'ajoute à la liste Xarrondie

# On affiche X et Xarrondie
print("X = ", X)
print("Xarrondie = ", Xarrondie)





