student_scores = input("Input a list of student scores: ").split()
for n in range(0,len(student_scores)):
    student_scores[n] = int(student_scores[n])

max_score = student_scores[0]
for score in range(1,len(student_scores)):
    if max_score < student_scores[score]:
        max_score = student_scores[score]
print(f"Highest score is : {max_score}")