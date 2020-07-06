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
    t = np.arange(0, 5*math.pi, 0.01)  # set t between [0, 5*pi] with step 0.01
    x = t * np.cos(t)  # x(t) = t.cos(t)
    y = t * np.sin(t)  # y(t) = t.sin(t)

    # plot the function using pyplot
    plt.plot(x, y, color='green')
    plt.show()

#call the function
arc()


#   -------
#   Part 2: Heart
#   -------

#   Draws a heart in dashed red lines with parameterized equations
def heart():
    t = np.arange(0, 2 * np.pi, 0.01)  # set t between [0, 5*pi] with step 0.01
    x = 16 * np.sin(t)**3  # x(t) = 16sin^3(t)
    y = 13 * np.cos(t) - 5*np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)  # y(t) = 13cos(t) - 5cos(2t) - 2.5cos(3t) - cos(4t)

    # plot the function using pyplot
    plt.plot(x, y, color='red', linestyle='dashed')
    plt.show()

#call the function
heart()


#   -------
#   Part 3: Graphs
#   -------

#   Part 1:
#   We


#   Part 2:
#   Algorithm that returns the minimum number of trucks to carry products



#   ------------
#   Part 4: Algorithm
#   ------------

#   A recursive  function using Egyptian multiplication
def algorithm():
    pass


#   END
