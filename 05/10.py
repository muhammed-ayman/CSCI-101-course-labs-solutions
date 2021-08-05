
user_input = input('Enter the coordinates in the following form [a b c] (example: [0 1 2]) > ')[1:-1].split()
a = int(user_input[0])
b = int(user_input[1])
c = int(user_input[2])

if a == 0 and b == 0 and c == 0:
    print('Any x is a solution')
elif  a == 0 and b == 0 and c != 0:
    print('No solution')
elif a == 0:
    print(-c/b)
else:
    solution1 = (-b+(b**2-4*a*c)**(1/2))/(2*a)
    solution2 = (-b-(b**2-4*a*c)**(1/2))/(2*a)
    print(solution1)
    print(solution2)
