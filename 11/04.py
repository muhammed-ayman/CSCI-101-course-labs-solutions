L = [
    {
        'name':'ahmed',
        'math_grade': 14,
        'physics_grade': 13
    },
    {
        'name':'khalid',
        'math_grade': 15,
        'physics_grade': 12
    },
    {
        'name':'mohamed',
        'math_grade': 3,
        'physics_grade': 3
    }
]

a = [v['name'] for v in L if v['math_grade'] >= 12]
b = [v['name'] for v in L if v['math_grade']+v['physics_grade'] < 10][0]
c = [v['name'] for v in L if v['math_grade'] == max([v['math_grade'] for v in L])]
