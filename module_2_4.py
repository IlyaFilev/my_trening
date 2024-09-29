# Задача "Всё не так уж просто": Д/з на "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True # не понимаю, зачем мне эта переменная
for i in numbers:
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                not_primes.append(i)
                break
            else:
                primes.append(i)
print('Primes: ', primes)
print('Not primes: ', not_primes)
