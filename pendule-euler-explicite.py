import matplotlib.pyplot as plt
from math import sqrt, sin
###################################

###################
# Euler explicite
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

# représentation de la pulsation
plt.title("Pulsation du pendule simple")
plt.xlabel("temps (en s)")
plt.ylabel("Pulsation")
plt.plot(T1,puls1, 'b+--', lw = 0.5, label = "Euler explicite : diverge")
plt.legend()
plt.show()
