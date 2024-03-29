#   HW3 Assignment 
#   Author: Ann-Elizabeth Le

#   -------
#   Part 1: Point
#   -------

#   State a class Point that has 2 instance variables, rational coordinates self.x and self.y
class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    # returns coordinates with specific format
    def toString(self):
        #return "({}, {})".format(self.x, self.y)
        return '(' + str(self.x) + ', ' + str(self.y) + ')'


    # compares 2 Points to see if they are similar or different
    def equals(self, point):
        # if self.x == point.x and self.y == point.y:
        #     return "True"
        # else:
        #     return "False"
        return self.x == point.getX() and self.y == point.getY()


print("PART 1: POINT")
# create points p1 and p2
p1 = Point()
p2 = Point(1, 2)
print("p1 and p2 --> ", p1.toString(), " ", p2.toString())  # print out coordinates of 2 points
print("p1 equals p2? --> ", p1.equals(p2))  # print out result of applying equals method of p1 to p2

# set x coordinate of p2 equal to x coordinate of p1
p1X = p1.getX()
p2.setX(p1X)
# set y coordinate of p2 equal to y coordinate of p1
p1Y = p1.getY()
p2.setY(p1Y)
print("\nset p2's coordinates to p1's --> ", p2.toString())  # print out result of applying equals method of p1 to p2
print("p1 equals p2? --> ", p1.equals(p2))  # print out result of applying equals method of p1 to p2

# increment 1 to x coordinate of p2
p2.setX(p2.getX() + 1)
print("\np2's x coordinate --> ", p2.toString())  # print out new coordinates of p2
print("p1 equals p2? --> ", p1.equals(p2))  # print out result of applying equals method of p1 to p2


#   -------
#   Part 2: Rectangle
#   -------

#   State a class Rectangle that has 3 instance variables: a point, a rational width, and a rational height
class Rectangle:
    def __init__(self, point, w, h):
        self.bottomLeft = point
        self.width = w
        self.height = h

    # returns perimeter of rectangle
    def perimeter(self):
        p = (self.width + self.height) * 2
        return p

    # returns area of rectangle
    def area(self):
        a = self.width * self.height
        return a

    # returns reference to point representing left bottom corner of rectangle
    def getOrigin(self):
        #o = self.point.x, self.point.y
        o = self.bottomLeft
        return o

    # returns string with specific format
    def toString(self):
        #s = "({}, {}), L={}, H={}".format(self.point.x, self.point.y, self.width, self.height)
        s = self.getOrigin().toString() + ", W=" + str(self.width) + ", H=" + str(self.height)
        return s


print("\n\nPART 2: RECTANGLE")
# create rectangles r1 and r2
p1 = Point()
r1 = Rectangle(p1, 2, 5.5)
p2 = Point(1, 2)
r2 = Rectangle(p2, 3, 6)

# print out bottom left corner and perimeter of r1
print("r1 bottom left corner --> ", r1.getOrigin())
print("r1 perimeter --> ", r1.perimeter())

# print out bottom left corner and area of r2
print("r2 bottom left corner --> ", r2.getOrigin())  # calls toString method
print("r2 area --> ", r2.area())

# print toString method for r1 and r2
print("r1 toString --> ", r1.toString())
print("r2 toString --> ", r2.toString())


#   -------
#   Part 3: Movable rectangle
#   -------

#   State a class MovableRectangle that inherits from the class Rectangle
#   This class has 3 arguments: a point and 2 rational values to be assigned to 3 instance variables
class MovableRectangle(Rectangle):
    def __init__(self, bottomLeft, w, h):
        Rectangle.__init__(self, bottomLeft, w, h)
        self.move = False

    # sets self.move to true
    def unlock(self):
        self.move = True

    # sets self.move to false
    def lock(self):
        self.move = False

    # detects whether rectangle is locked or unlocked
    def moveTo(self, newPoint):
        if self.move is True:  # if rectangle is unlocked
            #self.bottomLeft = newPoint  # moves rectangle so new origin is the point argument
            self.getOrigin().setX(newPoint.getX())
            self.getOrigin().setY(newPoint.getY())
        else:
            print("Warning: locked.")

    # returns string with specific format
    def toString(self):
        #s = "({}, {}), W={}, H={}, Movable? {}".format(self.point.x, self.point.y, self.width, self.height, self.move)
        s = Rectangle.toString(self) + ", Movable? " + str(self.move)
        return s


print("\n\nPART 3: MOVABLE RECTANGLE")
# create movable rectangle r3
p1 = Point()
r3 = MovableRectangle(p1, 2, 2)
print("r3 toString --> ", r3.toString())  # calls toString method

p3 = Point(5, 15)
print("\nCan it be moved?")
r3.moveTo(p3)  #calls moveTo method on r3 to move origin to p3
print("r3 with moveTo method on p3 --> ", r3.toString())  # calls toString method

r3.unlock()
print("\nCan it be moved?")
r3.moveTo(p3)  #calls moveTo method on r3 to move origin to p3
print("r3 with moveTo method on p3 --> ", r3.toString())  # calls toString method


#   ------------
#   Extra credit: Read File
#   ------------

#   Create a class Tour with a single instance variable self.MyList that will refer to a list object
class Tour:
    def __init__(self, filename):
        self.myList = []
        file = open(filename, 'r')
        for line in file.readlines():
            row = []
            for value in line.split(","):
                row.append(value.strip())
                self.myList.append(row)
        file.close()

        # alternative method
        # self.myList = []
        # file = open(filename)
        # for line in file:
        #     l = line.split(',')
        #     for i in range(0, len(l)):
        #         l[i] = l[i].rstrip('\n')
        #     self.myList.append(l)
        # file.close()

print("PART 4: EXTRA CREDIT - READ FILE")
filename = input('Enter input filename: ')
t = Tour(filename)
print(t.myList)


#   END
