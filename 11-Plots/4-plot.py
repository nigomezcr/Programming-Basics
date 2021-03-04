"""
Description: Plots in python
"""
import numpy as np
import matplotlib.pyplot as plt


x = np.arange(-np.pi, np.pi, 0.1)

y1 = np.sin(x)
y2 = np.sin(2*x)
y3 = np.sin(3*x)
y4 = np.sin(4*x)

plt.title("Plot in python")
plt.xlabel('x')
plt.ylabel('$f(x)$')
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
plt.yticks([-1,0,1])
plt.grid()


plt.plot(x, y1, 'b', label='$sin(x)$')
plt.plot(x, y2, 'g', label='$sin(2x)$')
plt.plot(x, y3, 'r', label='$sin(3x)$')
#plt.plot(x, y4, 'y', label='$sin(4x)$')
plt.legend()
plt.show()
plt.savefig('4-python.pdf')











"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

