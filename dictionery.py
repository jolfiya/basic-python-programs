x={"name":"jolfiya","place":"idukki","age":20,"colour":"gray"}
print(x)
print(type(x))
print(len(x))
print(x["name"])
print(x["place"])
print(x.get("name"))
print(x.keys())
print(x.values())
print(x.items())
print("name" in x)
print("name" not in x)
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
x["place"]="ekm"
print(x)
x.update({"name":"jyolsna"})
print(x)
x["number"]=100
print(x)
x.update({"town":"cheruthoni"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("name")
print(x)
x.popitem()
print(x)
del x["colour"]
print(x)
x.clear()
print(x)
del x
family={
    "child 1":{"name":"linto","age":10},
    "child 2":{"name":"joseph","age":15},
    "child 3":{"name":"jo","age":16}   
        }
print(family)
print(family["child 1"])
print(family["child 1"]["age"])

