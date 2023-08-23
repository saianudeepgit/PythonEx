import os

os.mkdir("somefldr")
f=open("somefldr\\text.txt","w")
for i in range(0,101):
 print(i,file=f)
 if i > 50 and i < 72 and i % 3 ==0:
  print(i,file=f,end=" ")
f.close()