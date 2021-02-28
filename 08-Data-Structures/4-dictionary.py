"""
Description: Third data structure in python: sets
Sets are neither ordered nor indexed.
"""

#Create a dictionary
mydictionary1 = {
    "personal": "I",
    "possesive": "mine",
    "adverbial": "me"}
print("dictionary: ", mydictionary1)

#As they are not ordered, can't be accessed
print('Value "persional": ', mydictionary1["personal"])

#Elemnts cannot be changed (discoment the second line)
mydictionary1["personal"]="you"
mydictionary1["adverbial"]="you"
mydictionary1["possesive"]="your"

#Functions
print('number of elements: ' , len(mydictionary1))

#Several values allowed
mydictionary2 =	{
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

"""
#Can be defined with diff. kinds of elements.
myset2 = {"one", 2, 3.0,  (1,0,0)}

#Unless they are mutable
#myset2 = {"one", 2, 3.0, [True, True],  (1,0,0), {6}}


#del , discard() and remove() function can be used on sets

"""


"""
//////////////////////////////////////////////////////////////////////////
Created on Fri Jan  1 13:32:11 2021                                    //
                                                                      //
@author: Nicolás Gómez                                               //
//////////////////////////////////////////////////////////////////////
"""
