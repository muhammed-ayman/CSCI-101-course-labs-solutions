grade_points = {
    'A':4,
    'B':3,
    'C':2.7,
    'D':2,
    'F':0
}
inputted_value = input('> ').split(' ,')
students = inputted_value[0].split()
grades = inputted_value[1].split(',')

for i in range(len(students)):
    gpa = 0
    count = 0
    student_grades = grades[i].split()
    for grades_ in range(len(grades)):
        gpa += grade_points[grades[grades_][i]]
        count += 1
    print(f'{students[i]} Has GPA: {round(gpa/count,2)}')
