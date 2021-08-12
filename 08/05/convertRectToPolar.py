import math
def rect2polar(x,y):
    r = (x**2+y**2)**(1/2)
    theta = math.atan(y/x)
    return r,theta
