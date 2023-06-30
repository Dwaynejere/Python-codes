#PYTHON PROGRAM CALCULATING THE AREA AND PERIMETER OF A CIRCLE USING FUNCTIONS AND OBJECTS

#IMPORTING MATH LIBRARIES AND PI FROM MATH
import math
from math import pi

#CREATING CLASS OBJECT
class A_cirlce:

#CREATING METHODS
    def __init__(self,radius):
        self.radius=radius

#METHOD FINDING THE AREA
    def give(self):
        area= pi*self.radius**2
        return math.ceil(area*100)/100
    
#METHOD FINDING THE PERIMETER
    def p_circle(self):
        perimeter=pi*self.radius*2
        return math.ceil(perimeter*100)/100
    
#PROMPTING TO ENTER THE RADIUS
radius=float(input("Enter the Radius:"))

#CREATING AN OBJECT
Area_Circle=A_cirlce(radius)
Perimeter_Circle=A_cirlce(radius)

#OUTPUTING THE AREA AND PERIMETER OF THE CIRCLE
print("Area of the Circle:",Area_Circle.give())
print("Perimeter of the Circle:",Perimeter_Circle.p_circle())