#CODE CALCULATING THE TEMPERATURE IN FAHRENHEIT AND CELSIUS

#IMPORT MATH LIBRARY
import math

#CREATING AND NAMING A CLASS
class temperature:
    temp=0

#CREATING METHODS
    def __init__(self,temp):
        self.temp= temp

#CREATING A METHOD TO CALCULATE THE TEMPERATURE IN FAHRENHEIT
    def CFahrenheit(self):
        Fahrenheit=(9/5*self.temp)+32
        return round(Fahrenheit*100)/100
    
#CREATING A METHOD TO CALCULATE THE TEMPERATURE IN CELSIUS
    def Ccelsius(self):
        Celsius=(5/9*self.temp)-32
        return round(Celsius*100)/100

#PROMPTING THE USER TO INPUT THE TEMPERATURE
Temp=int(input("Enter the Temperature in Celsius:"))

#CREATING A OBJECT AND NAMING IT
Ftemp=temperature(Temp)

#OUTPUT THE TEMPERATURE
print(Ftemp.CFahrenheit())

#PROMPTING THE USER TO INPUT THE TEMPERATURE
Temp=int(input("Enter the Temperature in Fahrenheit:"))

#CREATING A OBJECT AND NAMING IT
Ctemp=temperature(Temp)

#OUTPUT THE TEMPERATURE
print(Ctemp.Ccelsius())



        