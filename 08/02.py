def foo1(x):
    a = foo2(x*2)
    return a

def foo2(x):
    y = x+5
    return y

# foo1(5) returns 15
