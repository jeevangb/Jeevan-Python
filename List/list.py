#list
l=[]
print(l)
type(l)

# list=eval(input("enter list"))
# print(list)

#list()
l=list(range(0,10,2))
print(l)

#split()
s="python developer"
l=s.split()
print(l)
type(l)

#iterate using for loop
l=[0,1,3,3,4]
for i in l:
 print(i)

#count()
print(l.count(3))
l.insert(1,100)
print(l)

#remove
l.remove(100)
print(l)

#pop
print(l.pop())

#sort
l.sort()
print(l)

#reverse
l.reverse()
print(l)

#clear
print(l)
l.clear
print(l)
