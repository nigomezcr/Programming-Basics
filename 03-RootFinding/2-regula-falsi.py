import numpy as np

#Function whose root wants to be found
def f(x):
    g = 9.81
    m = 68.1
    T = 10.0
    VF = 40.0
    return m*g*(1-np.exp(-x*T/m))/x - VF

#Bisection algorithm
def bisection(xl, xu, eps, fun):
    NITERMAX = 1000
    xr = 0
    Niter = 0
    while Niter <= NITERMAX:
        xr = 0.5*(xl + xu)
        if abs(fun(xr)) < eps :
            break
        if fun(xr)*fun(xu) > 0:
            xu = xr
        else:
            xl = xr
        Niter+=1
    print("Bisection Info -> Niter: "  , Niter)
    return xr

#Regula-Falsi algorithm
def regula_falsi(xl, xu, eps, fun):
    NITERMAX = 1000
    xr = 0
    Niter = 0
    while Niter <= NITERMAX:
        fxu = fun(xu)
        fxl = fun(xl)
        xr = xu - (fxu*(xl - xu))/(fxl - fxu)
        if abs(fun(xr)) < eps :
            break
        if fun(xr)*fun(xu) > 0:
            xu = xr
        else:
            xl = xr
        Niter+=1
    print("Regula-Falsi Info -> Niter: "  , Niter)
    return xr

#Parameters to find the root
Xl = 1
Xu = 20
EPS = 1e-12

#Print roots and errors
xroot = bisection(Xl, Xu, EPS, f)
print(xroot, f(xroot))
xroot = regula_falsi(Xl, Xu, EPS, f)
print(xroot, f(xroot))



"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

