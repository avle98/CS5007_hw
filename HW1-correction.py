#   HW1 Assignment 
#   Author: <INSERT FIRST NAME> <INSERT LAST NAME> 
#   Save this file as FIRSTNAME-LASTNAME-HW1.py

#   EXAMPLE OF CORRECTION

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
expr_1a = 4*a*b+b*c
print("The value of expression 1a is", expr_1a)

#   1b: (write expression in place of the zero in the next line)
expr_1b = b**3
print("The value of expression 1b is", expr_1b)

#   1c: (write expression in place of the zero in the next line)
expr_1c = (a*b)**(1/2)
print("The value of expression 1c is", expr_1c)

#   1d: (write expression in place of the zero in the next line)
expr_1d = (a*c + b*a)/(b*c)
print("The value of expression 1d is", expr_1d)

#   1e: (write expression in place of the zero in the next line)
expr_1e = a**2 - c**4 + 2*a*b
print("The value of expression 1e is", expr_1e, "\n")

#   -------
#   Part 2:
#   -------

print("Part 2")

#   Write here your comment (max. two sentences)
#
#   Operator // is integer division while operator / is rational division. 
#   In expression 2a, 8//6 == 1 and in expression 2b, 8/6 == 1.3333333333
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

#   3a: (write expression in place of the zero in the next line)
expr_3a = a and (b or c)
print("The value of expression 3a is", expr_3a)

#   3b: (write expression in place of the zero in the next line)
expr_3b = (not b) or (a or c)
print("The value of expression 3b is", expr_3b)

#   3c: (write expression in place of the zero in the next line)
expr_3c = (a and b) or (not c)
print("The value of expression 3c is", expr_3c)

#   3d: (write expression in place of the zero in the next line)
expr_3d = (not a) or ((not b) or (not c))
print("The value of expression 3d is", expr_3d)

#   -------
#   Part 4:
#   -------

print("\nPart 4")

#  1)  Write here your windChill function

def windChill(T, V):
    wc = 13.13 + 0.628*T
    # print(wc) # uncomment to see the temporary value of the local variable wc
    wc -= 12.1*(V**0.15)
    # print(wc) # uncomment to see the temporary value of the local variable wc
    wc += 0.3967*T*(V**0.155)
    print ("At",str(T)+"C and",V,"kph winds it feels like",str(wc)+"C")

#   Call here your function with arguments -20 for T and 30 for V 

windChill(-20,30)

#   2) Write here your windChill2 function.

def windChill2(T, V):
    wc = 13.13 + 0.628*T
    # print(wc) # uncomment to see the temporary value of the local variable wc
    wc -= 12.1*(V**0.15)
    # print(wc) # uncomment to see the temporary value of the local variable wc
    wc += 0.3967*T*(V**0.155)
    return str(wc)

#   Call here your windChill2 function with arguments -20 for T and 30 for V.
#   Print the result of this call. 

T = -20
V = 30
wc = windChill2(-20,30)
print ("At",str(T)+"C and",V,"kph winds it feels like",str(wc)+"C")

#   -------
#   Part 5:
#   -------

print("\nPart 5")

#   List here the 5 errors in the Python function MyFct
#   - Error 1: Parameter y1 is duplicated.
#   - Error 2: lambda is a reserved word of Python. lambda cannot be used as a variable name. 
#   - Error 3: Indentation of the return statement is incorrect: considered to be outside the function.
#   - Error 4: 1//2 is equal to 0, not 0.5.
#   - Error 5: Print statement: The quotes make the string "result" printed,
#              instead of the value of the variable result. 

#   Write correcly the distance function, the call of this function and
#   the print statement

def euc(x1,y1,x2,y2):
    delta = (x1-x2)**2
    gamma = (y1-y2)**2
    return((delta+gamma)**0.5)

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

print(myFct(5))
print(myFct(4))
print(myFct(3),"\n")

#   Write here your comment:
#
#   The function returns the sum of the integers between 1 and value (included).


#   Write here a simpler function, doing the same without
#   if/else statements and without re-calling myFct

def myFct2(value):
    return(value*(value+1)//2)

print(myFct2(5))
print(myFct2(4))
print(myFct2(3))

# END
