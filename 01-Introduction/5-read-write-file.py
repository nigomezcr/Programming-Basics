# Python code to read from file
import numpy as np

#Reading files
f = open("file.csv", "r")

#reads char by char
string =f.read(24)

print(string)


f.close()

