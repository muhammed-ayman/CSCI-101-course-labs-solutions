L = [1, 12, -3, -50, 7, -2]
X = [v>0 for v in L]
X = sum( [v>0 for v in L] )
X = [v*(v>0) for v in L]
X = sum( [v*(v>0) for v in L] )
X = min( [v*(v>0) for v in L] )
X = [v for v in L if v>0]
X = sum( [v for v in L if v>0] )
X = min( [v for v in L if v>0] )

"""
a: [True, True, False, False, True, False]
b: 3
c: [1, 12, 0, 0, 7, 0]
d: 20
e: 0
f: [1, 12, 7]
g: 20
h: 1

I: g
II: f
III: b
IV: h
"""
