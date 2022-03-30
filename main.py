# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split(',')
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_heights = 0
for heights in student_heights :
    total_heights = heights + total_heights
print(total_heights)

numberof_students = 0
for number in student_heights:
    numberof_students = numberof_students + 1 

print(numberof_students)
average_height = round(total_heights/numberof_students) 
print(average_height)
#Write your code below this row 👇




