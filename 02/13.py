import random
num = random.randint(10,20)

success = False

for i in range(5):
    guess = int(input('Enter Number > '))
    if guess == num:
        success = True
        break;
    else:
        print('wrong guess')

if success:
    print('Well Done!')
