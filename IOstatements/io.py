#read data dynamically
#it takes all data in string type only
a=input("Enter a value")
print(type(a))

a,b=[int(x) for x in input("enter a and b: ").split()]
print(a+b)

#eval Function take a String and evaluate the Result. 
eval("10+20")

#sys
from sys import argv
print("command line args are :",argv)