#VOLUME OF A SPHERE

#IMPORT MATH AND PI
import math 
from math import pi

#DEFINING A FUNCTION
def V_Sphere(radius):

#FORMULA OF VOLUME OF A SPHERE
    Vsphere = 4/3*pi*(radius**3)
    return Vsphere

#PROMPT THE USER TO ENTER THE RADIUS
radius = int(input("Enter the radius:"))

#CALL THE FUNCTION AND OUTPUT IT
print(math.trunc(V_Sphere(radius)))