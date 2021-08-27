import random

# Magic 8-ball, based on CA assignment with user input for name

# User inputs name
name = input('What is your name?: ')

# Returns name for interactivity
print("Hello " + name)

# User inputs question
question = input("What is your question?: ")

# Empty string for answer variable
answer = ""

# Random number generator
random_number = random.randint(1,10)

# Answer list
if random_number == 1:
  answer = "Yes, definately."
elif random_number == 2:
  answer = "It is decidedly so."
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "Nah"
else:
  answer = "Error, please enter number between 1 and 9"

# Error handling for if the name is left empty
if name == "":
  print("Question: " + question)
else:
  print(name + " asks: " + question)

# Final answer
print("Magic 8-Ball's answer: " + answer)