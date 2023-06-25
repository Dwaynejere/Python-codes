#CHECK IF A STRING IS A PALINDROME

#DEFINING A FUNCTION
def This_is(s):
    return s == s[::-1]

#PROMPT THE USER TO ENTER THE STRING 
s = input("Enter the string:")

#CALL THE FUNCTION
Final = This_is(s)

#IF STATEMENT AND OUPUT
if Final:
    print("Its s Palindrome")
else:
    print("Not a Palindrome")