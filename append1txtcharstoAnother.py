firstfile = input("Enter the name of first file ")
secondfile = input("Enter the name of second file ")
 
f1 = open(firstfile, 'r')
f2 = open(secondfile, 'r')
 
print('content of first file before appending -', f1.read())
print('content of second file before appending -', f2.read())
f1.close()
f2.close()

f1 = open(firstfile, 'a+')
f2 = open(secondfile, 'r')
f1.write(f2.read())
 
f1.seek(0)
f2.seek(0)
print('content of first file after appending -', f1.read())
print('content of second file after appending -', f2.read())
 
f1.close()
f2.close()