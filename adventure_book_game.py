name = input("Type your name: ")
print ("Welcome", name, "to this adventure!")

answer= input(
  "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
  answer= input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")
  if answer == "swim":
    print("You swam across and were eaten by alligator")

  elif answer == "walk":
    print("You walked for many miles, ran out of water and lost the game")

  else:
    print("Not a valid option. You lose")


elif answer == "right":
  answer = input("You come to a bridge, it looks unstable, do you want to cross it or head back? (Type cross or back) ")

  if answer == "back":
    print("You go back and loose the game.")

  elif answer == "cross":
      answer = input("You cross the bridge and meet a stranger. Do you talk to them? (type yes or no)")
      if answer == "yes":
          print("You talk to the stranger and they give you gold. You win!")
      elif answer == "no":
          print("You ignored the stranger and they didn't like it. You loose!")
      else:
          print("Not a valid option. You lose")
  else:
    print("Not a valid option. You lose")
else:
  print("Not a valid option. You lose")

print("Thank you for playing", name)