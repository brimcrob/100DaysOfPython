# for number in range(1, 11, 3):
# print(number)

# total = 0
# for number in range(1, 101):
# total += number
# print(total)

# my solution
"""total = 0
for number in range(1, 101):
    if (number % 2) == 0:
        total += number
print(total)
"""
# proper solution
total = 0
for number in range(2, 101, 2):
    total += number
print(total)
