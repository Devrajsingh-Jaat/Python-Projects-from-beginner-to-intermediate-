rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
import sys

print("Rock Paper Scissors game")
print("Type 0 for rock, type 1 for paper, type 2 for scissor")

try:
    user_choice = int(input("Enter your choice: "))
except ValueError:
    sys.exit()

if user_choice in (0, 1, 2):
    if user_choice == 0:
        print(rock)
    elif user_choice == 1:
        print(paper)
    elif user_choice == 2:
        print(scissors)
else:
    sys.exit()

print("Computer Chose: ")

AI_choice = random.randint(0, 2)

if AI_choice == 0:
    print(rock)
    if user_choice == 1:
        print("You win!")
    elif user_choice == 2:
        print("You lose!")
    else:
        print("It's a draw!")
elif AI_choice == 1:
    print(paper)
    if user_choice == 0:
        print("You lose!")
    elif user_choice == 2:
        print("You win!")
    else:
        print("It's a draw!")
elif AI_choice == 2:
    print(scissors)
    if user_choice == 0:
        print("You win!")
    elif user_choice == 1:
        print("You lose!")
    else:
        print("It's a draw!")
