
#1 : because the value of c doesn't change
#1 Fix:
c=0
while c<10:
    c += 1
    print(c)

#2 : because the value of a keeps on decreasing and the difference between it and 10 increases
#2 Fix:
a=0
while a<10:
    a += 1
    print(a)

#3 : although the value of b is incremented by 2, it gets assigned to zero again
#3 Fix:
b = 0
while b<10:
    b += 2
    print(b)
