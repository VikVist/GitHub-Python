import random

user_wins=0
computer_wins=0
equal=0

list_1=["rock", "paper", "scissors"]

while True:
  user_input=input("Type Rock,Paper or Scissors or Type Q to quit: ").lower()
  if user_input=="q":
    break
  if user_input not in list_1:
    continue
  computer_selector=random.choices(list_1)
  computer_input=computer_selector[0]
  print("Computer picked", computer_input)

  if user_input=="rock" and computer_input=="scissors":
    user_wins += 1


  elif user_input=="scissors" and computer_input=="paper":
    user_wins += 1  


  elif user_input=="paper" and computer_input=="rock":
      user_wins += 1


  elif user_input==computer_input:
    equal += 1   


  else:
    print("You have lost!")
    computer_wins += 1
    
  print("The user has won ", user_wins," times the game")
  print("The computer has won ", computer_wins, " times the game")
  print("There were ", equal,"equal rounds.")
  
  


  
