"""
Description: Numerical Integration methods: Simpson Rule
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

#Simpson rule
def simpson(fun, x0, xf, n):
    h = (xf - x0)/n
    suma = 0
    aux1, aux2 = 0, 0
    for i in np.arange(1, n/2-1):
        xi = x0 + 2*i*h
        aux1 = fun(xi)
    for i in np.arange(1, n/2):
        xi = x0 + (2*i - 1)*h
        aux2 = fun(xi)
    suma = h*(fun(x0) + 2*aux1 + 4*aux2 + fun(xf))/3
    return suma

#Parameters and printing of the results
Xmin = 0.0
Xmax = 1.0

for i in np.arange(7):
    Nmax = pow(10, i)
    theoretical = -np.cos(Xmax) + np.cos(Xmin)
    numerical_trap = trapezoidal(f, Xmin, Xmax, Nmax)
    numerical_rich = richardson(trapezoidal, f, Xmin, Xmax, Nmax)
    numerical_simp = simpson(f, Xmin, Xmax, Nmax)
    Err_trap = abs(1 - numerical_trap/theoretical)
    Err_rich = abs(1 - numerical_rich/theoretical)
    Err_simp = abs(1 - numerical_simp/theoretical)
    print(Nmax, Err_trap, Err_rich, Err_simp)







"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

