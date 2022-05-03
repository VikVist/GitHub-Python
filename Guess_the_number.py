import random

top_of_range=input("Please choose top of range value: ")

if top_of_range.isdigit():
  top_of_range=int(top_of_range)

else:
  print("Please enter a number next time")
  quit()

random_value=random.randint(0,top_of_range)
guess=0
print(random_value)

while True:
  guess+=1
  guess_value=input("Please guess a value in the range from 0 to " + str(top_of_range) + ": " )

  if guess_value.isdigit():
    guess_value=int(guess_value)

  else:
    print("Please enter a number next time")
    continue

  if guess_value == random_value:
    print("You got it!")
    print("You got it right in " + str(guess) + " guesses")  
    break
  elif guess_value>random_value:
    print("You were above the number")
  else:
    print("You were below the number")
  
