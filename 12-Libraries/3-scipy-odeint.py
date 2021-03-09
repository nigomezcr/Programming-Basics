"""
Description: Solving ODE's using odeint, from scipy
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

#Damped harmonic oscillator: theta''(t) + b*theta'(t) + c*sin(theta(t)) = 0
# Define two ODE of order 1
#   theta'(t) = omega(t)
#   omega'(t) = -b*omega(t) - c*sin(theta(t))
def Equations(y,t,b,c):
    theta, omega = y
    dydt = [omega, -b*omega - c*np.sin(theta)]
    return dydt

#Set parameters
b = 0.25
c = 5.

#Set initical conditions
y0 = [np.pi - 0.1, 0.0]

#Set solution interval
t = np.linspace(0, 10, 101)

#Solve
sol = odeint(Equations, y0, t, args=(b, c))

#Plot
plt.plot(t, sol[:, 0], 'b', label='theta(t)')
plt.plot(t, sol[:, 1], 'g', label='omega(t)')
plt.legend(loc='best')
plt.xlabel('t')
plt.grid()
plt.show()












"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

