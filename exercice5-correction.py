import matplotlib.pyplot as plt
import numpy as np



T = [0.0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92]

X = [-0.953328037081172, -0.879995111151852, -0.799995555592592, -0.716662685218364, -0.636663129659105, -0.559996888914815, -0.479997333355555, -0.393331148166358, -0.313331592607099, -0.233332037047839, -0.149999166673611, -0.066666296299383, 0.013333259259877, 0.096666129634105, 0.179999000008333, 0.259998555567592, 0.343331425941821, 0.426664296316049, 0.506663851875308, 0.586663407434568, 0.663329648178858, 0.743329203738117, 0.819995444482407, 0.893328370411728]

Y = [-0.046666407409568, 0.069999611114352, 0.166665740748457, 0.253331925937654, 0.326664851866975, 0.389997833351389, 0.433330925945988, 0.469997388910648, 0.486663962985494, 0.493330592615432, 0.489997277800463, 0.469997388910648, 0.433330925945988, 0.38666451853642, 0.323331537052006, 0.249998611122685, 0.156665796303549, 0.053333037039506, -0.063332981484414, -0.189998944453241, -0.333331481496913, -0.486663962985494, -0.65332970373395, -0.789995611147685]



######################
# question 1
######################

# À COMPLÉTER :
# représenter la trajectoire

plt.plot(X,Y,'b--', label = 'trajectoire')




######################
# question 2
######################

# À COMPLÉTER :
# trouver la liste des coefficients polynomiaux
liste = np.polyfit(X,Y,2)
a = liste[0]
b = liste[1]
c = liste[2]

# À COMPLÉTER :
# faites-les afficher
print("a = ", a)
print("b = ", b)
print("c = ", c)




######################
# question 3
######################

# À COMPLÉTER :
# on transforme la liste X en tableau
X = np.array(X)

# À COMPLÉTER :
# on construit un tableau Y_modele image du tableau X
# par le polynôme trouvé au dessus
Y_modele = a*X**2+b*X+c

# À COMPLÉTER :
# on construit la trace de ce polynôme sur le graphe
plt.plot(X, Y_modele, 'r-', label = "modèle")



######################
# question 4
######################

# À COMPLÉTER :
# noms des axes, titre du graphique
plt.xlabel("abscisse")
plt.ylabel("ordonnée")
plt.title("Trajectoire et modèle associé")



######################
plt.legend()
plt.show()
