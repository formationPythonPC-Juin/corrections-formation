#############################
# EXERCICE 6
#############################

######################################
# question 3 : extraction des 2 listes
######################################

########################
# méthode 1 : avec Numpy
########################
import numpy as np

tableau = np.loadtxt("donnees", delimiter = ",", skiprows = 1)
T = tableau[:,0]
R = tableau[:,1]

"""
# OU : 
########################
# méthode 2 : avec Pandas
########################
import pandas as pa

table = pa.read_csv("donnees")

T = table["température"]
R = table["Réquivalente"]
"""
####################################################
# question 4 : représentation graphique des 2 listes
####################################################
import matplotlib.pyplot as plt

plt.plot(T,R,'b+', label = "points expérimentaux")

plt.title("Représentation Résistance en fonction de Température")
plt.xlabel("Température")
plt.ylabel("Résistance")



###########################
# question 5 : modélisation
###########################
import numpy as np

liste_coeffs = np.polyfit(T,R,1)

a = liste_coeffs[0]
b = liste_coeffs[1]


#######################################
# question 6 : représentation du modèle
#######################################

R_modele = a*T+b

plt.plot(T,R_modele,'r-', label = "modélisation")







plt.legend()
plt.show()
