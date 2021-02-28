"""
Description: Third data structure in python: sets
Sets are neither ordered nor indexed.
"""

#Create a set
myset1 = {"me", "you", "him"} #Notice the alphabetic order
print("set: ", myset1)


#As they are not ordered, can't be accessed
#print('The first one is: ', myset1[0])

#Elemnts cannot be changed (discoment the second line)
#myset1[0]="we"


#Duplicated elements will be ignored
myset1 = {"me", "you", "him", "me"}
print("set: ", myset1)


#Functions
print('number of elements: ' , len(myset1))

#Can be defined with diff. kinds of elements.
myset2 = {"one", 2, 3.0,  (1,0,0)}

#Unless they are mutable
#myset2 = {"one", 2, 3.0, [True, True],  (1,0,0), {6}}


#del , discard() and remove() function can be used on sets

#Union and instersection of sets
myset3 = {6,7,2,8,3,4}
myset4 = {9,7,8,3,6,0}
myset5 = myset3.union(myset4)
myset6 = myset3.instersection(myset4)

print('set 1:', myset3 )
print('set 1:', myset4 )
print('union set:', myset5 )
print('instersection set:', myset6 )

"""
There are more functions like:
    update()
    instersection_update()
    symmetric_difference_update()
"""

"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""
