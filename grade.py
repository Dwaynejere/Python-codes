#PROMPTING THE USER TO ENTER THE MARKS OF THE STATED UNIT
Python = int(input('Enter Python Marks:'))
Distributed_Systems = int(input('Enter Distributed Systems Marks:'))
Research_Methods = int(input('Enter Research Methods Marks:'))
Telecommunication = int(input('Enter Telecommunication Marks:'))
Software_Engineering = int(input('Enter Software engineering Marks:'))
System_Security = int(input('Enter System Security Marks:'))

#IF STATEMENT TO DEAL WITH MARKS ENTERED REJECTING MARKS LESS THAN 0 AND GREATER THAN 100
if Python < 0 or Python > 100 or Distributed_Systems < 0 or Distributed_Systems > 100 or Research_Methods < 0 or Research_Methods > 100 or Telecommunication < 0 or Telecommunication > 100 or Software_Engineering < 0 or Software_Engineering > 100 or System_Security < 0 or System_Security >100:
    print("Invalid marks entered.")
else:

#CALCULATION OF THE AVERAGE
    average = (Python+Distributed_Systems+Research_Methods+Telecommunication+Software_Engineering+System_Security)/6

#IF STATEMENT IN CALCULATING THE GRADE
if (average>=70 and average<=100):
    print("GRADE A")
elif (average>=60 and average<=69):
    print("GRADE B")
elif (average>=50 and average<=59):
    print("GRADE C")
elif (average>=40 and average<=49):
    print("GRADE D")
else:
    print("FAIL")