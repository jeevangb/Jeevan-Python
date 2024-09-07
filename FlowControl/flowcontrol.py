#if
name="jeevan"
if name=="jeevan":
   print("Hi jeevan")
print("who are you")

# if else
a=10
if a==10:
   print("ten")
else:
   print("not a ten")

#if-elif-else: 
num="1"
if num==0:
   print("zero")
elif num==1:
   print("one")
else:
   print("not a number")

# a=int(input("enter number"))
# print(a)

#for loop
name = "jeevan"
for i in name:
   print(i)

for x in range(5):
   print("Hello")

for i in range(10,0,-1):
   print(i)

# while loop:
x=1
while x<=5:
   print(x)
   x=x+1

#break
x=10
for i in range(x):
   if i==4:
      print("process ends")
      break
   print(i)

#continue
for i in range(6):
   if i%2==0:
      continue
   print(i)


cart=[10,20,30]
for item in cart:
    if item>100:
        print("not process")
        break
    print(item)
else:
    print("all proceed...")

#del
x=10
print(x)
del x
# print(x) it is delected so get error after del

#None 
n ="jeevan"
print(n)
n=None
print(n)
n="kiran"
print(n)
