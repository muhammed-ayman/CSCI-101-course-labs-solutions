grades_list = input('Enter grades list > ').split(' ')
sum = 0
sum_count = 0
validity_grades = []
higher_85 = []
higher_50 = []
highest_grade = int(grades_list[0])
lowest_grade = int(grades_list[0])
highest_grade_location = 0
lowest_grade_location = 0
for i in range(len(grades_list)):
    if int(grades_list[i]) >= 0 and int(grades_list[i]) <= 100:
        print(f'{grades_list[i]} is Valid')
        sum += int(grades_list[i])
        sum_count += 1
        validity_grades.append(1)
        if int(grades_list[i])>85:
            higher_85.append(i)
        if int(grades_list[i])>50:
            higher_50.append(i)
        if highest_grade > 100:
            highest_grade=int(grades_list[i])
        if lowest_grade < 0:
            lowest_grade=int(grades_list[i])
        if int(grades_list[i]) >= highest_grade:
            highest_grade=int(grades_list[i])
            highest_grade_location=i
        if int(grades_list[i]) <= lowest_grade:
            lowest_grade=int(grades_list[i])
            lowest_grade_location=i
    else:
        print(f'{grades_list[i]} is Invalid')
        validity_grades.append(0)
print(validity_grades)
if sum_count != 0:
    print(f'Average={sum/sum_count}')
else:
    print('Average cant be calculated when all grades are invalid')
print(f'Highest Grade={highest_grade}, its location={highest_grade_location}')
print(f'Lowest Grade={lowest_grade}, its location={lowest_grade_location}')
print(f'Students that have higher than 85% locations: {higher_85}, and their count={len(higher_85)}')
print(f'Students that have higher than 50% locations: {higher_50}, and their count={len(higher_50)}')
