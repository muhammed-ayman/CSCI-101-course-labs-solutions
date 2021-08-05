
friends = input('Friends > ').split(',')
presents = input('Presents > ').split(',')
in_mind = input('What is in joy\'s mind > ')

found = False
for i in range(len(presents)):
    if presents[i] == in_mind:
        print(f'Oh {friends[i]}, Thank you friend :)')
        found = True

if not found:
    print('Opps,Sorry none.')
