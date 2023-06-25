#AREA OF A CIRCLE

#IMPORT PI
import math
from math import pi

#DEFINING A FUNCTION
def circle(radius):

#STATING THE PERIMETER FORMULA
    area = pi*(radius**2)
    return area

#CALLING A FUNCTION && PRINT
radius = int(input("Enter the Radius:"))
print(math.trunc(circle(radius)))