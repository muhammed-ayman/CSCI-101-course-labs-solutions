def add_squares(n):
    if n == 1:
        return 1
    return n**2+add_squares(n-1)
