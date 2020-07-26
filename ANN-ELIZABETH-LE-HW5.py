#   HW5 Assignment
#   Author: Ann-Elizabeth Le

import numpy as np
import math
import matplotlib.pyplot as plt
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp


class City:
    #   constructor with 3 instant variables
    def __init__(self, name, xC, yC):
        self.name = name
        self.xCoord = float(xC)
        self.yCoord = float(yC)
        self.coordinates = (float(xC), float(yC))


class TSP:
    #   constructor with 2 dictionaries
    def __init__(self):
        self.cityDict = {}  # cityName key with value of cityCoord
        self.cities = {}  # cityName key with value of list of cityNames list of City objects

    #   read tourX.csv file and split it into partitions
    def readCities(self):
        f = open('tour17.csv', 'r').read()
        line = f.split('\n')
        for i in line:
            split_part = i.replace(' ', '').replace(';', ' ').split()
            cityNames = split_part[0]  # name of the cities
            cityCoord = ((float(split_part[1])), (float(split_part[2])))  # coordinates

            # dictionary where each city name is assigned to a pair of coordinates
            # {'Albany': (43.0, 25.0), ...}
            self.cityDict[cityNames] = cityCoord
            # dictionary where each city name is assigned to a City object (name, xC, yC)
            # {'Albany': <__main__.Cities object at 0x7faa5bd9cca0>, ...}
            self.cities[cityNames] = City(cityNames, (float(split_part[1])), (float(split_part[2])))
        return self.cities


#   run the readCities function in the TSP class
a = TSP()
a.readCities()
#   create
distMatrix = [[0 for i in range(len(a.cities.values()))] for j in range(len(a.cities.values()))]


#   make a list of the coordinates
nodesPoint = []
for n in a.cities.values():
    nodesPoint.append(n.coordinates)

#   make a dictionary with cities and corresponding coordinates
citiesPoint = dict(zip(a.cities.keys(), nodesPoint))


#   make 2 lists for x- and y- coordinates
coordinateXList = []
coordinateYList = []
for identity, i in enumerate(a.cities.values()):
    coordinateXList.append(i.xCoord)
    coordinateYList.append(i.yCoord)
# print(coordinateXList)  # [43.0, 23.0, 16.0, 22.0, ...]
# print(coordinateYList)  # [25.0, 3.0, 22.0, 19.0, ...]


#   calculate distance from each coordinates pairs
for idx, x in enumerate(a.cities.values()):
    for idy, y in enumerate(a.cities.values()):
        dist = math.sqrt((x.coordinates[0]-y.coordinates[0])**2 + (x.coordinates[1]-y.coordinates[1])**2)
        distMatrix[idx][idy] = dist
# for distM in distMatrix:
#     print(distM)


def print_solution(manager, routing, solution):
    #   Resource used in the creation of this part of the code: https://developers.google.com/optimization/routing/tsp
    sortedList = []
    print('Best found distance: {} miles'.format(solution.ObjectiveValue()))
    plan_output = 'Traveling Salesperson Tour Planned Route: \n'
    index = routing.Start(0)
    route_distance = 0
    while not routing.IsEnd(index):
        plan_output += ' {} -'.format(manager.IndexToNode(index))
        sortedList.append(int(manager.IndexToNode(index)))
        previous_index = index
        index = solution.Value(routing.NextVar(index))
        route_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
    #   print out the planned route
    plan_output += ' {}\n'.format(manager.IndexToNode(index))
    print(plan_output)

    #   draw the route path
    pathPoint = []
    for i in sortedList:
        pathPoint.append(nodesPoint[i])
    pathPoint.append(pathPoint[0])
    # print("ROUTE LIST:\n", sortedList)
    print("SORTED PATH POINTLIST:\n", pathPoint)
    data = np.array(pathPoint)
    plt.plot(data[:, 0], data[:, 1])
    plt.show()


if __name__ == '__main__':
    #   create pyplot with the following format in graph
    fig = plt.figure(figsize=(8, 8))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    plt.title("TSP Problem")
    for identity, x in enumerate(a.cities.values()):
        p = [x.xCoord, x.yCoord, x.name]
        axes.plot(p[0], p[1], '.')
        plt.text(p[0] + 0.1, p[1], p[2], horizontalalignment='left', verticalalignment='center')

    #   Resource used in the creation of this part of the code: https://developers.google.com/optimization/routing/tsp
    manager = pywrapcp.RoutingIndexManager(len(distMatrix), 1, 0)
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return distMatrix[from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
    solution = routing.SolveWithParameters(search_parameters)
    
    #   run the print_solution function
    print_solution(manager, routing, solution)
