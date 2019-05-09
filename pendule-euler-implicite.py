import matplotlib.pyplot as plt
from math import sqrt, sin
###################################

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

# représentation de la pulsation
plt.title("Pulsation du pendule simple")
plt.xlabel("temps (en s)")
plt.ylabel("Pulsation")
plt.plot(T2,puls2, 'g+--', lw = 0.5, label = "Euler implicite")
plt.legend()
plt.show()
