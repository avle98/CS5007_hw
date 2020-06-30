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
    def __str__(self):
        # return s = "(" + str(self.x) + ", " + str(self.y) + ")"
        return "({}, {})".format(self.x, self.y)

    # compares 2 Points to see if they are similar or different
    def equals(self, point):
        if self.x == point.x and self.y == point.y:
            return "True"
        else:
            return "False"


print("PART 1: POINT")
# create points p1 and p2
p1 = Point(0, 0)
p2 = Point(1, 2)
print("p1 and p2 --> " + p1.__str__() + " " + p2.__str__())  # print out coordinates of 2 points
print("p1 equals p2? --> " + p1.equals(p2))  # print out result of applying equals method of p1 to p2

# set x coordinate of p2 equal to x coordinate of p1
p1X = p1.getX()
p2.setX(p1X)
# set y coordinate of p2 equal to y coordinate of p1
p1Y = p1.getY()
p2.setY(p1Y)
print("\nset p2's coordinates to p1's --> " + p2.__str__())  # print out result of applying equals method of p1 to p2
print("p1 equals p2? --> " + p1.equals(p2))  # print out result of applying equals method of p1 to p2

# increment 1 to x coordinate of p2
p2plus = p2.getX()
p2.setX(p2plus + 1)
print("\np2's x coordinate --> " + p2.__str__())  # print out new coordinates of p2
print("p1 equals p2? --> " + p1.equals(p2))  # print out result of applying equals method of p1 to p2


#   -------
#   Part 2: Rectangle
#   -------

#   State a class Rectangle that has 3 instance variables: a point, a rational width, and a rational height
class Rectangle:
    def __init__(self, point, w, h):
        self.origin = point
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
        o = str(self.origin)
        return o

    # returns string with specific format
    def toString(self):
        s = "{}, L={}, H={}".format(self.origin, self.width, self.height)
        return s


print("\n\nPART 2: RECTANGLE")
# create rectangles r1 and r2
p1 = Point(0,0)
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
    def __init__(self, point, w, h, move=False):
        self.origin = point
        Rectangle.__init__(self, w, h, x, y)
        self.move = move

    # sets self.move to true
    def unlock(self):
        self.move = True

    # sets self.move to false
    def lock(self):
        self.move = False

    # detects whether rectangle is locked or unlocked
    def moveTo(self, point):
        if self.move is True:  # if rectangle is unlocked
            self.x = point.x  # moves rectangle so new origin is the point argument
            self.y = point.y
        else:
            print("Warning: locked.")

    # returns string with specific format
    def toString(self):
        s = "({}, {}), W={}, H={}, Movable? {}".format(self.x, self.y, self.width, self.height, self.move)
        return s


print("\n\nPART 3: MOVABLE RECTANGLE")
# create movable rectangle r3
p1
r3 = MovableRectangle(2, 2, False, 0, 0)
print("r3 toString --> " + r3.toString())  # calls toString method

p3 = Point(5, 15)
print("\nCan it be moved?")
r3.moveTo(p3)  #calls moveTo method on r3 to move origin to p3
print("r3 with moveTo method on p3 --> " + r3.toString())  # calls toString method

r3.unlock()
print("\nCan it be moved?")
r3.moveTo(p3)  #calls moveTo method on r3 to move origin to p3
print("r3 with moveTo method on p3 --> " + r3.toString())  # calls toString method


#   ------------
#   Extra credit: Read File
#   ------------

#   Create a class Tour with a single instance variable self.MyList that will refer to a list object
class Tour:
    def __init__(self, myList, filename):
        self.myList = myList
        self.filename = filename


# END
