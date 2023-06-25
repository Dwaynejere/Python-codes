#VOLUME OF A CYLINDER

#IMPORT MATH AND PI
import math
from math import pi

#DEFINING A FUNCTION
def V_Cylinder(radius,height):

#FORMULA OF VOLUME OF A CYLINDER
    volume = pi*(radius**2)*height
    return volume

#PROMPTING THE USER TO INPUT THE RADIUS AND HEIGHT
radius = int(input("Enter the Radius:"))
height = int(input("Enter the Height:"))

#CALL THE FUNCTION AND PRINT THE OUTPUT
print(math.trunc(V_Cylinder(radius,height)))