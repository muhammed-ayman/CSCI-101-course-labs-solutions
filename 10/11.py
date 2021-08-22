def calcDist(point1, point2):
    distance = ((point1['x']-point2['x'])**2+(point1['y']-point2['y'])**2)**(1/2)
    return round(distance,1)

ref_point = input('Enter reference Point=').split(',')
points_count = int(input('Enter no. of points:'))
points = []
ref_point_dict = {}
ref_point_dict['x']=float(ref_point[0])
ref_point_dict['y']=float(ref_point[1])
points.append(ref_point_dict)
for i in range(points_count):
    point_dict = {}
    point = input('Enter a point: ').split(',')
    point_dict['x'] = float(point[0])
    point_dict['y'] = float(point[1])
    points.append(point_dict)

distances = []

for i in range(len(points)):
    if i+1 != len(points):
        distance = calcDist(points[0], points[i+1])
        distances.append(distance)

print(f'Points are:{points}')
print(f'Distance={distances}')
