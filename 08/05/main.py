import convertRectToPolar

rect_input = input('Enter Rectangular Coordinates in the following form: x y > ').split()
res = convertRectToPolar.rect2polar(float(rect_input[0]),float(rect_input[1]))
print(f'Polar Coordinates: {res}')
