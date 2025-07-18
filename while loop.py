# i=1
# while i<=10:
#     print(i)
#     i+=1
# i=20
# while i<=35:
#     print(i)
#     i+=1
# i=2
# while i<=10:
#     print(i)
#     i+=2
# i=1
# while i<=10:
#     if i%2!=0:
#         print(i)
#     i+=1
# i=1
# while i<=20:
#     if i%3==0 or i%5==0:
#         print(i)
#     i+=1
# i=1
# while i<=10:
#     print(i)
#     if i==5:
#         break
#     i+=1  
# i=0
# while i<10:
#     i+=1
#     if i==5:
#         continue
#     print(i)
# i=1
# sum=0
# while i<=10:
#     sum=sum+1
#     i=i+1
# print(sum)
# i=1
# sum=0
# while i<=10:
#     if i%2==0:
#         sum+=i
#     i+=1
# print(sum)
x=int(input("enter a limit"))
i=1
factorial=1
while i<=x:
    factorial*=i
    i+=1
print(factorial)

