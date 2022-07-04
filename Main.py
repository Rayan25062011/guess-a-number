import time
import random

# Game begins here
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int (input(f"Guess a number between 1 and {x}:  "))
        if guess < random_number:
            print("Sorry, guess again, too low.")
        elif guess > random_number:
            print("Sorry, guess again, too high.")
        if guess == random_number:
            print(f"Congrats! You found {random_number} correct correctly!!!")

userChoice = 2
while userChoice == 2:
  guess(10)
  rate = int(input("Rate us! (1 for 1 star, 2 for 2 stars,.. up to 4 stars) "))
  if rate <= 1:
      print("Why? Write what did you not like down here: ")
      star_1 = input("Write here: ")
      print("\nFeedback sent!")
  if rate == 2:
      print("\nThank you for your feedback!")
  if rate == 3:
      print("\nThank you for your feedback")
  if rate >= 4:
      print("\nWow! We are glad you enjoyed our game!")
  time.sleep(1.6)
  print("1- Type 1 to exit game")
  print("2- Type 2 to make a new game")
  userChoice = int(input("Choose an option: "))
  if userChoice == 1:
    print("\tbye bye!")
    break
  else:
    userChoice = 2
