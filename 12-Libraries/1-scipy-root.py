"""
Description: Python code using Scipy library to solve equations
(Taken from Scipy documentation tutorial)
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root

#1. Solve x + 2 cos(x) = 0:
    
#First, define the LHS as a function
def f1(x):
    return x + 2 * np.cos(x)

def Solve1():
    sol1 = root(f1, 0.3) #Solution of f1 close to 0.3
    x_root = sol1.x

    print(x_root)

def Plot_f1():
    x = np.arange(-3,3,0.01)
    y = f1(x)
    
    plt.plot(x,y)
    
#Solve1()
#Plot_f1()

#Consider now a set of non-linear equations:
#       x cos(y) = 4
#        xy - y  = 5 

def func2(x):
    f = [x[0] * np.cos(x[1]) - 7, 
         x[1]*x[0] - x[1] - 5]
    df = np.array([[np.cos(x[1]), -x[0] * np.sin(x[1])],
                   [x[1], x[0] - 1]]) 
    return f, df

def Solve2():
    sol2 = root(func2, [1, 1], jac=True, method='lm') #the Levenberg-Marquardt solver is used here
    x_root = sol2.x[0]
    y_root = sol2.x[1]

    print("x = ", x_root)    
    print("y = ", y_root)    


Solve2()




"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

