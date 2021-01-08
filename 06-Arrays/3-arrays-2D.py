"""
Description: Arrays in 2D
"""
import numpy as np

N = 5 #rows
M = 4 #columns

#Two forms of initialize 2D arrays (the first one has to be filled)
matrix1 = np.zeros((N,M))
matrix2 = np.array([ [1,23,6],[8,7,5] ])

#To fill or access to the elements
matrix1[4][3] = 3
matrix1[2,2] = 2
a = matrix2[0,1]

def fill(array, row, col):
    for ix in np.arange(row):
        for iy in np.arange(col):
            array[ix][iy] = ix*col + iy

def transpose(array, Tarray, row, col):
    for ix in np.arange(row):
        for iy in np.arange(col):
            Tarray[iy][ix] = array[ix][iy]
            
#Fill original matrix
fill(matrix1, N, M)

#Initialize transpose
Tmatrix = np.zeros((M,N))

#Get the transpose
transpose(matrix1, Tmatrix, N, M)

#print both
print("Original matrix:\n", matrix1, '\n' , "Transpose:\n" , Tmatrix)





"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

