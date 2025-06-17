import random
options=["rock","paper","scissor"]
while True:
  
  computer=random.choice(options)
  player=str(input("ENter your choice(rock/paper/scissor)"))
  print(f"computer:{computer}\nPlayer:{player}")
  if computer == player:
    print("Draw")
  elif computer=="rock":
    if player=="scissor":
      print("computer wins🥳")
    elif player=="paper":
      print("player wins🥳")
  elif computer=="paper":
    if player=="rock":
      print("computer wins🥳")
    elif player=="scissor":
      print("player wins🥳")
  elif computer=="scissor":
    if player=="paper":
      print("computer wins🥳")
    elif player=="rock":
      print("player wins🥳")
  choice=str(input("Do you want to continue?(yes/no):")).lower()
  if choice!="yes":
    print("Thanks for playing!!😌")
    break
  
      





