'''Блокировки и обработка ошибок
Задача "Банковские операции"
Скрипт разблокирующий поток до баланса равному 500 и больше
 или блокирующий, когда происходит попытка снятия при недостаточном балансе.
'''
import threading
import time
from random import randint
from time import sleep


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock() # lock - объект класса Lock для блокировки потоков.

    def deposit(self):
        for i in range(1,101):
            replenishment = randint(50, 500) # сумма Пополнения = случайному целому числу от 50 до 500.
            self.balance += replenishment
            if self.balance >= 500 and self.lock.locked() == True: # Если баланс больше или равен 500 и замок lock заблокирован,
                self.lock.release()  # то производим разблокировку
            print(f'Транзакция {i}. Пополнение: {replenishment}. Баланс: {self.balance}')
            time.sleep(0.001) # ожидание в 0.001 секунды - имитация скорости выполнения пополнения.

    def take(self):
        for i in range(1,101):
            withdrawal  = randint(50, 500) # сумма Снятия
            print(f'Запрос на {withdrawal}')
            if self.balance >= withdrawal: # проверка платежеспособности, если подтверждается, то
                self.balance -= withdrawal # производим снятие суммы с баланса
                print(f'Транзакция {i}. Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire() # при недостаточном балансе для снятия - заблокировать поток
            time.sleep(0.001)

bk = Bank()
# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')