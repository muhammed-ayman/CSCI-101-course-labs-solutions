
passwd = input('Enter the password > ')

if len(passwd) < 6 or len(passwd) > 20:
    print('Invalid!')
    exit()

letter_checked = 0
number_checked = 0
character_checked = 0
upper_checked = 0

for i in passwd:
    if letter_checked == 1 and number_checked == 1 and upper_checked == 1 and character_checked == 1:
        print('Valid')
        exit()
    if (ord(i) >= 65 and ord(i) <= 90) and (upper_checked == 0):
        upper_checked += 1
    if (ord(i.lower()) >= 97 and ord(i.lower()) <= 122) and (letter_checked == 0):
        letter_checked += 1
    if (i in '$#@') and (character_checked == 0):
        character_checked += 1
    if (i in '0123456789') and (number_checked == 0):
        number_checked += 1

print('Invalid!')
