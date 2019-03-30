###############################
## 2 H2S + SO2 ---> 3 S + 2 H2O
###############################

#########################################################
## question 1 : valeur des coefficients stoechiométriques
#########################################################

coeff_H2S = 2 # coefficient stoechiométrique de H2S

# À COMPLÉTER : Entrez les autres coefficients
coeff_SO2 = 1
coeff_S = 3
coeff_H2O = 2


##############################################
## question 2 : quantités de matière initiales
##############################################
# on demande à l'utilisateur la quantité de H2S initiale
n0_H2S = input("Donne le nombre de moles de H2S : ")
# on transforme cette donnée (typée chaîne de caractères) en nombre décimal
n0_H2S = float(n0_H2S)

# À COMPLÉTER : faites de même pour les autres espèces ;
# pouvez-vous condenser les 2 lignes en une ?
n0_SO2 = float(input("Donne le nombre de moles de SO2 : "))
n0_S = float(input("Donne le nombre de moles de S : "))
n0_H2O = float(input("Donne le nombre de moles de H2O : "))


###############################################
## question 3 : calcul des avancements maximaux
###############################################
xmax_H2S = n0_H2S/coeff_H2S

# À COMPLÉTER : faites de même pour SO2
xmax_SO2 = n0_SO2/coeff_SO2




#################################################
## question 4 : avancement maximal de la réaction
#################################################

# À COMPLÉTER : 
# on utilise une condition pour trouver l'avancement maximal de la réaction :
# si le xmax de H2S est plus petit (ou égal) que le xmax de SO2
# alors xmax de la réaction vaut xmax de H2S
# sinon, xmax de la réaction vaut xmax de SO2
if xmax_H2S <= xmax_SO2 :
    xmax = xmax_H2S
else :
    xmax = xmax_SO2





#on aurait aussi pu utiliser la fonction min :
# xmax = min(xmax_H2S, xmax_SO2)




# À COMPLÉTER : on affiche le résultat sous la forme xmax = ..... mol
print("xmax = ", xmax, " mol.")


#######################################################
## question 5 : calcul des quantités de matière finales
#######################################################
# on calcule les quantités de matière finales en fonction
#des quantités initiales, des différents coeffs et de l'avancement maximal
nF_H2S = n0_H2S - coeff_H2S*xmax

# À COMPLÉTER : faites de même pour les autres espèces de la réaction
nF_SO2 = n0_SO2 - coeff_SO2*xmax
nF_S = n0_S + coeff_S*xmax
nF_H2O = n0_H2O + coeff_H2O*xmax

# À COMPLÉTER : on les affiche sur la console
# sous la forme nF_xxxx = ...... mol.
print("nF_H2S = ",nF_H2S, " mol.")
print("nF_SO2 = ",nF_SO2, " mol.")
print("nF_S = ",nF_S, " mol.")
print("nF_H2O = ",nF_H2O, " mol.")



