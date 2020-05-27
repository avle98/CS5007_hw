#   HW1 Assignment 
#   Author: Ann-Elizabeth Le
#   Save this file as FIRSTNAME-LASTNAME-HW1.py

import math

#   -------
#   Part 1:
#   -------

print("Part 1")

#   Let the following variables be defined with the following
#   values

a = 5.0
b = 2.5
c = 9.0

#   1a: (write expression in place of the zero in the next line)
expr_1a = (4*a*b) + (b*c)                    
print("The value of expression 1a is", expr_1a)

#   1b: (write expression in place of th5e zero in the next line)
expr_1b = b**3
print("The value of expression 1b is", expr_1b)

#   1c: (write expression in place of the zero in the next line)
expr_1c = math.sqrt(a*b)
print("The value of expression 1c is", expr_1c)

#   1d: (write expression in place of the zero in the next line)
expr_1d = (a*c + b*a)/(b*c)
print("The value of expression 1d is", expr_1d)

#   1e: (write expression in place of the zero in the next line)
expr_1e = a**2 - c**4 + (2*a*b)
print("The value of expression 1e is", expr_1e, "\n")

#   -------
#   Part 2:
#   -------

print("Part 2")

#   2a: (write expression in place of the zero in the next line)
expr_2a = (8//6)*6 
print("The value of expression 2a is", expr_2a)

#   2b: (write expression in place of the zero in the next line)
expr_2b = (8/6)*6
print("The value of expression 2b is", expr_2b)

#   Write here your comment (max. two sentences)
# The double slash '//' represents integer divison (quoteient without remainder)
# instead of floating-point division.
# Therefore 8//6 becomes 1 and 8/6 is 4/3, which is why the first equation is 1*6=6 and the
# second equation is (4/3)*6 = 8.0. 
#



#   -------
#   Part 3:
#   -------

print("\nPart 3")

#   Let the following variables be defined with the following
#   values

a = True
b = False
c = True

#   3a: (write expression in place of the True in the next line)
expr_3a = a and (b or c)
print("The value of expression 3a is", expr_3a)

#   3b: (write expression in place of the True in the next line)
exp3b1 = (a or c)
exp3b2 = b
expr_3b = (not exp3b1) or exp3b2
print("The value of expression 3b is", expr_3b)

#   3c: (write expression in place of the True in the next line)
expr_3c = (a and b) or (not c)
print("The value of expression 3c is", expr_3c)

#   3d: (write expression in place of the True in the next line)
exp3d1 = b
exp3d2 = not c

exp3d4 = (not exp3d1) or exp3d2
exp3d3 = a

expr_3d = (not exp3d3) or exp3d4
print("The value of expression 3d is", expr_3d)

#   -------
#   Part 4:
#   -------

print("\nPart 4")

#   1) Write here your windChill function.
def windChill(T, V):
    windchill = 13.13 + 0.628 * T - 12.1 * (V**0.15) + 0.3967 * T * (V**0.155)
    print("The wind chill with a temperature (C) of ", T,
      " and a wind velocity (kph) of ", V, " is ", windchill) 



#   Call here your windChill function with arguments -20 for T and 30 for V. 
windChill (-20, 30)




#   2) Write here your windChill2 function.
def windChill2():
    windchill = 13.13 + 0.628 * T - 12.1 * (V**0.15) + 0.3967 * T * (V**0.155)
    return(windchill)




#   Call here your windChill2 function with arguments -20 for T and 30 for V.
#   Print the result of this call. 
T = -20
V = 30
print("The wind chill with a temperature (C) of ", T,
      " and a wind velocity (kph) of ", V, " is ", windChill2()) 






#   -------
#   Part 5:
#   -------

print("\nPart 5")

#   List here the 5 errors in the Python function euc
# 1. Arguments do not include y2 and instead have duplicates for y1
# 2. lambda is already a Python function and can't be used as a variable
# 3. return statement is outside of function and variables would not be recognized for function
# 4. 1//2 would not produce the square root because it would return 1 since it is integer divison
# 5. print statement returns a string "result" instead of the called euc function with arguments
#


#   Write correcly the function, the call of this function and
#   the print statement:
def euc(x1, y1, x2, y2):
    x = (x1-x2)**2
    y = (y1-y2)**2
    return ((x+y)**(1/2))
result = euc(1,3,2,7)
print(result)
        








#   ------------
#   Extra credit
#   ------------

print("\nExtra credit")

def myFct(value):
    if(value==1):
        return value
    else:
        return value+myFct(value-1)

#   Write here your comment:
# The recursive function acts like an addition version of factorials, where it adds up all the
# integers starting from the value argument provided all the way down until 1. 
#

#   Write here a simpler function, doing the same without
#   if/else statements and without re-calling myFct

def myFct(value):
    return sum(range(1, value+1))

print("myFct with an argument value of 1: ", myFct(1))
print("myFct with an argument value of 2: ", myFct(2))
print("myFct with an argument value of 3: ", myFct(3))
print("myFct with an argument value of 4: ", myFct(4))
print("myFct with an argument value of 5: ", myFct(5))

# END
