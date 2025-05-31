p=int(input("Enter your sum:\n"))
t=int(input("Enter your time:\n"))
r=float(input("Enter your rate:\n"))
def SI(a,b,c):
    return (a*b*c)/100
print("your interest is",SI(p,t,r))