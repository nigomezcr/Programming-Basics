"""
Description: First data structure in python: List
"""
import numpy as np
import matplotlib.pyplot as plt

#Create list
mylist1 = ["apple", "bannana", "lulo"]
print('List: ', mylist1)

#Access list elements
print('First element: ', mylist1[0])

#Number of elements
print('number of elements: ', len(mylist1))

#In python, a single list can have different data types
mylist2 = ["monkey", "b", 8, np.pi]

#A list can also be created using list()
mylist3 = list((2,3,4))

#Nested lists: list that contain list as elements
mylist4 = ["one", 5, mylist1, [3,4,2]]

#To access to nested lists elements we need more indices
print( mylist4[0], mylist4[3][2] )


#List sclicing:
mylist5 = [0,1,2,3,4,5,6,7,8,9]

print("Slicing of lists: ")
print( mylist5[4:7]) #Elements 4th to 6th
print( mylist5[:-4]) #Elements from first to 4th last


#Operations to change lists
mylist5.append(10)
print("Append 10: ", mylist5)

mylist5.extend([11,12,13])
print("Extend to three more elements: ", mylist5)

mylist5.insert(4, 'pi')
print("Insert elements: ", mylist5)

del mylist5[5:10]
print("Delete elements: ", mylist5)

mylist5.remove('pi')
print("Delete specific elements: ", mylist5)

mylist5.reverse()
print("Reverse elements: ", mylist5)


mylist5.sort()
print("Sort elements: ", mylist5)

#List comprehesion: defining lists from formulas
listpow2 = [2**x for x in range(10)]
print("Comprehesion list: ", listpow2)

"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

