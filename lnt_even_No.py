#FUNCTION THAT TAKES  A LIST OF INTEGERS AS INPUT 
#AND RETURN A NEW LIST CONTAINING ONLY THE EVEN NUMBER

#DEFINING A FUNCTION
def list(numb):
    Enum=[]

#FOR LOOP
    for i in numb:

#IF LOOP
      if i % 2== 0:
       Enum.append(i)
    return Enum 
numb=[21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
Enum=list(numb)

#OUTPUT THE NUMBER
print(Enum)


