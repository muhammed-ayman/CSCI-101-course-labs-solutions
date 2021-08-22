G = [ {'name':'ahmed','grade':12},{'name':'mohamed','grade':15},
{'name':'hassan','grade':19},{'name':'hana','grade':11} ]
X = [ v['name'] for v in G if v['grade']>12 ]

"""
['mohamed', 'hassan']
"""
