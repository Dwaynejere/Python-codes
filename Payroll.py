#PYTHON ON PAYROLL

#IMPORT MATH LIBRARY
import math

#CREATING A CLASS CALLED EMPLOYEE 
class Employee():

#DEFINING VARIABLES IN THE INIT METHOD    
    def __init__(self,id,name):
        self.id=id
        self.name=name

#CREATING A SALARY EMPLOYEE CLASS INHERITING FROM CLASS EMPLOYEE
class SalaryEmployee(Employee):
    
#DEFINING VARIABLES IN THE INIT METHOD    
    def __init__(self,id,name,basic_salary,allowance):

#CALLING THE VARIABLES FROM CLASS EMPLOYEE        
        super().__init__(id,name)
        self.basic_salary=basic_salary
        self.allowance=allowance
    
#CALCULATE PAYROLL METHOD CALCULATING BASIC SALARY    
    def calculate_payroll(self):

#FORMULA CALCULATING BASIC SALARY        
        Bsalary=self.basic_salary+self.allowance

#OUTPUTING        
        print("THE BASIC SALARY")
        print("ID NO.:", self.id)
        print("NAME:", self.name)
        print("The Basic salary is:",math.trunc(Bsalary))
        return 

#HOURLY EMPLOYEE CLASS INHERITING FROM EMPLOYEE CLASS
class HourlyEmployee(Employee):

#DEFINING VARIABLES    
    def __init__(self,id,name,Hourly_worked,Hourly_pay):

#CALLING THE VARIABLES FROM CLASS EMPLOYEE        
        super().__init__(id,name)
        self.Hourly_worked=Hourly_worked
        self.Hourly_pay=Hourly_pay
    
#CALCULATE PAYROLL METHOD CALCULATING THE PAY OF AN HOURLY EMPLOYEE    
    def calculate_payroll(self):

#FORMULA FOR CALCULATING THE PAY FOR AN HOURLY EMPLOYEE
        Wpay=self.Hourly_worked*self.Hourly_pay

#OUTPUT         
        print("THE HOURLY SALARY")
        print("ID NO.:", self.id)
        print("NAME:", self.name)
        print("The Hourly salary is:",math.trunc(Wpay))
        return 

#COMMISSION EMPLOYEE CLASS INHERITING FROM SALARY EMPLOYEE CLASS
class CommissionEmployee(SalaryEmployee):

#DEFINE VARIABLES
    def __init__(self,id,name,commssion,basic_salary,allowance):

#CALLING THE VARIABLES FROM SALARY EMPLOYEE CLASS        
        super().__init__(id,name,basic_salary,allowance)
        self.commission=commssion
    
#CALCULATE PAYROLL METHOD CALCULATING THE COMMISSION OF AN EMPLOYEE    
    def calculate_payroll(self):
         
#COMMISSION FORMULA         
         Commision=(self.basic_salary+self.allowance)*0.03

#OUTPUT
         print("THE COMMISSION")
         print("ID NO.:",self.id)
         print("NAME:",self.name)
         print("The Commission is:",math.trunc(Commision))
         return 
    
#CREATING OBJECT NAMED EDETAILS AND CALLING SALARYEMPLOYEE CLASS
Edetails= SalaryEmployee(7979,'Jere',35000,500)

#USING THE OBJECT TO CALL THE CALCULATING_PAYROLL METHOD IN SALARYEMPLOYEE CLASS
Edetails.calculate_payroll()

#CREATING OBJECT NAMED EDETAILS1 AND CALLING HOURLYEMPLOYEE CLASS
Edetails1=HourlyEmployee(7970,'Jere',60,800)

#USING THE OBJECT TO CALL THE CALCULATING_PAYROLL METHOD IN HOURLYEMPLOYEE CLASS
Edetails1.calculate_payroll()

#CREATING OBJECT NAMED EDETAILS2 AND CALLING COMMISSIONEMPLOYEE CLASS

Edetails2=CommissionEmployee(7970,'Jere',1000,35000,500)

#USING THE OBJECT TO CALL THE CALCULATING_PAYROLL METHOD IN COMMISSIONEMPLOYEE CLASS
Edetails2.calculate_payroll()
        