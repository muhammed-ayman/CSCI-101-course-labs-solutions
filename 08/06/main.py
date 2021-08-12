import scoreToGrade

students_scores = input('Enter Students Scores > ').split()
students_grades = []

for i in students_scores:
    students_grades.append(scoreToGrade.scoreToGrade(int(i)))

print(f'Students Grades > {students_grades}')
