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
# game images
game_images = [rock, paper, scissors]

player_chocie = int(input("Please enter 0 for rock, 1 for paper,  2 for scissors\n "))
print(game_images[player_chocie])
comp_choice = random.randint(0, 2)
print(game_images[comp_choice])

# 0 = rock
# 1 = scissors
# 2 = paper
if player_chocie == 0 and comp_choice == 2:
    print("Player wins")
elif comp_choice == 0 and player_chocie == 2:
    print("You lost! ")
elif comp_choice > player_chocie:
    print("You lose! ")
elif player_chocie > comp_choice:
    print("You Win! ")
elif comp_choice == player_chocie:
    print("Its a draw. ")
elif player_chocie >= 3 or player_chocie < 0:
    print("You typed an invalid number, you lose ")
