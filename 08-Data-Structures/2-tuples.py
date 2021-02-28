"""
Description: Second data structure in python: tuples
"""

#Create a tuple
mytuple1 = ("me", "you", "him")

print("tuple: ", mytuple1)

#Access elements
print('The first one is: ', mytuple1[0])

#Elemnts cannot be changed (discoment the second line)
#mytuple1[0]="we"

#Can be defined with diff. kinds of elements.
mytuple2 = ("one", 2, 3.0)

#Functions
print('number of elements: ' , len(mytuple1))

#Nested tuples: A tuple can be made of lists or other tuples
mytuple3 = ("wow", 564.3, (2,3,4), [False, True, True, False])

#Operations like sclicing, deleting, or operations element by element still work on tuples.


"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""

