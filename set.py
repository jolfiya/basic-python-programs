x={1,2,3,4,5,6,7,8}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
print(2 in x)
print(5 not in x)
x.add(10)
print(x)
y={10,20,30,40,50}
print(y)
x.update(y)
print(x)
a={2,4,6,5,8,7,9,1}
print(a)
b={2,4,10,11,10,5}
print(b)
c=a.union(b)
print(c)
d=a.intersection(b)
print(d)
e=a.difference(b)
print(e)
f=a.symmetric_difference(b)
print(f)
x.remove(3)
print(x)
x.discard(3)
print(x)
x.pop()
print(x)
x.clear()
print(x)
# del x
# print(x)

x=[1,2,3,4,5,6,7,8,9,10]
x[2]=5
print(x)
y=frozenset(x)
print(y)
y[3]=6
print(y)