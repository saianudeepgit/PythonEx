num1=float(input("enter first num"))
op1=input("enter operator one:")
num2=float(input("enter second num"))

if op1 == "+":
    print(num1+num2)
elif op1 == "-":
    print(num1-num2)
elif op1 == "*":
    print(num1*num2)
elif op1 == "/":
    print(num1/num2)
else:
    print("invalid operator")
