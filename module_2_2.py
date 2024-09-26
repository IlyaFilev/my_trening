first = input('Привет, сравним три числа - введи первое целое число: ')
second = input('введи ещё одно целое число: ')
third = input('третье целое число: ')
rez = 'Совпадений:'
if first == second and second == third:
    print(rez, '3')
elif first == second or first == third or second == third:
    print(rez, '2')
else:
    print(rez, '0')
