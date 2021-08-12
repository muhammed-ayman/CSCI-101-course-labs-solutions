# A:
def angleType(a):
    if a==0:
        return 'zero'
    elif a<90:
        return 'acute'
    elif a==90:
        return 'right'
    elif a<180:
        return 'obtuse'
    elif a==180:
        return 'straight'
    elif a<360:
        return 'reflex'
    else:
        return 'complete'
# B:
def GeneralAngleType(b):
    if b<0:
        return 'negative'
    elif b >= 0 and b <= 360:
        return angleType(b)
    else:
        angle = b * (1-b//360)
        return angleType(angle)
