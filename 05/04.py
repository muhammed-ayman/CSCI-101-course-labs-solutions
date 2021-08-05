
que_answer = input('What did team members bring').split()

# A solution
found = False
for word in que_answer:
    if word == 'battery':
        found = True
        break

if found:
    print('I don\'t need to bring the battery')
else:
    print('I will need to bring the battery')

# B solution

if 'battery' in que_answer:
    print('I don\'t need to bring the battery')
else:
    print('I will need to bring the battery')
