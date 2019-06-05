number = input()
for digit in number:
    print(digit)

a = input('Введите первое число: ')
b = input('Введите второе число: ')
temp = a
a = b
b = temp
print('Первое чилос теперь: ',a,'\nВторое число теперь:', b)

age = int(input('Введите ваш возраст:'))
if age >= 18:
    print('Доступ разрешен')
else:
    print('Извините, пользование данным ресурсом только с 18 лет')