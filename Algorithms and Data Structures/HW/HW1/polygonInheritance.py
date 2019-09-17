#Logan Passi
#CPSC-34000
#08/31/19
#polygonInheritance.py
#P-2.39: Develop an inheritance hierarchy based upon a Polygon class that has abstract methods area( ) and
#perimeter( ). In order to avoid less trivial math, let's just Implement classes RightTriangle, Square and
#Rectangle.


class Polygon: #super class that will be inherited

    def __init__(self): #initializer for the super class
        self._numSides = 0
        self._area = 0
        self._perimeter = 0
        self._sideLengthList = [0] * int(self._numSides)

    def _setSideLength_(self): #function to ask the user to input the length of each distince side of the polygon
        for i in range(self._numSides): #will ask you to input a number for each distinct side
            self._sideLengthList[i] = float(input("Please enter in the length of side " + str(i + 1) + " : "))


    def _calcArea_(self):  #function to calc and return the area of the polygon
        #calculation to determine area goes here
        return self._area

    def _calcPerimeter_(self): #function to calc and return the perimeter of the polgyon
        #calculation to determine perimeter goes here
        return self._perimeter


class RightTriangle(Polygon): #child class of Polygon

    def __init__(self):
        print("\nRight Triangle")
        self._numSides = 3
        self._area = 0
        self._perimeter = 0
        self._sideLengthList = [0] * int(self._numSides)
        self._setSideLength_()

    def _calcArea_(self):
        sideA = float(self._sideLengthList[0])
        sideB = float(self._sideLengthList[1])
        if self._sideLengthList[2] < sideA and self._sideLengthList[2] < sideB: #determining the hypotenuse
            if sideA < sideB:
                sideB = float(self._sideLengthList[2])
            else:
                sideA = float(self._sideLengthList[2])
        else:
            if self._sideLengthList[2] < sideA:
                sideA = self._sideLengthList[2]
            else:
                sideB = self._sideLengthList[2]

        self._area = (sideA*sideB) / 2
        return("\nArea of the right triangle is " + str(self._area) + " units.")

    def _calcPerimeter_(self):
        for i in range(self._numSides):
            self._perimeter += self._sideLengthList[i]

        return("\nThe perimeter of the right triangle is " + str(self._perimeter) + " units.")



class Square(Polygon):

    def __init__(self):
        print("\nSquare")
        self._numSides = 1 #it only has 1 disctinct sides because it is a square
        self._area = 0
        self._perimeter = 0
        self._sideLengthList = [0] * (self._numSides)
        self._setSideLength_()

    def _calcArea_(self): #calculate the area
        self._area = self._sideLengthList[0] ** 2
        return("\nArea of the square is " + str(self._area) + " units.")

    def _calcPerimeter_(self): #calculate the perimeter
        self._perimeter = self._sideLengthList[0] * 4
        return("\nPerimeter of the square it " + str(self._perimeter) + " units.")



class Rectangle(Polygon):

    def __init__(self):
        print("\nRectangle")
        self._numSides = 2 #it only has 1 disctinct sides because it is a square
        self._area = 0
        self._perimeter = 0
        self._sideLengthList = [0] * (self._numSides)
        self._setSideLength_()

    def _calcArea_(self): #calculate the area
        self._area = self._sideLengthList[0] * self._sideLengthList[1]
        return ("\nArea of the square is " + str(self._area) + " units.")

    def _calcPerimeter_(self): #calculate the perimeter
        self._perimeter = (self._sideLengthList[0] * 2) + (self._sideLengthList[1] * 2)
        return ("\nPerimeter of the square it " + str(self._perimeter) + " units.")

myTriangle = RightTriangle()
print(myTriangle._calcArea_())
print(myTriangle._calcPerimeter_())

mySquare = Square()
print(mySquare._calcArea_())
print(mySquare._calcPerimeter_())

myRect = Rectangle()
print(myRect._calcArea_())
print(myRect._calcPerimeter_())

#Right Triangle
#Please enter in the length of side 1 : 5
#Please enter in the length of side 2 : 3
#Please enter in the length of side 3 : 4
#
#Area of the right triangle is 6.0 units.
#
#The perimeter of the right triangle is 12.0 units.
#
#Square
#Please enter in the length of side 1 : 4
#
#Area of the square is 16.0 units.
#
#Perimeter of the square it 16.0 units.
#
#Rectangle
#Please enter in the length of side 1 : 2
#Please enter in the length of side 2 : 5
#
#Area of the square is 10.0 units.
#
#Perimeter of the square it 14.0 units.