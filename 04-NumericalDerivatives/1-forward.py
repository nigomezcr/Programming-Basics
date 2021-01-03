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

#Define parameters to plot
DX = 0.01
Xmin = 0.0
Xmax = np.pi

N = (Xmax - Xmin)/DX

for i in np.arange(N):
    x = Xmin + i*DX
    Err_forward = abs(1-forward_derivative(x,DX)/np.cos(x)) 
    print(x, forward_derivative(x, DX), Err_forward)




"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

