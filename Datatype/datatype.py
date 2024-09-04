#Data Type

#1 int 
a=10
type(a)

#2 float
b=10.0
type(b)

#3 bool
c=True
type(c)

#4 string
d="jeevan"
type(d)

e="""tech
squad"""
type(e)

#Slicing of Strings:
a="jeeva"
print(a[0])
print(a[-1])
print(a[1:80]) #start at 1 to complete

#5 char
x='j'
type(x)

a=100
b=100

a is b
#if data is same then id/ address remains same -memory utilization
print(id(a))
print(id(b))

#6 byte
x=[10,20,30]
b=bytes(x)
# b[0]=100  #'bytes' object does not support item assignmen
type(x)

#7 bytearray 

a=[10,20,30]
b=bytearray(a)
for i in b : print(i)
b[0]=100
for i in b : print(i)

#8 list -> An ordered, mutable, heterogenous collection of eleemnts is nothing but list, 
# where duplicates also allowed.
l=[10,2.4,"jeeva",True,10]
print(l)

#9  tuple
t=(10,20,30,40) # mmutable
type(t)
# t[0]=100
# t.remove(10)

#10 range 
r=range(10)
for i in r: print(i)

k=range(10,2,20)
for i in k: print(i)

#11 set - is not index base
s={10,20,"jeevan"}
type(s)
s.add

#12 frozenset
type(frozenset(s)) #immmutable

#13 dict
d={a:"jeevan"}
type(d)

