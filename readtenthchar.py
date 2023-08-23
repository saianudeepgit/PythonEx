import os
f=open("tenthChar.txt","r")
item=list(f.readlines())
print(item[1])
f.close()