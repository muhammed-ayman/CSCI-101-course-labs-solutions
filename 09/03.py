def myFun(N):
    if N <= 0:
        return 0
    return 1+myFun(N-1)

print(myFun(4)) # 4
