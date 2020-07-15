# ---
# Exam 2 - July 2020
# ---

# ----------
# Question 1
# ----------

class Animal:
    def __init__(self, weight,age):
        self.w = weight
        self.a = age
    def incrAge(self):
        self.a += 1
    def __str__(self):
        return "weight: "+str(self.w)+", age: "+str(self.a)

def test1a():
    a = Animal(34,4)
    print(a)
    a.incrAge()
    print(a)

test1a()

class Cat(Animal):
    def __init__(self, weight, age, color):
        Animal.__init__(self,weight, age)
        self.color = color
    def __str__(self):
        return Animal.__str__(self)+", color:"+self.color

def test1b():
    b = Cat(23,3,"brown")
    print(b)
    b.incrAge()
    print(b)

test1b()

# ----------
# Question 2
# ----------

class Polynomial:
    def __init__(self, degree):
        self.myList = []
        for i in range(degree+1):
            self.myList.append(0)
    def setCoef(self, coef, p):
        if coef>=0 and coef<len(self.myList):
            self.myList[coef]=p
    def __str__(self):
        degree = len(self.myList)
        s =""
        for i in range(0,degree):
            if self.myList[i]!=0:
                if self.myList[i]>0:
                    if s != "":
                        s += " + "
                else:
                    if s != "":
                        s += " - "
                    else: s+= "-"
                s += str(abs(self.myList[i]))
                if(i!=0):
                    s += "x"+str(i)
        return s
    def evaluate(self,xvalue):
        degree = len(self.myList)
        res = 0
        for i in range(0,degree):
            res += self.myList[i]*(xvalue**i)
        return res

def test2():
    p1 = Polynomial(5)
    print(p1)
    print(p1.evaluate(3))
    p1.setCoef(0,-4)
    p1.setCoef(2,3)
    p1.setCoef(5,-8)
    print(p1)
    print(p1.evaluate(3))
    p2 = Polynomial(8)
    p2.setCoef(2,-2)
    p2.setCoef(3,4)
    p2.setCoef(5,7)
    p2.setCoef(8,-0.25)
    print(p2)
    print(p2.evaluate(0))
    print(p2.evaluate(-2))
    print(p2.evaluate(3))
    
test2()

# ------------
# Extra-credit
# ------------

import matplotlib.pyplot as plt
import math
import numpy as np

def extra(r,R):
    t = np.arange(0,5*math.pi,0.01)
    d = R+r
    x = d*np.cos(t)-r*(np.cos((d*t)/r))
    y = d*np.sin(t)-r*(np.sin((d*t)/r))
    plt.plot(x, y,'b')

def example():
    plt.subplot(2,2,1)
    extra(10,30)
    plt.subplot(2,2,2)
    extra(10,40)
    plt.subplot(2,2,3)
    extra(10,50)
    plt.subplot(2,2,4)
    extra(10,100)
    plt.show()
    
example()
