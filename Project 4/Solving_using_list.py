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

choice_game = [rock, paper, scissors]

print("Rock Paper Scissors game")
print("Type 0 for rock, type 1 for paper, type 2 for scissor")

user_choice = int(input("Enter your choice: "))

if user_choice >=3 or user_choice < 0:
    print("Invalid Number. You lose!")
else:
    print(choice_game[user_choice])

    ai_choice = random.randint(0, 2)
    print("Computer picked")

    if ai_choice == 0:
        print(choice_game[ai_choice])
        if user_choice == 1:
            print("You win!")
        elif user_choice == 2:
            print("You lose!")
        else:
            print("It's a draw!")
    elif ai_choice == 1:
        print(choice_game[ai_choice])
        if user_choice == 0:
            print("You lose!")
        elif user_choice == 2:
            print("You win!")
        else:
            print("It's a draw!")
    elif ai_choice == 2:
        print(choice_game[ai_choice])
        if user_choice == 0:
            print("You win!")
        elif user_choice == 1:
            print("You lose!")
        else:
            print("It's a draw!")
