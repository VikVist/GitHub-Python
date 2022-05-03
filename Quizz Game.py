print("Welcome to engineering wonder quizzzz!")

quiz = input("Do you want to start the quiz?")

print(quiz)

if quiz.lower() != "yes":
  quit()

print("Awesome, let's dive into the engineering world")
score = 0

answer=input("Decimal number 10 is equal to binary number of:  ")
if answer.lower() == "1010":
  print('Correct!')
  score += 1
else:
  print('Not correct')

answer=input("What is the emissivity of a black body ")
if answer.lower() == "1":
  print('Correct!')
  score += 1
else:
  print('Not correct')

answer=input("What is the value of sound speed in dry air at 20 °C? ")
if answer.lower() == "343":
  print('Correct!')
  score += 1
else:
  print('Not correct')

answer=input("What does V stand for in electrics? ")
if answer.lower() == "voltage":
  print('Correct!')
  score += 1
else:
  print('Not correct')

answer=input("What is the hubble in one word? ")
if answer.lower() == "telescope":
  print('Correct!')
  score += 1
else:
  print('Not correct')

print("You have scorred " + str(score) + " from the quiz")


