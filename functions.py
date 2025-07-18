# def name():
#     print("jolfiya")
# name()
# name()

# x=int(input("enter a number"))
# y=int(input("enter a number"))
# def sum():
#     print(x+y)
# sum()      
#                                                                           
# def substract():
#     print(x-y)
# substract()

# def multiplication():
#     x=5
#     y=5
#     print(x*y)
# multiplication()

# def add(x,y):
#     print(x+y)
# add(5,5)

# def multiplication(x,y):
#     print(x*y)
# z=int(input("enter a number"))
# h=int(input("enter a number"))
# multiplication(z,h)

# def evenorodd(x):
#     print(x)
#     if x%2==0:
#         print(y,"is even")
#     else:
#         print(y,"is odd")
# y=int(input("enter a number"))
# evenorodd(y)

# y=int(input("enter a number"))
# def sum(x):
#     print(x)
#     sum=0
#     for i in range(x+1):
#         sum+=i
#     print(sum)
# sum(y)

# x=int(input("enter a number"))
# def add(y):
#     print(y)
#     sum=0
#     for i in range(1,x+1):
#         if i%2!=0:
#             sum+=i
#     print(sum)
# add(x)    
        
# x=int(input("enter a number"))
# def factorial(y):
#     print(y)
#     factorial=1
#     for i in range(1,y+1):
#          factorial*=i
#     print(factorial)
# factorial(x)

# x=int(input("enter a number"))
# def prime(y):
#     print(y)
#     for i in range(2,x):
#         if x%i==0:
#             print(y,"is not prime")
#             break
#     else:
#         print(y,"is prime")
# prime(x)

# x=int(input("enter a number"))
# def palindrome(y):
#     print(y)
#     org=y
#     rev=0
#     while y>0:
#         a=y%10
#         rev=rev*10+a
#         y=y//10
#         print("is not palindrome")
#         break
#     else:
#         print("is palindrome")
# palindrome(x)

# x=int(input("display a multiplication table"))
# def table(y):
#     print(y)
#     for i in range(1,11):
#         print(i,"x",x,"=",x*i)
# table(x)

# def add(a,b):
#     print(a+b)
# add(5,5)

# def arbitrary(*a):
#     print(a[6])
# arbitrary(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)

# def keywordarguments(x,y,z):
#     print(x+y)
# keywordarguments(z=15,x=10,y=5)

# def arbitrarykeyword(**x):
#     print(x["b"])
# arbitrarykeyword(a=22,b=15,c=19,d=20,e=50,f=26)

# def default(x=20):
#     print(x)
# default()

# def returnstatement(x):
#     return x+10
# print(returnstatement(15))

# list=[10,5,12,3,5]
# def add(x):
#     sum=0
#     for i in x:
#         sum+=i
# add(list)
 
# x=float(input("enter a number"))
# def area(x):
#     for i in x:
#         area=math.pi*r*r
#         print(math.pi)

# lambda function
# z=lambda a,b:a+b 
# print(z(6,6))

# y=lambda p,q,r:p*q*r
# print(y(2,2,2))

# map function
# x=["mango","anar","grape","banana"]
# a=list(map(lambda b:b.upper(),x))
# print(a)

# x=["WHITE","GREEN","BLACK","BLUE"]
# y=list(map(lambda z:z.lower(),x))
# print(y)

# z=[2,5,3,6,10,5]
# y=list(filter(lambda a:a>5,z))
# print(y)

# find the even numbers in a list using lambda function.
# x=[1,2,3,4,5,6,7,8,9,10]
# y=list(filter(lambda z:z%2==0,x))
# print(y)

# squire the list of numbers using lambda function.
# x=[5,6]
# y=list(map(lambda z:z**2,x))
# print(y)

# squire only even numbers in a list.
# x=[1,2,3,4,5,6]
# y=list(filter(lambda z:z%2==0,x))
# print(y)
# a=list(map(lambda z:z**2,y))
# print(a)

# double the odd numbers only.
# x=[1,2,3,4,5]
# y=list(filter(lambda z:z%2!=0,x))
# print(y)
# a=list(map(lambda z:z+z,y))
# print(a)

# calculate the length of the string in the list.
# x=["white","blue","black","yellow"]
# y=list(map(lambda z:len(z),x))
# print(y)

# find the neg numbers in a list.
# x=[2,5,-10,5,-15,-17,-5,10,0]
# y=list(filter(lambda z:z<0,x))
# print(y)