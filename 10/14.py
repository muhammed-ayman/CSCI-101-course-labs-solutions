maps = input('> ').replace(' ', '')
tot_distance = 0

for i in maps:
    if i in 'RDLU':
        tot_distance += 1

maps = maps.split(',')
y_dist = len(maps)-1
x_dist = 0

to_ = list(maps[-1])[-1::-1]
here = 0
for i in to_:
    if i != 'x':
        break
    else:
        here += 1
x_dist = len(to_)-here
print(x_dist)
print(y_dist)
direct_dist = (y_dist**2+x_dist**2)**(1/2)
print(tot_distance)
print(f'the ratio = {tot_distance/direct_dist}')
