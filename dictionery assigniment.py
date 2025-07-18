x={"name":"jo","place":"ekm","age":"15","date":18,"colour":"red"}
print(x)
print(type(x))
print(len(x))
print(x["name"])
print(x.get("place"))
print(x.keys())
print(x.values())
print(x.items())
print("colour" in x)
print("colour" not in x)
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.items():
    print(i)
for i in x.values():
    print(i)
x["date"]="15"
print(x)
x.update({"name":"jyo"})
print(x)
x["number"]=50
print(x)
x.update({"town":"idukki"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("age")
print(x)
x.popitem()
print(x)
del x["name"]
print(x)
x.clear()
print(x)
school={
    "teacher":{"name":"bindu","age":42},
    "student 1":{"name":"aleena","age":15},
    "student 2":{"name":"soja","age":16},
    "student 3":{"name":"kiran","age":17}
}
print(school)
print(school["student 2"])
print(school["student 3"]["name"])
print(school["teacher"]["age"])