import matplotlib.pyplot as plt
from scipy.integrate import odeint
import numpy as np
from math import sqrt, sin
###################################

################################
# Solution par la méthode odeint
################################

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

# notre inconnue sera ici X = (angle3, puls3)
# soit pour chaque élément : x = (theta, Omega)

# fonction traduisant l'équa diff
def derivee(Z, T) :# il faut préciser qu'est-ce qu'on dérive et par rapport à quoi pr la suite
    return [Z[1], -omega**2 * sin(Z[0])]

# traduisons les CI :
Z0 = [theta0, Omega0]

# espace de temps T3
T3 = np.arange(0, 10, dt)

# résolution de l'équa diff
solution = odeint(derivee, Z0, T3)
# et pour la pulsation uniquement :
puls3 = solution[:,1]


# notre solution est vectorielle
# pour prendre la partie correspondant à la pulsation il faut faire : solution[:,1]

plt.plot(T3,puls3, 'r-', lw = 1, label = "solution par méthode odeint")
plt.legend()
plt.show()
