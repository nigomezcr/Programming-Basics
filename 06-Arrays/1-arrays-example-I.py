"""
Description: Arrays in python. 
"""
import numpy as np

#Built-in arrays in numpy:
N = 11              #number of elements
a = np.zeros(N)
b = np.ones(N)
c = np.arange(N)
d = np.eye(N)

#To fill our array
for i in c:
    a[i] = 2*i+1
    
#Operations with the array: average
suma = 0
for i in c:
    suma += a[i]
    
average = suma/N
print(average)



"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

