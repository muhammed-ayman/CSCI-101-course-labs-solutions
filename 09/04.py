def f(x,y):
    if y == 0:
        return x
    return f(y,x%y)
print(f(60,48)) #12
print(f(33,21)) #3
