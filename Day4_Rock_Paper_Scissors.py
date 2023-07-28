import random

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


photo = [rock, paper, scissors]
computer = random.randint(0,1)

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))
if player >= 3 or player <0:
    print("Invalid!")
else: 
    print(photo[player])
    print("Computer chose:")
    print(photo[computer])
    
    if computer == 1 and player == 0:
        print("You lose!")
    if computer == 2 and player == 0:
        print("You win!")
    elif computer == 0 and player == 1:
        print("You win!")
    elif computer == 2 and player == 1:
        print("You lose!")
    elif computer == 0 and player == 2:
        print("You lose!")
    elif computer == 1 and player == 2:
         print("You win!")
    else:
        print("Tie!")
