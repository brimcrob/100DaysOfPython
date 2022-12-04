import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

# Write your code below this line 👇

"""
The Rules
Rock wins against paper
Scissors win against paper
Paper wins against rock
both players draw the same go again.  
"""
choice = [rock, paper, scissors]
# create the generation of the computers choice


option_zero = choice[0]
option_one = choice[1]
option__two = choice[2]
player_choice = input(
    "Please enter 0 for rock, 1 for paper and 2 for scissors and 3 for paper\n "
)

if player_choice == choice[0]:
    print(option_zero)
elif player_choice == choice[1]:
    print(option_one)
elif player_choice == choice[2]:
    print(option__two)

# computer_go = random.choice(tuple(choice))
# print(computer_go)
