import numpy as np

#Define a class
class Fractional:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def PrintFraction(self):
        print(self.num, '/', self.den)

    def Plus(self, f2):
        result = Fractional(0,1)
        result.num = self.num*f2.den + f2.num*self.den
        result.den = self.den*f2.den
        return result

    def Minus(self, f2):
        result = Fractional(0,1)
        result.num = self.num*f2.den - f2.num*self.den
        result.den = self.den*f2.den
        return result



f = Fractional(4,3)
f.PrintFraction()

g = Fractional(0,1)
g.num = 5
g.den = 2
g.PrintFraction()

h = Fractional(0,1)
h = f.Plus(g)
h.PrintFraction()

h = f.Minus(g)
h.PrintFraction()
