name_grade = {
    'student1': {'name': 'x', 'grade': 'B'},
    'student2': {'name': 'y', 'grade': 'D'},
    'student3': {'name': 'happy_zewailian', 'grade': 'A'}
}

for student in name_grade.keys():
    if name_grade[student]['name'] == 'happy_zewailian':
        name_grade[student]['grade'] = 'F'

print(name_grade)
