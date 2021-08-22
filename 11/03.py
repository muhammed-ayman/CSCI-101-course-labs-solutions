x=[-4,1,2,3,4,50,0]

a = sum([v>0 for v in x if v!=0])
b = [i for i in range(len(x)) if x[i]!=0]
c = [v for v in x if (v in range(-3,50))]
d = max([v for v in x if v%3 == 0])
e = sum([v for v in x if v > 10])/len([v for v in x if v > 10])
f = [i for i in range(len(x)) if x[i] == min(x)]
