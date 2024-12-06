'''Декораторы
Задача:
1. Функция, которая складывает 3 числа (sum_three)
2. Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом и
"Составное" в противном случае.
'''

def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for j in range(2, int(res ** 0.5) + 1):
            if res % j == 0:
                print(res, 'Составное')
            else:
                print(res, 'Простое')
    return wrapper


@is_prime
def sum_three(*args):
    summ = sum(args)
    return summ


sum_three(1, 1, 1)

'''
def is_prime(func):
    def wrapper(*args):
        res_ = func(*args)
        # if isinstance(res_, int):
        for j in range(2, int(res_**0.5)+1):
            if res_ % j == 0:
                print(res_, 'Составное')
            else:
                print(res_, 'Простое')
        
    return wrapper
'''