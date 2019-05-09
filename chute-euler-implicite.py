import matplotlib.pyplot as plt
from math import sqrt
###########################################################
### chute libre sans vitesse initiale, frott quadratiques
###########################################################
#########################
# dv/dt = -(f/m)*v**2 + g
#########################
# Euler implicite

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
Y2=[]; V2 = []; T2 =[]



############################################
# question 5 : calculs au cours du mouvement
############################################
while t < 30 :
    V2.append(v); T2.append(t)
    v = (-1+sqrt(1+4*(f*dt/m)*(v+dt*g)))/(2*f*dt/m)
    t+=dt

############################################
# question 6 : représentation v = f(t)
############################################
plt.plot(T2,V2, "g--", lw=0.5, label = "Euler implicite")
plt.title("chute libre, frottements quadratiques, Euler implicite")
plt.xlabel("temps")
plt.ylabel("vitesse")
plt.show()
