# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

new_password = " "

# nr_letters = 2
# nr_symbols = 2
# nr_numbers = 2
for letter in range(1, nr_letters + 1):
    random_chars1 = random.choice(letters)
    new_password = new_password + random_chars1
    # print(new_password)
for symbol in range(1, nr_symbols + 1):
    random_chars2 = random.choice(symbols)
    # new_password = new_password + random_chars1 + randon_chars2
for num in range(1, nr_numbers + 1):
    random_chars3 = random.choice(numbers)
    new_password = new_password + random_chars1 + random_chars2 + random_chars3
print(new_password)
