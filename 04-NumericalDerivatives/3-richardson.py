"""
Description:  Calculate forward derivative of  sin 
              and plot in [0, 2pi] to compare with built-in cos
"""
import numpy as np

#Define the function
def f(x):
    return np.sin(x)

#Fordward derivative algorithm
def forward_derivative(x, h):
    return (f(x+h) - f(x))/h

#Central derivative algorithm
def central_derivative(x, h):
    return (f(x+h/2) - f(x-h/2))/h

#Richardson algorithms
def richardson(x, h, fun):
    D1 = fun(x,h)
    D2 = fun(x,h/2)
    return (4*D2 - D1)/3.0

#Define parameters to plot
DX = 0.01
Xmin = 0.0
Xmax = 2*np.pi

N = (Xmax - Xmin)/DX

for i in np.arange(N):
    x = Xmin + i*DX
    Err_forward = abs(1-forward_derivative(x,DX)/np.cos(x)) 
    Err_central = abs(1-central_derivative(x,DX)/np.cos(x)) 
    Err_richardson_forward = abs(1 - richardson(x, DX, forward_derivative))
    Err_richardson_central = abs(1 - richardson(x, DX, central_derivative))
    print(x, forward_derivative(x, DX), central_derivative(x, DX),
             richardson(x, DX, forward_derivative), richardson(x, DX, central_derivative),
             Err_forward, Err_central, Err_richardson_forward, Err_richardson_central)




"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

