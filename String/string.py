#string

s='jeevan'
print(s[0])
print(s[-1])

j="kiran"
j[::1] # forward direction
j[::-1] # backward direction

name="kumar"
print(name.find("u"))
print(name.index("u")) # if data not value error

print(name.rfind("u"))
print(name.rindex("u"))

pr="python is more concurrency suuport"
pr1=pr.replace("python","go")
print(pr1)

#reverse string
s="go is more concurrency suuport"
# s[::-1]
print(''.join(reversed(s)))

#reverse order of words
s="Learning python is very is easy"
l=s.split()
l1=[]
i=len(l)-1
while i>=0:
    l1.append(l[i])
    i=i-1
output=' '.join(l1)
print(output)

