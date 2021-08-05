class_1 = input('Class 1 grades > ').split()
class_1_students = input('Class 1 Students > ').split()
class_2 = input('Class 2 grades > ').split()
class_2_students = input('Class 2 Students > ').split()


# Class 1:
for j in range(len(class_1)):
    for i in range(len(class_1)):
        if i+1 != len(class_1):
            if int(class_1[i]) < int(class_1[i+1]):
                class_1[i] , class_1[i+1] = class_1[i+1] , class_1[i]
                class_1_students[i] , class_1_students[i+1] = class_1_students[i+1] , class_1_students[i]

# Class 2:
for j in range(len(class_2)):
    for i in range(len(class_2)):
        if i+1 != len(class_2):
            if int(class_2[i]) < int(class_2[i+1]):
                class_2[i] , class_2[i+1] = class_2[i+1] , class_2[i]
                class_2_students[i] , class_2_students[i+1] = class_2_students[i+1] , class_2_students[i]

print(f'class 1 grades sorted from highest to lowest grade {class_1}')
print(f'class 2 grades sorted from highest to lowest grade {class_2}')
print(f'class 1 students sorted from highest to lowest grade {class_1_students}')
print(f'class 2 students sorted from highest to lowest grade {class_2_students}')

highest_grade = int(class_1[0])
if int(class_2[0]) > highest_grade:
    print(f'the student with the highest grade is {class_2_students[0]} in class 2')
else:
    print(f'the student with the highest grade is {class_1_students[0]} in class 1')
