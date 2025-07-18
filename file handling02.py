# # q=open("jolfiya.txt","x")
# q=open("jolfiya.txt","w")
# q.write("jolfiya joseph")
# q.write("\nvarapolackal")
# q.close()

# # q=open("jolfiya.txt","x")
# q=open("jolfiya.txt","a")
# q.write("\nidukki")
# q.close()

# # q=open("jolfiya.txt","x")
# q=open("jolfiya.txt","r")
# print(q.read())
# q.close()

# # q=open("jolfiya.txt","x")
# q=open("jolfiya.txt","r")
# print(q.read(14))
# q.close()

# # q=open("jolfiya.txt","x")
# q=open("jolfiya.txt","r")
# print(q.readline())
# print(q.readline())
# print(q.readline())
# q.close()

# q=open("joseph.txt","x")
# import os
# os.remove("joseph.txt")

# m=open("file01.txt","x")
# n=open("file02.txt","x")
m=open("file01.txt","w")
m.write("my name is jolfiya")
m.close()
m=open("file01.txt","r")
c=m.read()
m.close()
n=open("file02","w")
n.write(c)
n.close()

