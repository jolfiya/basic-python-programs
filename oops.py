# class sample:
#     x="jolfiya"
# obj=sample()
# # print(obj.x)

# class person:
#     def __init__(self,name,age):
#         self.fname=name
#         self.fage=age
#     def details(self):
#         print(self.fname,self.fage)
# obj=person("jolfiya",20)
# obj.details()      

class person:
    def __init__(self,name,age):
        self.fname=name
        self.fage=age
    def details(self):
        print(self.fname,self.fage)
class student(person):
   pass
obj=student("jo",10)
obj.details()