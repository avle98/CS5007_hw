#   HW4 Assignment
#   Author: Ann-Elizabeth Le

import numpy as np
import math
import matplotlib.pyplot as plt


#   -------
#   Part 1: Archimedean spiral
#   -------

#   Draws a green Archimedean spiral with parameterized equations
def arc():
    t = np.arange(0, 5 * math.pi, 0.01)  # set t between [0, 5*pi] with step 0.01
    x = t * np.cos(t)  # x(t) = t.cos(t)
    y = t * np.sin(t)  # y(t) = t.sin(t)

    # plot the function using pyplot
    plt.plot(x, y, color='green')
    plt.show()


# call the function
arc()


#   -------
#   Part 2: Heart
#   -------

#   Draws a heart in dashed red lines with parameterized equations
def heart():
    t = np.arange(0, 2 * np.pi, 0.01)  # set t between [0, 5*pi] with step 0.01
    x = 16 * np.sin(t) ** 3  # x(t) = 16sin^3(t)
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(
        4 * t)  # y(t) = 13cos(t) - 5cos(2t) - 2.5cos(3t) - cos(4t)

    # plot the function using pyplot
    plt.plot(x, y, color='red', linestyle='dashed')
    plt.show()


# call the function
heart()


#   -------
#   Part 3: Graphs
#   -------

#   Part 1:
#   If we were to have a situation where there needed to be 8 products loaded by the trucks,
#   there would be 8 vertices and 13 edges. There would be 7 edges between P(k) and P(k+1)
#   and 6 edges between P(k) and P(1), which don't include the already counted P1 to P2 and P1 to P8.

#   Part 2:
#   Algorithm that returns the minimum number of trucks to carry products:
#   1) Randomly select a node and assign it with an initial variable (like a). Start a depth first search from (a)
#   and each time when a new node is found, assign it with the next letter (i.e. b, c, etc.).
#   2) Start assigning letters from Node 1 with (a) to Node 2 with (b). Therefore, letter set is now {a,b}.
#   3) Check the variables of all the nodes one by one (between P(1) and P(k))
#       Compare current node with adjacent node. If any node letter matches with letter of current node,
#       assign the next letter from letter order that's different from the adjacent vertex
#       (i.e. change a to c if current letter set is only {a,b)
#   4) Check the variables of all the nodes having node number greater than current node (between P(i) and P(i+1))
#       If node is not assigned any letter, assign one from the letter set that is different from current node letter
#       If node letter matches with current node, then change letter of node and assign the next letter from letter set
#        (i.e. assign it d if current letter set is only {a,b,c)
#   From this algorithm, the undirected graph with 8 nodes from part 1 would have 3 letters in the letter set.
#   The assignments would be as follows: P(1) = a, P(2,8) = b, P(3,4,5,6,7) = c


#   ------------
#   Part 4: Algorithm
#   ------------

#   A recursive function showing the principle of Egyptian multiplication
def algorithm(x, y):
    if y % 2 == 0 and x > 2 and y > 2:  # if y is even
        #print("method 1")  # uncomment to print this to show for test
        return 2 * (x * (y / 2))
    if y % 2 != 0 and x > 2 and y > 2:  # if y is odd
        #print("method 2")  # uncomment to print this to show for test
        return x + (x * (y - 1))
    if x <= 2 or y <= 2:
        #print("method 3")  # uncomment to print this to show for test
        return x * y


# TESTS
print(algorithm(3, 6))  # method 1
print(algorithm(3, 5))  # method 2
print(algorithm(2, 3))  # method 3


#   END
