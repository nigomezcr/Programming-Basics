"""
Description: Numerical Integration methods: Trapezoidal Rule
"""
import numpy as np
import matplotlib.pyplot as plt

#Function to integrate
def f(x):
    return np.sin(x)
    
#Trapezoidal rule: integral from x0 to xf with n steps
def trapezoidal(fun, x0, xf, n):
    h = (xf - x0)/n
    suma = 0.5*(fun(x0) + fun(xf))
    for i in np.arange(n):
        xi = x0 + i*h
        suma += fun(xi)
    suma *= h
    return suma

#Parameters and printing of the results
Xmin = 0.0
Xmax = 1.0

for i in np.arange(7):
    Nmax = pow(10, i)
    numerical = trapezoidal(f, Xmin, Xmax, Nmax)
    theoretical = -np.cos(Xmax) + np.cos(Xmin)
    Err_trap = abs(1 - numerical/theoretical)
    print(Nmax, Err_trap)







"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

