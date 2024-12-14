'''
Очереди для обмена данными между потоками
Задача "Потоки гостей в кафе":
Необходимо имитировать ситуацию с посещением гостями кафе.
'''
import threading
import time
from queue import Queue
from random import randint

class Table:
    def __init__(self, number, guest=None):
        self.number = number
        self.guest = guest


class Guest(threading.Thread):

    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run (self):
        for
        replenishment = randint(3, 10) # Обладать run, где происходит ожидание случайным образом от 3 до 10 с.


class Cafe:

    def __init__(self, *tables):
        self.table = tables
        self.queue = Queue()

    def guest_arrival(self, *guests):  # Если есть свободный стол, то садить гостя за стол (назначать столу guest),
                # запускать поток гостя и выводить на экран строку "<имя гостя> сел(-а) за стол номер <номер стола>".
        if
        for i in range(guests):
            self.queue.put(self.i)

    def discuss_guests(self, *guests):




'''Выполняемый код:
class Table:
...
class Guest:
...
class Cafe:
...'''
# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()

