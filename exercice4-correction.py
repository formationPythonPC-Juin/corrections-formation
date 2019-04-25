import matplotlib.pyplot as plt


######################################
# coordonnées spatiales et temporelles
######################################

T = [0.0, 0.04, 0.08, 0.12, 0.16, 0.2, 0.24, 0.28, 0.32, 0.36, 0.4, 0.44, 0.48, 0.52, 0.56, 0.6, 0.64, 0.68, 0.72, 0.76, 0.8, 0.84, 0.88, 0.92]

X = [-0.953328037081172, -0.879995111151852, -0.799995555592592, -0.716662685218364, -0.636663129659105, -0.559996888914815, -0.479997333355555, -0.393331148166358, -0.313331592607099, -0.233332037047839, -0.149999166673611, -0.066666296299383, 0.013333259259877, 0.096666129634105, 0.179999000008333, 0.259998555567592, 0.343331425941821, 0.426664296316049, 0.506663851875308, 0.586663407434568, 0.663329648178858, 0.743329203738117, 0.819995444482407, 0.893328370411728]

Y = [-0.046666407409568, 0.069999611114352, 0.166665740748457, 0.253331925937654, 0.326664851866975, 0.389997833351389, 0.433330925945988, 0.469997388910648, 0.486663962985494, 0.493330592615432, 0.489997277800463, 0.469997388910648, 0.433330925945988, 0.38666451853642, 0.323331537052006, 0.249998611122685, 0.156665796303549, 0.053333037039506, -0.063332981484414, -0.189998944453241, -0.333331481496913, -0.486663962985494, -0.65332970373395, -0.789995611147685]


#################
# question 1
#################

plt.plot(X,Y, 'bo--', label = "trajectoire du point")


#################
# question 2
#################

vx = (X[3]-X[2])/(T[3]-T[2])
vy = (Y[3]-Y[2])/(T[3]-T[2])

print("vx = ",vx, " m/s")
print("vy = ",vy, " m/s")


#################
# question 3
#################

v = (vx**2+vy**2)**(1/2)

print("v = ", v, " m/s")

#################
# question 4
#################

echelle = 0.1
plt.arrow(X[2], Y[2], echelle*vx, echelle*vy, length_includes_head ="true", color = 'red')


#################
# question 5
#################

for i in range(0, len(X)-1) :
    vx = (X[i+1]-X[i])/(T[i+1]-T[i])
    vy = (Y[i+1]-Y[i])/(T[i+1]-T[i])
    plt.arrow(X[i], Y[i], echelle*vx, echelle*vy, length_includes_head ="true", head_width = 0.02, color = 'magenta')


#################
# question 6
#################


plt.text(0,0, "vecteurs vitesse", color = "magenta")
# place le texte "vecteurs vitesse" de couleur magenta aux coordonnées (0,0) : c'est la légende des vecteurs
# Pour vérifier cela, il suffit de commenter la ligne plt.text(...) ; à ce moment-là, après compilation, la légende des vecteurs n'apparaît plus
# l'utilité de cette ligne est donc bien d'écrire une légende pour les vecteurs

#################
# question 7
#################

plt.xlabel("abscisse")
plt.xlabel("ordonnée")
plt.title("trajectoire et vecteurs vitesse")


#######################
plt.legend()
plt.show()
