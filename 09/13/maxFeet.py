def maxFeet():
    n = int(input('Enter the maximum length in feet > '))
    if n >= 1:
        return n
    else:
        print('Invalid Input!')
        maxFeet()
