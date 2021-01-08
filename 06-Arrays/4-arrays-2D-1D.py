"""
Description: Arrays in 2D
"""
import numpy as np

N = 5 #rows
M = 4 #columns

#Declare array
matrix = np.zeros(N*M)

def fill(array, row, col):
    for ix in np.arange(row):
        for iy in np.arange(col):
            array[ix*col + iy] = ix*col + iy

def transpose(array, Tarray, row, col):
    for ix in np.arange(row):
        for iy in np.arange(col):
            Tarray[iy*row + ix] = array[ix*col + iy]
            
#Fill original matrix
fill(matrix, N, M)

#Initialize transpose
Tmatrix = np.zeros(M*N)

#Get the transpose
transpose(matrix, Tmatrix, N, M)

#print both
print("Original matrix:\n", matrix, '\n' , "Transpose:\n" , Tmatrix)





"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

