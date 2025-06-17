def converter(a,b):
  return a*b
print("welcome to currency converter:\n")
print("options available:")
print("1. NPR to INR")
print("2. NPR to USD")
print("3. NPR to AUD")
print("4. NPR to euro")
amount=int(input("ENter your amount(in NPR):\n"))
choice=int(input("Enter your conversion choice:\n"))
if(choice==1):
  rate=0.63
  print("result:",converter(amount,rate),"INR")
elif(choice==2):
  rate=0.0073
  print("result:",converter(amount,rate),"USD")
elif(choice==3):
  rate=0.011
  print("result:",converter(amount,rate),"AUD")
elif(choice==4):
  rate=0.0065
  print("result:",converter(amount,rate),"euros")