# Задача "Всё не так уж просто": Д/з на "Цикл for. Элементы списка. Полезные функции в цикле"
# Используя этот список составьте второй список primes содержащий только простые числа.
# А так же третий список not_primes, содержащий все не простые числа.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True # эта переменная является Флагом (переключателем)
for i in numbers:
    if i == 1:
        continue
    else:
        for j in range(2, i): # 2 не проверяется, True не меняется => добавляется в primes
            if i % j == 0:
                is_prime = False
                break   # останавливаем, иначе след значение i может перещёлкнуть переменную
            else:
                is_prime = True
    if is_prime == True:
        primes.append(i)
    else:
        not_primes.append(i)
print('Primes: ', primes)
print('Not primes: ', not_primes)

