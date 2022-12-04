# # 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# # 🚨 Don't change the code above 👆
combined_names = name1 + name2
t = combined_names.count("t")
r = combined_names.count("r")
u = combined_names.count("u")
e = combined_names.count("e")
true_total = t + r + u + e
print(true_total)

l = combined_names.count("l")
o = combined_names.count("o")
v = combined_names.count("v")
e2 = combined_names.count("e")
love_total = l + o + v + e2
#print(love_total)
total_love_score = int(str(true_total) + str(love_total))
#print(total_love_score)

if total_love_score < 10 or total_love_score > 90:
    print(f"Your score is {total_love_score},you go together like coke and mentos.")
elif total_love_score >= 40 and total_love_score <= 50:
    print(f"Your score is {total_love_score}, you are alright together.")
else:
    print(f"Your score is {total_love_score}.")
