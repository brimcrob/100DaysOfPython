# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
# input 78 65 89 86 55 91 64 89

max_student_score = 0

for score in student_scores:
    if score > max_student_score:
        max_student_score = score


print(f"The Highest Score in the Cliass is : {max_student_score}")
