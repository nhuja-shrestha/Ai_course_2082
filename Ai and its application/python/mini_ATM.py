balance=10000  #initial balance
while True:
  print("/--ATM simulator--/")
  print("1.Check balance")
  print("2.Withdraw")
  print("3.Deposit")
  print("4.Exit\n\n")
  choice=int(input("Enter your choice:\n"))
  if choice==1:
    print(f"Your balance is:{balance}\n")
  elif choice==2:
    withdraw=int(input("Enter the amount to withdraw:\n"))
    if withdraw>balance:
      print("Insufficient balance!!!\n")
    else:
      balance-=withdraw
      print("Your remaining balance is:",balance,"\n")
  elif choice==3:
    deposit=int(input("Enter the amount to deposit:\n"))
    balance+=deposit
    print(f"Rs.{deposit} was added to your previous balance\nYour updated balance is: Rs.{balance}\n")
  elif(choice==4):
    print("Thank you for using atm simulator")
    print(f"You have Rs.{balance} remaining in your account!!!\n")
    break
  else:
    print("Invalid option")