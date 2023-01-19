# Write your code below this line 👇
import math


def paint_calc(height, width, cover):
    cover = (height * width) / cover
    # print(math.ceil(cover))
    cover = math.ceil(cover)
    print(f"You'll need {cover} cans of paint")


# Write your code above this line 👆2
# Define a function called paint_calc() so that the code below works.

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
