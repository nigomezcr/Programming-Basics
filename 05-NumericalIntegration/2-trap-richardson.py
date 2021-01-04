"""
Description: Numerical Integration methods: Richardson-Trapezoidal Rule
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

#Richardson rule to improve trapezoidal rule
def richardson(alg, fun, x0, xf, n):
    return (4*alg(fun, x0, xf, 2*n) -alg(fun, x0, xf, n))/3

#Parameters and printing of the results
Xmin = 0.0
Xmax = 1.0

for i in np.arange(7):
    Nmax = pow(10, i)
    numerical_trap = trapezoidal(f, Xmin, Xmax, Nmax)
    numerical_rich = richardson(trapezoidal, f, Xmin, Xmax, Nmax)
    theoretical = -np.cos(Xmax) + np.cos(Xmin)
    Err_trap = abs(1 - numerical_trap/theoretical)
    Err_rich = abs(1 - numerical_rich/theoretical)
    print(Nmax, Err_trap, Err_rich)







"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

