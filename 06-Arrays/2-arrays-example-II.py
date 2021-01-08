"""
Description: Arrays in python. 
"""
import numpy as np

N = 11              #number of elements
a = np.zeros(N)
c = np.arange(N)

#To fill our array
for i in c:
    a[i] = 2*i+1
    
#Buil-in operations with numpy arrays
avg = a.mean()
suma = a.sum()
stddev = a.std()

print (avg, suma, stddev)




"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

