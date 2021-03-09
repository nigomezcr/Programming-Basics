"""
Description: Solving integrals with Scipy libary
"""
from scipy.integrate import quad, dblquad
from scipy.special import jv

#Integral of the Bessel function n=2.5 from 0 to 5

result = quad(lambda x: jv(2.5,x), 0, 5)

print("Result = ", result[0])
print("error = ", result[1])

#Double integral: area 

area = dblquad(lambda x, y: x**y, 0, 0.5, lambda x: 0, lambda x: 1-2*x)

print("area = ", area[0])
print("error = ", area[1])







"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

