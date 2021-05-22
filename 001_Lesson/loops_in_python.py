# for
words = ['list', 'dict', 'tuple']
upper_words = []
for word in words:
    upper_words.append(word.upper())

print(upper_words)

numbers = [20, 1, 3, 1, 2, 3, 4, 5, 100]
for number in numbers:
    print(number)

for i in range(10):
    print(i)

for i in range(1,10,2):
    print(i)

ukraine_city = {
    'kyiv':
        {
            'Area': '839',
            'Population': '2,950,819'
        },
    'rivne':
        {
            'Area': '63.00',
            'Population': '246,003'
        }
}

for city in ukraine_city:
    print(city)

for key in ukraine_city:
    print(ukraine_city[key])

for key in ukraine_city:
    print(key)
    for value in ukraine_city[key]:
        print(value)
        print(ukraine_city[key][value])

counter = 5
while counter >= 0:
    print(counter)
    counter -= 1

username = input('Введите имя пользователя: ')
password = input('Введите пароль: ')

password_correct = False

while not password_correct:
    if len(password) < 8:
        print('Пароль слишком короткий\n')
        password = input('Введите пароль еще раз: ')
    elif username in password:
        print('Пароль содержит имя пользователя\n')
        password = input('Введите пароль еще раз: ')
    else:
        print(f'Пароль для пользователя {username} установлен')
        password_correct = True
