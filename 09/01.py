x = [1,2,3,4,5,6]

#a
result = sum(x)

#b
result = sum([i for i in x if i%2!=0])

#c
result = sum([i for i in range(len(x)) if i%2!=0])

#d
result = any([i for i in x if i > 0])

#e
result = sum([1 for i in x if i>0])

#f
result = True if sum([1 for i in x if i > 0]) == 0 else False
