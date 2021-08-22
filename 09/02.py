def sumVal(N):
    if N<=0:
        return 0
    return N+sumVal(N-1)
