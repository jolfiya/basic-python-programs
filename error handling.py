# try:

#     print(x)
# except:
#     print("there is an error")
# else:
#     print("non error")
# finally:
#     print("sucessfully completed")

# try:
#     print(x)
# except NameError:
#     print("check variable")
# except:
#     print("there is an error")

x=int(input("enter a number"))
if x<0:
    raise Exception("negative numbers are not allowed")
else:
    print("its a positive number")