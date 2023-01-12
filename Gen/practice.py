user1 = int(input("please enter a number between 1-10"))
user2 = int(input("please enter a number between 1-10"))
combi_num = [user1, user2]
total_score = sum(combi_num)
mean1 = sum(combi_num) / len(combi_num)
print(f"total score is {total_score}")

print(f" this is the mean {mean1}")
