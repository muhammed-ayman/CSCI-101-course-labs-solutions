statement = input('Enter the statement > ')
vowels = 'aeiouy'
vowels_count = 0

for chara in statement:
    if chara.lower() in vowels:
        vowels_count += 1

if vowels_count != 0:
    print(f'The number of vowel letters {vowels_count}')
else:
    print('No vowels found')
