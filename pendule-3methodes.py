import matplotlib.pyplot as plt
from math import sqrt, sin
import numpy as np
from scipy.integrate import odeint

###################################

# constantes et CI
g = 10
L = 0.25
omega = sqrt(g/L)
Omega0 = 2
Omega = Omega0
theta0 = 0
theta = theta0
t =0
dt = 0.02


###################
# Euler explicite
###################
# définition des listes
angle1 = []
puls1 = []
T1 = []
# boucle d'évolution sur les 10 premières secondes
while t<10 : 
    angle1.append(theta) ; puls1.append(Omega) ; T1.append(t) 
    Omega1 = Omega - omega**2 * sin(theta)*dt
    theta1 = theta + Omega * dt
    Omega = Omega1
    theta = theta1
    t+=dt

###################
# Euler implicite
###################

# constantes et CI
g = 10
L = 0.25
omega = sqrt(g/L)
Omega0 = 2
Omega = Omega0
theta0 = 0
theta = theta0
t =0
dt = 0.02

# définition des listes
angle2 = []
puls2 = []
T2 = []

# boucle d'évolution sur les 10 premières secondes
while t<10 : 
    angle2.append(theta) ; puls2.append(Omega) ; T2.append(t) 
    theta1 = theta + Omega * dt
    Omega1 = Omega - omega**2 * sin(theta1)*dt
    Omega = Omega1
    theta = theta1
    t+=dt


##########################
# résolution par odeint
##########################

# fonction traduisant l'équa diff
def derivee(Z, T) :
    return [Z[1], -omega**2 * sin(Z[0])]

# traduisons les CI :
Z0 = [theta0, Omega0]

# espace de temps T3
T3 = np.arange(0, 10, dt)

# résolution de l'équa diff
solution = odeint(derivee, Z0, T3)

#la solution pour la pulsation : 
puls3 = solution[:,1]

# représentation des différentes solutions
plt.plot(T1,puls1, 'b+--', lw = 0.5, label = "Euler explicite : diverge")
plt.plot(T2,puls2, 'c+--', lw = 1.5, label = "Euler implicite")
plt.plot(T3,puls3, 'r-', lw = 1, label = "solution par méthode odeint")
plt.title("Pulsation du pendule simple par 3 méthodes numériques")
plt.xlabel("temps (en s)")
plt.ylabel("pulsation")
plt.legend()
plt.show()
