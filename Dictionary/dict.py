#doctionary

# d={} 
# print(type(d))
 #or
d=dict()
print(type(d))

d[100]="jeevan"
d["k"]="kiran"
print(d)

#get
print(d.get("k"))

#del
del d["k"]
print(d)

#clear
d.clear()
print(d)

k={1:"a",2:"b",3:"c"}
print(k.keys())
print(k.values())