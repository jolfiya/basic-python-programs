# # 1.print multiplication table from 1 to 10.
# x=int(input("enter multiplication table"))
# def table(y):
#     print(y)
#     for i in range(1,11):
#         print(i,"x",x,"=",x*i)
# table(x)

# # 2.write a function to generate the fibanocci sequence up to a specified number n. use a loop to print the sequence.
# def fibanocci(n):
#     a,b=1,2
#     print("fibanocci up to",n)
#     while a<=n:
#          print(a,end="")
#          a,b=b,a+b
# fibanocci(15)

# 3.write a function to check if a given string is a palindrime.
# x=str(input("enter a string"))
# def palindrome(y):
#     print(y)
#     if y==y[::-1]:
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome(x)


# 4.create a function that checks whether a given number is prime or not.
# x=int(input("enter a number"))
# def prime(y):
#     if y<=1:
#         print("false")
#         return
#     for i in range(2,y):
#         if y%i==0:
#             print("false")
#             break
#         else:
#             print("true")
# prime(x)
        
# 5.create a function that takes a string as input and returns the number of vowels in the string.
x=str(input("enter a string"))
def vowels(y):
    print(y)
    vowels="aeiou"
    count=0
    for vowels in y:
        if vowels in y:
            count+=1
vowels(x)
