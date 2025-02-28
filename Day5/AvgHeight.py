# student_heights = map(int,input("Enter a list of student heights").split())
student_heights = input("Input list of student heights: ").split()
for n in range(0,len(student_heights)):
    student_heights[n] = int(student_heights[n])

# total_height = sum(student_heights)
total_height=0
for height in student_heights:
    total_height+=height
# number_of_students = len((student_heights))
number_of_students = 0
for student in student_heights:
    number_of_students+=1
avg_height = total_height/number_of_students
print(round(avg_height,2))