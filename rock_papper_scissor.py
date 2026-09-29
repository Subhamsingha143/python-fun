import random
ch=["rock","paper","scissor"]
player=input("choose rock , paper or scissor: ")
computer=random.choice(ch)
if player not in ch:
 print("please choose a valid option..")
else:
 print("computer choice : ",computer)
 if player==computer:
  print("its a draw!")
 else:
  if player=="rock" :
   if computer=="scissor":
    print("player wins..")
   else:
    print("computer wins..")
  if player=="paper":
    if computer=="rock":
     print("player wins..")
    else:
     print("computer wins..")
  if player=="scissor":
    if computer=="paper":
     print("player wins...")
    else:
     print("computer wins..")

 print("game over!")