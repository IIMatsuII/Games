import random

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''


n = int(input('Введите кол-во паролей для генерации: '))
length = int(input('Введите длину пароля: '))
add_digits = input('Включить цифры?: (y - Да, n - Нет): ').strip()
add_lowercase = input('Включить прописные буквы (y - Да, n - Нет): ').strip()
add_uppercase = input('Включить строчные буквы (y - Да, n - Нет): ').strip()
add_puncuation = input('Включить символы !#$%&*+-=?@^_ (y - Да, n - Нет): ').strip()
remove_badsymbol = input('Исключить символы il1lo0O? (y - Да, n - Нет): ').strip()

if add_digits.lower() == 'y':
    chars += digits
if add_lowercase.lower() == 'y':
    chars += lowercase_letters
if add_uppercase.lower() == 'y':
    chars += uppercase_letters
if add_puncuation.lower() == 'y':
    chars += punctuation
if remove_badsymbol.lower() == 'y':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password

for _ in range(1, n+1):
    print(generate_password(length, chars))




'''
list_of_words = [
    'Укажите количество паролей для генерации: ',
    'Укажите длину одного пароля: ',
    'Включать ли цифры 0123456789? (y/n): ',
    'Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n): ',
    'Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n): ',
    'Включать ли символы !#$%&*+-=?@^_? (y/n): ',
    'Исключать ли неоднозначные символы il1Lo0O? (y/n): '
]
'''