x={2,4,6,8,10,12,14,16,18,20}
print(x)
print(type(x))
print(len(x))
for i in x:
    print(i)
print(6 in x)
print(6 not in x)
y={1,2,3,4,5,6,7,8,9,10}
print(y)
x.add(22)
print(x)
x.update(y)
print(x)
z=x.union(y)
print(z)
a=x.difference(y)
print(x)