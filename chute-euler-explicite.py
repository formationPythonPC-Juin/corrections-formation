import matplotlib.pyplot as plt

###########################################################
### chute libre sans vitesse initiale, frott quadratiques
###########################################################

#########################
# Euler explicite
#########################


########################
# question 1
########################
m = 80
f = 0.17
g = 9.81

#############################
# question 2 : initialisation
#############################
t = 0
dt = 1
v0 = 0
v = v0
y0 = 0
y = y0

################################
# question 3 : les forces
################################
frott = -f*v**2
P = m*g

# somme des forces
F = frott+P


################################
# question 4 : initialisation des listes
################################
Y1=[]; V1 = []; T1 =[]



############################################
# question 5 : calculs au cours du mouvement
############################################
while t < 30 :
    V1.append(v); T1.append(t) ; Y1.append(y)
    frott = -f*v**2
    P = m*g
    F = frott+P
    y = y+v*dt
    v = v +F*(dt/m)
    t+=dt

############################################
# question 6 : représentation v = f(t)
############################################
plt.plot(T1,V1, "b--", lw=0.5, label = "Euler explicite")
plt.title("chute libre, frottements quadratiques, Euler explicite")
plt.xlabel("temps")
plt.ylabel("vitesse")
plt.show()
