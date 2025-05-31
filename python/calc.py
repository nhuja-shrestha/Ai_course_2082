#WAP TO CREATE SIMPLE CALCULATOR

a=int(input("Enter your first number:"))
b=int(input("Enter your second number:"))
c=str(input("Enter your operation:"))
def sum(a, b):
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if(b!=0):
        return a/b
    else:
        return "Math error!!"
if c=='+':
    print("Result:", sum(a, b))
elif c=='-':
    print("Result:", sub(a, b))
elif c=='*':
    print("Result:", mul(a, b))
elif c=='/':
    print("Result:", div(a, b))
else:
    print("Invalid operator")
