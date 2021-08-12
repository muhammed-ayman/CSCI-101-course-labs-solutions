def getInput():
    value = float(input('Enter angle between 0 and 360 > '))
    if value < 0 or value > 360:
        print('Invalid Angle!')
        getInput()
    else:
        return value
