"""
Description: Python code to compute some statistics with arrays
"""
import numpy as np

#Number of elements
N = 10000

#Fill with random numbers
def fill(array):
    for i in np.arange(N):
        array[i] = np.random.rand()


data = np.zeros(N)
fill(data)
print(data.mean())














"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

