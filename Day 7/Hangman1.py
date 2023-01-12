# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)
word_length = len(chosen_word)


# create the blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)


# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter : ").lower().strip()
print(guess)
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Replace the _ with the correct letter
for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)
