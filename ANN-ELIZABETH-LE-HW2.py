#   HW2 Assignment 
#   Author: Ann-Elizabeth Le

import math

#   -------
#   Part 1: Patterns
#   -------

#   1) Write a function that given two integers, prints out two identical rectangles
#   of width n and height m, separated by an empty column with '*'
def rectangle(n, m):
    symbol = '*'
    empty_col = " "
    for i in range(n):
        rect = n * symbol
        print(rect + empty_col + rect)

# calling the function with an example
print("Example output for Part 1.1: ")
rectangle(4, 6)


#   2) Write a function that given a positive integer n, prints out a triangle of height n with '*'
#   The triangle should follow the rules:
#   (a) Each row at depth i, i >0 has two more stars than the number of stars of the previous row at depth i-1 
#   (b) At depth 0, the function prints 1 star
def triangle(n):
    k = 2 * n - 2
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")
        k = k - 1
        for j in range(0, i + 1):
            print("* ", end="")
        print("\r")

# calling the function with an example
print('\n' + "Example output for Part 1.2: ")
triangle(6)


#   -------
#   Part 2: Function on lists
#   -------

#   Write a function that takes a list of integers aList as argument
#   and returns a new list where multiple occurrences of values have been removed.
def clean1(aList):
    tmp = []
    for i in aList:
        if i not in tmp:
            tmp.append(i)
    return tmp


# calling the function with an example
print('\n' + "Example output for Part 2: ")
al = [1, 2, 3, 4, 4, 4, 5, 1, 2, 1, 5]
newlist = clean1(al)
print(al)
print(newlist)


#   -------
#   Part 3: Function on lists 
#   -------

#   Write a function that takes a list of integers aList as an argument,
#   modifies this list and does not return a list.
def clean2(aList):
    aList = list(set(aList))


# calling the function with an example
print('\n' + "Example output for Part 3: ")
al = [1, 2, 3, 4, 4, 4, 5, 1, 2, 1, 5]
print(al)
clean2(al)
print(al)

#   -------
#   Part 4: Function on lists
#   -------

#   Write a function that takes a list of integers aList as arguments
#   and returns a string containing elements of the list that are not a power of 2, all on the same line
#   Write a call to this function with arguments embedded in a print statement
def fct(aList):
    tmp = []
    for i in aList:
        if i & (i-1) != 0:
            tmp.append(i)
    return tmp

# calling the function with an example
print('\n' + "Example output for Part 4: ")
al = [1, 2, 3, 4, 5, 16, 255, 256, -1, -2, -4, 84, 8, 16, 4, 6]
print(al)
print(fct(al))


#   -------
#   Part 5: Taylor Sinus 
#   -------

#   Write a function that approximates the sin(x) by
#   returning the sum of the first n elements of its Taylor series
def taylor(x, n):
    approx = 0
    for i in range(n):
        approx += (math.pow(-1,i))/(math.factorial(2*i+1))*(math.pow(x,2*i+1))
    return approx

# calling the function with an example
print('\n' + "Example output for Part 5: ")
x = math.pi/2
print(math.sin(x))
print(taylor(x,7))


#   ------------
#   Extra credit
#   ------------

#   Implement a function that takes a list of integers as argument
#   and return the max number of consecutive integers that are all equal witin this list
def consecutives(aList):
    i = 0
    consec_int = 0   
    while 0 <= i < len(aList):
        counter = 1  
        for j in range(i+1, len(aList)):
            if aList[j] != aList[i]:
                i = j
                break
            counter += 1
            i += 1    
        if counter > consec_int:
            consec_int = counter
        if i == len(aList) - 1:
            break
    return consec_int 

# calling the function with an example
print('\n' + "Example output for extra credit: ")
l1 = [1,1,1,3,3,4,4,4,4,4,3,1,7,3,3,4,4]
l2 = []
l3 = [1,2,1,1,2,1,1]
print(consecutives(l1))
print(consecutives(l2))
print(consecutives(l3))



# END
